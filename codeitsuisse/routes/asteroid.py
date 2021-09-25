import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/asteroid', methods=['POST'])
def evaluateas():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputvalue = data.get("test_cases")
    result = []
    for j in inputvalue:
        a = j
        i = 0
        score = 0
        forigin = 0
        for i in range(len(a)):
            if i != 0 and i!= (len(a)-1):
                origin = i
                if a[i] == a[i-1] == a[i+1]:
                    lcurrent = a[i]
                    rcurrent = a[i]
                    current = a[i]
                    current_c = 1
                    fscore = 0
                    sscore = 0
                    for k in range(1,len(a)):
                        if (i-k) >= 0:
                            if a[i-k] == lcurrent:
                                current_c += 1
                                if current_c >= 7:
                                    sscore += 1.5
                                elif current_c >= 10:
                                    sscore += 2
                                else:
                                    sscore += 1
                            else:
                                lcurrent = a[i-k]
                                if (lcurrent != current)or(rcurrent != current):
                                    current = lcurrent
                                    current_c = 1
                                    fscore += sscore
                                    fscore += 1
                                    sscore = 0
                        if (i+k) < len(a):
                            if a[i+k] == rcurrent:
                                current_c += 1
                                if current_c >= 7:
                                    sscore += 1.5
                                elif current_c >= 10:
                                    sscore += 2
                                else:
                                    sscore += 1
                            else:
                                rcurrent = a[i+k]
                                if (lcurrent != current)or(rcurrent != current):
                                    current = rcurrent
                                    current_c = 1
                                    fscore += sscore
                                    fscore += 1
                                    sscore = 0
                    fscore += sscore
                    if fscore > score:
                        score = fscore
                        forigin = origin
                else:
                    if 1>score:
                        score = 1
            else:
                if 1>score:
                    score = 1  
        dict = {"input": j,"score": score,"origin": forigin}
        result.append(dict)
    logging.info("My result :{}".format(result))
    return json.dumps(result)


