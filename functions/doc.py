import os

def get_quant(userid, data):
    userid = str(userid)
    max_quant = -1
    for i in data:
        id = i[:i.index('_')]
        if id == userid:
            index_first = i.index('_')
            index_last = i.index(".")
            quant = int(i[index_first + 1:index_last])
            if max_quant < quant:
                max_quant = quant

    return max_quant
