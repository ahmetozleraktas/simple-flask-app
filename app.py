from flask import Flask, request
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# write log to file 

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# log file path
log_file = '/var/log/app.log'
app = Flask(__name__)


@app.route('/')
def endpoint():
    # Get the query string parameters from the request
    query_params = request.args

    # Print the query string parameters to the console
    logging.info(f"Query parameters: {query_params}")
    for key, value in query_params.items():
        logging.info(f"Key: {key}, Value: {value}")

    return "Query parameters printed to console."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)