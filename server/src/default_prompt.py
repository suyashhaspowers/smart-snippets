# primary training example
default_prompt = """Query: A list from 1 to 10 with only even numbers.
l = [num for num in range(1,11) if num % 2 == 0]

Query: A dict with cat and dog keys and examples as values.
d = {'cat': ['persian', 'siamese'], 'dog': ['labrador', 'poodle']}

Query: A loop that goes from 1 to 10 and prints out hello each time.
for i in range(1,11):
\tprint('hello')
"""

# basic data types
basic_data_types_prompt = """Query: A string
s = 'abcd'

Query: A list
l = [1,2]

Query: A set
s = set([1,2,3])

Query: A class
class Foo:
\tdef __init__(self):
\t\tprint("class")

Query: A dict
d = {'x': 'y'}
"""

basic_control_flow_prompt = """Query: An if/else block
if x:
\tprint("if")
else:
\tprint("else")

Query: A for loop
for idx in range(x, y):
\tprint("for loop")

Query: A while loop
x = 0
while (x < y):
\tprint("while")

Query: A function
def func(x,y):
\treturn
"""

data_type_control_flow_prompt = basic_data_types_prompt + "\n" + basic_control_flow_prompt