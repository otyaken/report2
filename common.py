# -*- coding: utf-8 -*-

import numpy as np

def generate_data(n1, n2, x_num, y_sigma=1):
    x_data = []
    y_data = []
    #xの生成
    x_info = [("(0,0)", 0.6), ("(0,1)", 0.1), ("(1,0)",0.1), ("(1,1)", 0.2)]
    for i in range(0, x_num):
        p = np.rand()
        p_sum = 0
        n11_num = 0
        for x in x_info:
            p_sum += x[1]
            if p_sum >= p:
                x_data.append(eval(x[0]))
                if x[0] == "(1,1)":
                    n11_num += 1
                break

    for i in range(0, x_num):
        y = []
        #y1の生成
        for k in range(0, n1):
            y.append(np.normal(x_data[0], y_sigma))
        #y2の生成
        for k in range(0, n2):
            y.append(np.normal(x_data[1], y_sigma))

        y_data.append(tuple(y)) 

    return (x_data, y_data, n11_num)


