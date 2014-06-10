fin = open("Better DS3.exe", 'rb')
'''
import base64
 
with open("image.jpg", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())'''
char = []

dict = {}
c = 'a'


while 1:
    c = fin.read(1)
    if c == '': break
    char.append(ord(c))
   

for i in range(0, len(char)-1):
  dict.update({(char[i], char[i+1]):1})

for i in range(0,len(char)-1):
  dict.update({(char[i], char[i+1]):dict[(char[i], char[i+1])]+1})
  
  
data = []
data = dict.keys()

#print char
import math
import csv
writer = csv.writer(open("2tuple.csv", 'wb'))
writer.writerow(["x", "y", "hits"])

for x,y in data:
   writer.writerow([x, y, dict[x,y]])

