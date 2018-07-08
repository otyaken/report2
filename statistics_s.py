# -*- coding: utf-8 -*-
import math

def SG(y, threshold, n1, n2, y_sigma):
    x_info = [((0,0), 0.6), ((0,1), 0.1), ((1,0),0.1), ((1,1), 0.2)]

    y1_data = y[0:n1]
    y2_data = y[n1:n1+n2]

    #p(x11)の確率
    p_x11 = x_info[3][1]

    p_sum = 0

    for x in x_info:
        x1 = x[0][0]
        x2 = x[0][1]
        exp_sum = 0

        for y1 in y1_data:
            exp_sum += (1 - 2*y1 + 2*y1*x1 - x1**2) / (2 * y_sigma * y_sigma)

        for y2 in y2_data:
            exp_sum += (1 - 2*y2 + 2*y2*x2 - x2**2) / (2 * y_sigma * y_sigma)
        
        p_sum += x[1] * math.exp(exp_sum)

    ans = p_sum / p_x11

    # (1,1)である
    if 1/ans >= threshold:
        return 1
    # (1,1)でない
    else:
        return 0

    

def ST(y, threshold, n1, n2, y_sigma):
    x_info = [((0,0), 0.6), ((0,1), 0.1), ((1,0),0.1), ((1,1), 0.2)]
    y1_data = y[0:n1]
    y2_data = y[n1:n2]
    
    #p(x00)の確率
    p_x00 = x_info[0][1]
    #p(x11)の確率
    p_x11 = x_info[3][1]

    exp_sum = 0

    for y1 in y1_data:
        exp_sum += (1 - 2*y1) / (2 * y_sigma * y_sigma)

    for y2 in y2_data:
        exp_sum += (1 - 2*y2) / (2 * y_sigma * y_sigma)

    ans = 1 + (p_x00 / p_x11) * math.exp(exp_sum)

    # (1,1)である
    if 1/ans >= threshold:
        return 1
    # (1,1)でない
    else:
        return 0

    


