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
    y2_data = y[n1:n1+n2]
    
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


def SP1_2(y, threshold, n1, n2, y_sigma):
    x_info = [((0,0), 0.6), ((0,1), 0.1), ((1,0),0.1), ((1,1), 0.2)]

    y1_data = y[0:n1]
    y2_data = y[n1:n1+n2]
    
    #p(x1=1)の確率
    p_x1 = 0
    for x in x_info:
        if x[0][0] == 1:
            p_x1 += x[1]

    #p(x1=0)の確率
    p_x0 = 0
    for x in x_info:
        if x[0][0] == 0:
            p_x0 += x[1]

    #p(x10)の確率
    p_x10 = x_info[2][1]
    #p(x11)の確率
    p_x11 = x_info[3][1]

    p_sum = 0
    
    for y1 in y1_data:
        p_sum += (1 - 2*y1) / (2 * y_sigma * y_sigma)

    ans_first = 1 + (p_x0 / p_x1) * math.exp(p_sum)

    if 1 / ans_first < threshold:
        #(1,1)でない
        return 0
    
    p_sum = 0

    for y2 in y2_data:
        p_sum += (1 - 2*y2) / (2 * y_sigma * y_sigma)

    ans_second = 1 + (p_x10 / p_x11) * math.exp(p_sum)
    
    if (1 / ans_first) * (1 / ans_second) >= threshold:
        #(1,1)である
        return 1
    else:
        #(1,1)でない
        return 0


def SP2_1(y, threshold, n1, n2, y_sigma):
    x_info = [((0,0), 0.6), ((0,1), 0.1), ((1,0),0.1), ((1,1), 0.2)]

    y1_data = y[0:n1]
    y2_data = y[n1:n1+n2]
 
    #p(x1=1)の確率
    p_x1 = 0
    for x in x_info:
        if x[0][0] == 1:
            p_x1 += x[1]

    #p(x1=0)の確率
    p_x0 = 0
    for x in x_info:
        if x[0][0] == 0:
            p_x0 += x[1]

    #p(x2=0)の確率
    p_x2_0 = 0
    for x in x_info:
        if x[0][1] == 0:
            p_x2_0 += x[1]

    #p(x2=1)の確率
    p_x2_1 = 0
    for x in x_info:
        if x[0][1] == 1:
            p_x2_1 += x[1]


    #p(x10)の確率
    p_x10 = x_info[2][1]
    #p(x01)の確率
    p_x01 = x_info[1][1]
    #p(x11)の確率
    p_x11 = x_info[3][1]


    p_sum = 0
    for y2 in y2_data:
        p_sum += (1 - 2*y2) / (2 * y_sigma * y_sigma)
    #Pr(X2=1, | y2)
    ans_first = 1 + (p_x2_0 / p_x2_1) * math.exp(p_sum)

    if 1 / ans_first < threshold:
        #(1,1)でない
        return 0
    
    p_sum = 0
    for y1 in y1_data:
        p_sum += (1 - 2*y1) / (2 * y_sigma * y_sigma)

    ans_second = 1 + (p_x01 / p_x11) * math.exp(p_sum)
    
    if (1 / ans_first) * (1 / ans_second) >= threshold:
        #(1,1)である
        return 1
    else:
        #(1,1)でない
        return 0

def SS(y, threshold, n1, n2, y_sigma):
    x_info = [((0,0), 0.6), ((0,1), 0.1), ((1,0),0.1), ((1,1), 0.2)]
    y1_data = y[0:n1]
    y2_data = y[n1:n1+n2]

    #p(x1=1)の確率
    p_x1 = 0
    for x in x_info:
        if x[0][0] == 1:
            p_x1 += x[1]

    #p(x1=0)の確率
    p_x0 = 0
    for x in x_info:
        if x[0][0] == 0:
            p_x0 += x[1]

    #p(x2=0)の確率
    p_x2_0 = 0
    for x in x_info:
        if x[0][1] == 0:
            p_x2_0 += x[1]

    #p(x2=1)の確率
    p_x2_1 = 0
    for x in x_info:
        if x[0][1] == 1:
            p_x2_1 += x[1]


    #p(x10)の確率
    p_x10 = x_info[2][1]
    #p(x01)の確率
    p_x01 = x_info[1][1]
    #p(x11)の確率
    p_x11 = x_info[3][1]

    p_sum = 0
    for y1 in y1_data:
        p_sum += (1 - 2*y1) / (2 * y_sigma * y_sigma)

    ans_first = 1 + (p_x0 / p_x1) * math.exp(p_sum)
    
    #Pr(X1=1 | y1)
    a = 1 / ans_first


    p_sum = 0
    for y2 in y2_data:
        p_sum += (1 - 2*y2) / (2 * y_sigma * y_sigma)
    #Pr(X2=1, | y2)
    ans_second = 1 + (p_x2_0 / p_x2_1) * math.exp(p_sum)
    b = 1 / ans_second



    if a > b:
        return SP1_2(y, threshold, n1, n2, y_sigma)

    else:
        return SP2_1(y, threshold, n1, n2, y_sigma)
