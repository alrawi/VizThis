import os
filename = 'file.mp4'
fin = open(filename, 'rb')
check = os.stat(filename).st_size

slide = 3
points = 15000000000
x=y=z=0
char = []

dict = {}
c = 'a'

i = 0
while 1:
    c = fin.read(1)
    if c == '': break
    char.append(ord(c))

print len(char)
for i in xrange(0, len(char)-2, slide):
  dict.update({(char[i], char[i+1], char[i+2]):0})

for i in range(0,len(char)-2,slide):
  dict.update({(char[i], char[i+1], char[i+2]):dict[(char[i], char[i+1],char[i+2])]+1})

print len(dict)

num = int(len(dict)/points)+1
print num

avg = {} #NEW DICTIONARY WITH AVERAGES

import numpy
arr = dict.keys()

if(num <= 1):
   avg = dict

else:
 for i in xrange(0,len(dict),num):
   ctr =[0,0,0,0]
   for j in range(0, num):
     if i+j >= len(dict)-1 : break
     for k in range(0,3):
       ctr[k] = ctr[k]+arr[i+j][k]
       
     ctr[3] = ctr[3]+dict[arr[i+j]]
   for k in range(0,4):
       ctr[k] = ctr[k]/num
   avg.update({(ctr[0],ctr[1], ctr[2]) : ctr[3]})
   

data = []
data = avg.keys()
i = 0
import math
import csv
writer = csv.writer(open("3tuple.csv", 'wb'))
writer.writerow(["x", "y","z", "hits"])

for x,y,z in data:
   writer.writerow([x, y, z, avg[x,y,z]])
   i+=1

print i

