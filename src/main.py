from os import path
from AI import AI
from flask import Flask, jsonify, request


app = Flask(__name__)

ai = AI("questions-2114")


@app.route("/<s>")
def mainPage(s: str):
    result = ai.askAI(s)
    return jsonify(result)


# if __name__ == "__main__":
#     ai = AI("questions-2114")
#
#     print(ai.askAI("how do I creat an array"))
