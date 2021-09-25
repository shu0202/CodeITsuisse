import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/parasite', methods=['POST'])
def evaluateparasite():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = []
    for x in data:
        result_dict = {}
        room_no = x["room"]
        grid = x["grid"]
        interested_ind = x["interestedIndividuals"]
        p1={}
        p2=0
        p3=0
        p4=0
        temp_row = 0
        temp_col = 0
        result_dict["room"] = room_no
        tick_list = [0]
        for i in interested_ind:
            tick = 0
            if grid[int(i[0])][int(i[-1])] == 0 or 2:
                p1[i] = -1
            elif grid[int(i[0])][int(i[-1])] == 3:
                p1[i] = 0
            elif grid[int(i[0])][int(i[-1])] == 1:
                if grid[int(i[0])][int(i[-1])] == 1:
                    temp_row = int(i[0])
                    temp_col = int(i[-1])
                    while True:
                        if temp_row == 0:
                            if grid[temp_row+1][temp_col] == 3:
                                tick += 1
                                p1[i] = tick
                                break
                            elif grid[temp_row+1][temp_col] == 1:
                                tick += 1
                                temp_row += 1
                                continue
                        elif temp_row == len(grid)-1:
                            if grid[temp_row-1][temp_col] == 3:
                                tick += 1
                                p1[i] = tick
                                break
                            elif grid[temp_row-1][temp_col] == 1:
                                tick += 1
                                temp_row -= 1
                                continue
                        else:
                            if grid[temp_row+1][temp_col] == 3:
                                tick += 1
                                p1[i] = tick
                                break
                            elif grid[temp_row+1][temp_col] == 1:
                                tick += 1
                                temp_row += 1
                                continue
                            if grid[temp_row-1][temp_col] == 3:
                                tick += 1
                                p1[i] = tick
                                break
                            elif grid[temp_row-1][temp_col] == 1:
                                tick += 1
                                temp_row -= 1
                                continue
                        if temp_col == 0:
                            if grid[temp_row][temp_col+1] == 3:
                                tick += 1
                                p1[i] = tick
                                break
                            elif grid[temp_row][temp_col+1] == 1:
                                tick += 1
                                temp_col += 1
                                continue
                        elif temp_col == len(grid[temp_row])-1:
                            if grid[temp_row][temp_col-1] == 3:
                                tick += 1
                                p1[i] = tick
                                break
                            elif grid[temp_row][temp_col-1] == 1:
                                tick += 1
                                temp_col -= 1
                                continue
                        else:
                            if grid[temp_row][temp_col+1] == 3:
                                tick += 1
                                p1[i] = tick
                                break
                            elif grid[temp_row][temp_col+1] == 1:
                                tick += 1
                                temp_col += 1
                                continue
                            if grid[temp_row][temp_col-1] == 3:
                                tick += 1
                                p1[i] = tick
                                break
                            elif grid[temp_row][temp_col-1] == 1:
                                tick += 1
                                temp_col -= 1
                                continue
                        p1[i] = -1
                        break
                    else:
                        tick_list.append(tick)
        result_dict["p1"] = p1
        for ind in p1:
            if p1[ind] == -1:
                p2 = -1
            else:   
                p2 = max(tick_list)
        result_dict["p2"] = p2
        result_dict["p3"] = p3
        result_dict["p4"] = p4
        result.append(result_dict)                   
    return json.dumps(result)