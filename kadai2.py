# -*- coding: utf-8 -*-

from common import generate_data
from statistics_s import SG, ST

import matplotlib.pyplot as plt

n1 = 3
n2 = 3
x_num = 1000

(x_data, y_data, x11_num) = generate_data(n1, n2, x_num, y_sigma=1)


fpr_list = []
cdr_list = []

threshold_list = [i * 0.01 for i in range(0, 101)]
for threshold in threshold_list:
    fpr_count = 0
    cdr_count = 0
    for data in zip(x_data, y_data):
        result = SG(data[1], threshold, n1, n2, y_sigma=1)

        if data[0] == (1,1) and result == 1: 
            cdr_count += 1
   
        if data[0] != (1,1) and result == 1:
            fpr_count += 1

    fpr_list.append(fpr_count/(x_num-x11_num))
    cdr_list.append(cdr_count/x11_num)

plt.plot(fpr_list, cdr_list)

plt.show()
