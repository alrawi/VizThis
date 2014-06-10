import os

points = 500
filename = "Better DS3.exe"

check = os.stat(filename).st_size

size =  check/points
fin = open(filename, 'rb')



list = []
c = 'a'

while 1:
    c = fin.read(1)
    
    if not c : break
    b = ord(c)
    if b < 0 : b = b+256
    list.append(b)

fin.close()

strings = []
for i in range(0, (len(list)/size)+1):
    strings.append(list[size*i : (size*i)+size])
   # strings[i] = ''.join(map(str, strings[i]))

if len(strings[len(strings)-1]) < size :
     for i in range(0, size-len(strings[len(strings)-1])):
           strings[len(strings)-1].append(0)

    


import math
import csv
import numpy
import scipy
import scipy.spatial

writer = csv.writer(open("C:\Users\u1\Documents\NetBeansProjects\COntactMap\public_html\map.csv", 'wb'))
writer.writerow(["x", "y", "ham"])#, "jac", "diff" ])

val = [0,0,0]
length = len(strings)

print(len(strings))
i = j = 0
for i in xrange(0,length):
    while j < length:
      val[0] = 100*scipy.spatial.distance.braycurtis(strings[i], strings[j])
      #val[1] = (100*scipy.spatial.distance.jaccard(strings[i], strings[j]))
      #val[0] = (scipy.spatial.distance.sqeuclidean(strings[i], strings[j]))
      for k in range(0,2):
        if math.isnan(val[k]): val[k] = 0;
        else : val[k] = val[k]
      writer.writerow([i, j,val[0]])#, val[1], val[2]])
      j = j+1
    j = 0
    if  i%100 == 0 : print i
   
    
    

