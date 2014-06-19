import pymongo, hashlib
from pymongo import MongoClient
client = MongoClient()

def decode(datas, hash):
	tt = []
        dict = {}	
	data = datas
        client = MongoClient()
   	db = client.local
        collection = db.vizdata
        
        print len(data) 
        for dat in collection.find():
         print "Finding.." 
         if dat['hash'] == hash:
	      print "FILE ALREADY EXISTS"
 	      exit()
 
	print "DECODING TWOTUPLE DATA... " 				#TWO TUPLE

        i = 0
	for c in data:
	  tt.append(ord(c))

	threetup = tt
	for i in range(0, len(tt)-1):
	  dict.update({(tt[i], tt[i+1]):1})

	for i in range(0,len(tt)-1):
	  dict.update({(tt[i], tt[i+1]):dict[(tt[i], tt[i+1])]+1})
  
	tt = []
        
        for x,y in dict:
          tt.append((x,y,dict[x,y]))
 	
        
        dict = {} 
 
        print "Decoding histogram Data..."        			#HISTOGRAM
 	
 	hist = []
	import distorm3
	from distorm3 import Decode, Decode16Bits, Decode32Bits, Decode64Bits
	l = Decode(0xA30, data, Decode32Bits)

	for i in l:
	   hist.append(i[2].split(' ')[0])

	for i in hist:
          dict.update({i:0})
	
	for i in hist:
	  dict.update({i:(dict[i]+1)})

        import math
	hist = sorted(dict.items(), key=lambda val:val[0])
 	hist = hist[::]

 	print "Decoding Three Tuple Data...."				#THREE TUPLE	
	slide = 3
	points = 15000000000
	x=y=z=0
	dict = {}

	for i in xrange(0, len(data)-2, slide):
	  dict.update({(threetup[i], threetup[i+1], threetup[i+2]):0})

	for i in range(0,len(data)-2,slide):
	  dict.update({(threetup[i], threetup[i+1], threetup[i+2]):dict[(threetup[i], threetup[i+1],threetup[i+2])]+1})


	num = int(len(dict)/points)+1

	import numpy
	arr = dict.keys()
	threetup = []
	if(num <= 1):
	   for x,y,z in dict:
	     threetup.append((x,y,z,dict[(x,y,z)]))
	
	else:
	 for i in xrange(0,len(dict),num):	
	   ctr =[0,0,0,0]
	   for j in range(0, num):			#SMALLER BLOCK OF DATA TO BE AVERAGED
	     if i+j >= len(dict)-1 : break		
	     for k in range(0,3):
	       ctr[k] = ctr[k]+arr[i+j][k]
	       
	     ctr[3] = ctr[3]+dict[arr[i+j]]
	   for k in range(0,4):
	       ctr[k] = ctr[k]/num
	   threetup.append((ctr[0],ctr[1], ctr[2],ctr[3]))
	   
	print threetup[0:40]
	print "Decoding ContactMap..."			#CONTACT MAP DECODE
	list = []

	points = 225 					#NO. OF POINTS ON CONTACT MAP
        check = len(data)

	size =  check/points
	for c in data:
	    b = ord(c)
	    b = float(b)
	    if b < 0 : b = b+256
	    list.append(b)

	strings = []
	for i in range(0, (len(list)/size)+1):
	    strings.append(list[size*i : (size*i)+size])
	
	if len(strings[len(strings)-1]) < size :
	     for i in range(0, size-len(strings[len(strings)-1])):
	           strings[len(strings)-1].append(0)

    

	import numpy
	import scipy
	import scipy.spatial
	import math 
	val = [0,0,0]
	length = len(strings)
	cont = []
	print length
	i = j = 0
	for i in xrange(0,length):
	    t1 = strings[i]
	    for j in range(0,length):
	      t2 = strings[j]	
	      val[0] = 100*scipy.spatial.distance.braycurtis(t1, t2)
	      #val[0] = (100*scipy.spatial.distance.jaccard(strings[i], strings[j]))
	      #val[0] = (scipy.spatial.distance.sqeuclidean(strings[i], strings[j]))
	      #for k in range(0,2):
	      if math.isnan(val[0]) or (val[0] <= 10): val[0] = 0
	      else : cont.append((i, j,val[0]))#, val[1], val[2]])
	    if  i%100 == 0 : 
		print i 
		
	print len(cont)
	print cont[0:10]
	import json,zlib,base64
	print "COmpressing data..."				#DATA COMPRESSION
	
	hist = json.dumps(hist)
	hist = zlib.compress(hist)

	tt = json.dumps(tt)
	tt = zlib.compress(tt)

	threetup = json.dumps(threetup)
	threetup = zlib.compress(threetup)

	cont = json.dumps(cont)
	cont = zlib.compress(cont)
	
	hist = base64.b64encode(hist)
	tt = base64.b64encode(tt) 
	threetup = base64.b64encode(threetup)
	cont = 	base64.b64encode(cont)
	
	dict = {"hash" : hash, "hist" : hist, "tt" : tt ,"threetup" : threetup, "cont":cont}
    	tt = threetup = hist = cont = []	
        print "Inserting..."
	collection.insert(dict)
	print "Database Created"
