import time

def time_execution(code):
	start=time.process_time()
	eval(code)
	run_time=time.process_time()-start
	return run_time

def addWordToIndex(index,keyword,url):
	for entry in index:
		if entry[0]==keyword:
			entry[1].append(url)
			return
	index.append([keyword,[url]])	
	
def make_string(listOfLetters):
	str=""
	for e in listOfLetters:
		str=str+e
	return str
			
def make_big_index(index, size):
	letters=['a','a','a','a','a','a','a','a']
	while len(index)<size:
		word=make_string(letters)
		addWordToIndex(index,word,"dummyURL")
		for i in range(len(letters)-1,0,-1):
			if letters[i]<'z':
				letters[i]=chr(ord(letters[i])+1)
				break
			else:
				letters[i]='a'
	return index					

def lookup(keyword, index):
	for e in index:
		if e[0]==keyword:
			return e[1]
index=[]

make_big_index(index,1000)
print("Lookup for index 1000")
print(time_execution("lookup('xxx',index)"))

make_big_index(index,2000)
print("Lookup for index 2000")
print(time_execution("lookup('xxx',index)"))

make_big_index(index,4000)
print("Lookup for index 4000")
print(time_execution("lookup('xxx',index)"))

make_big_index(index,8000)
print("Lookup for index 8000")
print(time_execution("lookup('xxx',index)"))

make_big_index(index,16000)
print("Lookup for index 16000")
print(time_execution("lookup('xxx',index)"))
	
make_big_index(index,32000)
print("Lookup for index 32000")
print(time_execution("lookup('xxx',index)"))	