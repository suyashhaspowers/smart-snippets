from flask import Flask, request, make_response, jsonify
from flask import json

from utils import QueryPipeline

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world from smart-snippet server"

@app.route("/test_server")
def test_server():
    return "Smart-snippet server running"

@app.route("/test_openai_engine")
def test_openai_engine():
    qp = QueryPipeline()

    answer = qp.query(testing=True)
    
    response_body = {
        "answer": answer
    }

    return make_response(jsonify(response_body))

@app.route("/submit_query", methods=['POST'])
def submit_query():
    response_body = {}

    if request.method != 'POST' or not request.is_json:
        response_body['message'] = 'Invalid request method or request is not JSON'
        response_body['snippet'] = None

        return make_response(jsonify(response_body))

    req = request.get_json()

    user_id = req.get('user_id')
    user_query = req.get('query')

    input_dict = {
        'user_id': user_id,
        'text': user_query
    }

    qp = QueryPipeline()

    build_prompt = qp.build_prompt(input_dict)

    if not build_prompt:
        response_body['message'] = 'Unable to build prompt.'
        response_body['snippet'] = None

        return make_response(jsonify(response_body))

    print(qp.prompt)

    snippet = qp.query()

    if snippet is None:
        response_body['message'] = 'Query failed. Empty result.'
        response_body['snippet'] = None
    else:
        response_body['message'] = 'Snippet successfully generated!'
        response_body['snippet'] = snippet

    return make_response(jsonify(response_body))

@app.route("/submit_reviewed_snippet", methods=['POST'])
def submit_reviewed_snippet():
    return "reviewed snippet submitted"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
