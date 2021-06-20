from flask import Flask
from flask import json
import logging


app = Flask(__name__)

@app.route('/status')
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    #Log line
    app.logger.info("Status endpoint was reached")

    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    app.logger.info("Metrics endpoint was reached") 
    return response

@app.route("/")
def hello():
    app.logger.info("Main endpoint was reached") 
    return "Hello World!"

if __name__ == "__main__":

    logging.basicConfig(filename='app.log',format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
    app.run(host='0.0.0.0')
