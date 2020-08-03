default_prompt = """Query: A list from 1 to 10 with only even numbers.
Result:
l = [num for num in range(1,11) if num % 2 == 0]

Query: A dict with cat and dog keys and examples as values.
Result:
d = {'cat': ['persian', 'siamese'], 'dog': ['labrador', 'poodle']}

Query: A loop that goes from 1 to 10 and prints out hello each time.
Result:
for i in range(1,11):
\tprint('hello')
"""