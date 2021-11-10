import csv
import os
print(os.getcwd())
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

def ayir(string):
    string = string.replace('\n',"")
    string = string.replace('\t',"")
    for i in range(15):
        space = " "*i
        string = string.replace(space,"")
    return string

file = open("data.csv")
data = list(csv.reader(file))
header = data[0]
data = data[1:]

for row in data:
    if len(row) != len(header):
        data.remove(row)

length_list = []
width_list = []
e_l_list = []
e_w_list = []
for row in data:
    type_egg = row[0]
    length = float(ayir((row[1])))
    length_list.append(length)
    width = float(ayir((row[2])))
    width_list.append(width)
    e_l = float(ayir((row[3])))
    e_l_list.append(e_l)
    e_w = float(ayir((row[4])))
    e_w_list.append(e_w)
sort_list = []

for i in range(len(length_list)):
    length = length_list[i]
    width = width_list[i]
    e_l = e_l_list[i]
    e_w = e_w_list[i]
    if length < 10:
        length = round(length*10,1)
    elif length > 100:
        length = round(length/10,1)
    if width < 10:
        width = round(width*10,1)
    elif width > 100:
        width = round(width/10,1)
    sort_list.append((length,width,e_l,e_w))
sort_list = sorted(sort_list)

s_l = []
s_w = []
s_el = []
s_ew = []
s_tl = [s_l,s_w,s_el,s_ew]

for i in sort_list:
    s_l.append(i[0])
    s_w.append(i[1])
    s_el.append(i[2])
    s_ew.append(i[3])

print(round((sum(s_l)/len(s_l))/(sum(s_w)/len(s_w)),4))
x = np.array(s_l)
y = np.array(s_w)
print(type(x),type(y))

A = np.vstack([x, np.ones(len(x))]).T
y = y[:, np.newaxis]

pinv = np.linalg.pinv(A)
alpha = pinv.dot(y)
print(alpha)

plt.figure(figsize = (10,8))
plt.plot(x, y, 'b.')
plt.plot(x, alpha[0]*x + alpha[1], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
