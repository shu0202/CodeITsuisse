import logging
import json
import random

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def fixedrace():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    swimmer_list = data.split(",")
    result = random.shuffle(swimmer_list)
    return json.dumps(result)



