from flask import Flask, request
import logging
import datetime
import json

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a custom log handler that outputs logs in JSON format
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            'timestamp': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'message': record.getMessage(),
            'name': record.name,
        }
        return json.dumps(log_data)

# Set the custom JSON formatter for the logger
json_handler = logging.StreamHandler()
json_handler.setFormatter(JsonFormatter())
logger.addHandler(json_handler)

@app.route('/')
def endpoint():
    # Get the query string parameters from the request
    query_params = request.args

    # Print the query string parameters to the log in JSON format
    for key, value in query_params.items():
        logging.info({"Key": key, "Value": value})

    return "Query parameters logged in JSON format."

@app.route('/health')
def health():
    # kubernetes health check
    try:
        return json.dumps({"status": "ok"}), 200
    except Exception as e:
        return json.dumps({"status": "error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)