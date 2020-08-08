# hit submit query endpoint and pass user prompt
echo "Query: A loop from 1 to 5 that prints out hello for every other iteration"
curl --data '{"user_id": "3ajasd343", "query": "A loop from 1 to 5 that prints out hello for every other iteration"}' -X POST -H "Content-Type: application/json" http://localhost:5000/submit_query

# be specific about the type of loop that we want
echo "Query: A while loop that prints test 5 times"
curl --data '{"user_id": "3ajasd343", "query": "A while loop that prints test every other iteration 5 times"}' -X POST -H "Content-Type: application/json" http://localhost:5000/submit_query

# basic data structures
echo "Query: A set with 3 string items"
curl --data '{"user_id": "3ajasd343", "query": "A set with 3 string items"}' -X POST -H "Content-Type: application/json" http://localhost:5000/submit_query

echo "Query: A list with 3 integers"
curl --data '{"user_id": "3ajasd343", "query": "A list with 3 integers"}' -X POST -H "Content-Type: application/json" http://localhost:5000/submit_query

echo "Query: A nested dict with 2 keys"
curl --data '{"user_id": "3ajasd343", "query": "A nested dict with 2 keys"}' -X POST -H "Content-Type: application/json" http://localhost:5000/submit_query

# class snippets
echo "Query: A Pet class with a function called adopt"
curl --data '{"user_id": "3ajasd343", "query": "A Pet class with a function called adopt"}' -X POST -H "Content-Type: application/json" http://localhost:5000/submit_query

# test context outside of Python
echo "Query: A list with 3 fruits"
curl --data '{"user_id": "3ajasd343", "query": "A list with 3 fruits"}' -X POST -H "Content-Type: application/json" http://localhost:5000/submit_query