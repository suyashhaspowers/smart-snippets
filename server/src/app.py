from flask import Flask, request, make_response, jsonify

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
    return "query submitted"

@app.route("/submit_reviewed_snippet", methods=['POST'])
def submit_reviewed_snippet():
    return "reviewed snippet submitted"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
