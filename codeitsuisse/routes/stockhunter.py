import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)
def mklist(en_first,en_second,ta_first,ta_second):
    l = []
    if en_first>ta_first:
        hor = en_first
    else:
        hor = ta_first
    if en_second>ta_second:
        vert = en_second
    else:
        vert = ta_second
    for i in range(vert+1):
        sub_list = []
        for j in range(hor+1):
            sub_list.append(0)
        l.append(sub_list)
    return(l,hor,vert)

@app.route('/stock-hunter', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    dic=data[0]
    gridDepth = dic["gridDepth"]
    gridKey = dic["gridKey"]
    horizontalStepper = dic["horizontalStepper"]
    verticalStepper = dic["verticalStepper"]
    en_first = 0
    en_second = 0
    ta_first = 2
    ta_second = 2
    end_list, first, second= mklist(en_first,en_second,ta_first,ta_second)
    end_list_r = []
    for vert in range(0,second+1):
        for hor in range(0,first+1):
            if vert != 0:
                if hor == 0:
                    end_list[vert][hor]=vert*verticalStepper
                else:
                    if (vert == second) and (hor == first):
                        end_list[vert][hor]=0
                    else:
                        end_list[vert][hor]=end_list[vert-1][hor]*end_list[vert][hor-1]
            else:
                if hor != 0:
                    end_list[vert][hor]=hor*horizontalStepper
                else:
                    end_list[vert][hor]=0

    for i in range(0,second+1):
        sub_list_r =[]
        for j in range(0,first+1):
            j = int(end_list[i][j])
            risk_lv = (j+gridDepth)%gridKey
            risk_s = risk_lv%3
            if risk_s == 0:
                sub_list_r.append("L")
            elif risk_s == 1:
                sub_list_r.append("M")
            elif risk_s == 2:
                sub_list_r.append("S")
        end_list_r.append(sub_list_r)
    return json.dumps(end_list_r)      



