from distorm3 import Decode, Decode16Bits, Decode32Bits, Decode64Bits
l = Decode(0xA30, open("C:\Users\u1\Desktop\Better DS3.exe", "rb").read(), Decode32Bits)
dict = {}
data = []
for i in l:
# print "0x%08x (%02x) %-20s %s" %(i[0],  i[1],  i[3],  i[2])
  data.append(i[2].split(' ')[0])
#  dict.update({data:0})    #adds all possible keys to dictionary and assigns 0

#print data
data.sort()
print data[0:23]
for i in data:
  dict.update({i:0})

for i in data:
  dict.update({i:(dict[i]+1)})    #updates key as they are found

#print dict
import math
import csv
writer = csv.writer(open('C:\Users\u1\Documents\NetBeansProjects\HTML5Application\public_html\data.csv', 'wb'))
writer.writerow(["op", "value"])
list = sorted(dict.items(), key=lambda val:val[0])
list = list[::]
for key, value in list:
   writer.writerow([key, round(math.log10(value),4)])
