"""
Flask Server
"""

from flask import Flask
# from flask_restful import Api
# from dotenv import load_dotenv
from argparse import ArgumentParser
# from flask_cors import CORS

# parse command line arguments
parser = ArgumentParser()
parser.add_argument("--host", help="Serve the host ip", required=False)

args = parser.parse_args()

# load environment variables
# load_dotenv()

# init flask app
app = Flask(__name__)
# CORS(app)

@app.get("/")
def dothigns():
    return "HELLO WORLD"

if __name__ == "__main__":
    if args.host:
        app.run(debug=False, host=args.host)
    else:
        app.run(debug=False, host="127.0.0.1")
