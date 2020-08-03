import os

import psycopg2 as pg
import openai

from default_prompt import default_prompt

# HELPER METHODS
def get_openai_key():
    """
        Utility method to retrieve openAI key.
        Check to see whether key present in CWD.

        Parameters
        ----------
        None
    """
    current_working_dir = os.getcwd()
    theoretical_path = os.path.join(current_working_dir, "openai-credentials.txt")

    if os.path.isfile(theoretical_path):
        with open(theoretical_path) as fl:
            key = fl.read()
            key = key.strip()
        
        return key
    else:
        return None

# PRIMARY CLASSES/METHODS
class Cursor:
    """
        Postgres cursor wrapper.
    """
    def __init__(self):
        # connection options
        self.host = os.environ['PG_HOST']
        self.user = os.environ['PG_USER']
        self.password = os.environ['PG_PASSWORD']

        self.conn = pg.connect(host=self.host, user=self.user, password=self.password)

        self.crs = self.conn.cursor()
    
    def _get_cols(self):
        """
            Private helper method to get the columns of a query result.
        """
        return [desc[0] for desc in self.crs.description]

    def commit(self):
        """
            Public method to commit database changes. To be used after 'write' queries.
        """
        self.conn.commit()

    def fetch_dict(self, query):
        """
            Public method to get query result as a list of dictionaries.

            Parameters
            ----------
            query : {str}
                PostgreSQL compatible query string.
        """
        self.crs.execute(query)

        cols = self._get_cols()

        result = self.crs.fetchall()

        return [dict(zip(cols, res)) for res in result]

class QueryPipeline:
    """
        Primary query pipeline class. APIs should create an instance of this class
        and then build prompts / query.
    """

    def __init__(self, **kwargs):
        """
            Parameters
            ----------
            engine : {str}
                Name of engine to use
            
            temperature : {float}
                Value between 0 and 1 representing the randomness of the model output.
            
            num_tokens : {int}
                Number of tokens returned by the model
        """
        # get key and instantiate openai key
        self.api_key = get_openai_key()
        openai.api_key = self.api_key

        # set query parameters
        self.engine = \
            kwargs['engine'] if 'engine' in kwargs else 'davinci-msft'
        self.temperature = \
            kwargs['temperature'] if 'temperature' in kwargs else 0.5
        self.num_tokens = \
            kwargs['num_tokens'] if 'num_tokens' in kwargs else 100
        self.stop_seq = \
            kwargs['stop_sequence'] if 'stop_sequence' in kwargs else '\nQuery:'

        # initialize prompt
        self._initialize_prompt()

        # initialize postgres cursor
        self.cursor = Cursor()

    def _initialize_prompt(self):
        """
            Private method for initializing prompt.
            Not used for testing.

            Parameters
            ----------
        """
        self.prompt = default_prompt
    
    def _build_test_prompt(self):
        """
            Private method for building test prompt.

            Parameters
            ----------
        """

        self.prompt = "Once upon a time"

    def build_prompt(self, input):
        """
            Public method for building the prompt used to query the API.

            Parameters
            ----------
            input : {dict}
                Dict containing information about the user and their query input
            
            Input Dict Properties
            ---------------------
            user_id : {str}
                Unique identifier for user
            
            text : {str}
                String representation of text input used for prompt
        """
        if not isinstance(input, dict) or len(input) == 0:
            return False

        user_id = input['user_id']

        text = input['text']

        added_prompt = f"\nQuery: {text}"
        added_prompt += "\nResult:"
        added_prompt += "\n"
        

        # query for existing examples from user
        sql_query = f"""
            SELECT snippet_id FROM user_snippet WHERE user_id = '{user_id}'
        """
        
        snippet_list = self.cursor.fetch_dict(sql_query)

        if len(snippet_list) == 0:
            # no previously generated examples from user
            self.prompt += added_prompt
            return True
        
        # use existing examples and further build the prompt
        sql_query = f"""
            SELECT snippet.query, snippet.generated_snippet
            FROM snippet
            INNER JOIN on snippet.snippet_id = user_snippet.snippet_id
            WHERE user_snippet.user_id = '{user_id}'
        """

        example_list = self.cursor.fetch_dict(sql_query)
        
        if len(example_list) >= 5:
            # use the user-examples as the only ones for the final prompt
            self.prompt = ""

        for example in example_list:
            prompt_append = f"\nQuery: {example['query']}"
            prompt_append += '\nResult:'
            prompt_append += f"\n{example['generated_snippet']}"
            
            self.prompt.append(prompt_append)
        
        self.prompt += added_prompt

        return True

    def query(self, testing=False):
        """
            Public method for querying OpenAI API.

            Parameters
            ----------
            testing : {boolean}
                Flag to specify whether in testing phase
        """
        if testing:
            self._build_test_prompt()
        
        res = openai.Completion.create(
            engine=self.engine,
            prompt=self.prompt,
            temperature=self.temperature,
            max_tokens=self.num_tokens,
            stop=self.stop_seq
        )

        res_dict = res.to_dict()

        # check if choices returned, return top choice
        if 'choices' not in res_dict or len(res_dict['choices']) == 0:
            return None
        
        return res_dict['choices'][0]['text']
    