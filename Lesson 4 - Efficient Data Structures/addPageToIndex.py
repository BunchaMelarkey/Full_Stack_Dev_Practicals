import urllib.request
 
def getPageText(url):

	response = urllib.request.urlopen(url)
	html = str(response.read())

	pageText, pageWords = "", []
	html = html[html.find("<body")+5:html.find("</body>")]

	finished = False
	while not finished:
		nextCloseTag = html.find(">")
		nextOpenTag = html.find("<")
		if nextOpenTag > -1:
			content = " ".join(html[nextCloseTag+1:nextOpenTag].strip().split())
			pageText = pageText + " " + content
			html = html[nextOpenTag+1:]
		else:
			finished = True
			
	for word in pageText.split():
		if word[0].isalnum() and word not in pageWords:
			pageWords.append(word)
				
	return pageWords

def addWordToIndex(index, keyword, url):
	for entry in index:
		if entry[0] == keyword:
			entry[1].append(url)
			return
	index.append([keyword, [url]])

def addPageToIndex(index, url):
	pageWords = getPageText(url)
	for word in pageWords:
		addWordToIndex(index, word, url)	

index, pageWords = [], []
url = "http://www.ulster.ac.uk"
addPageToIndex(index, url)		
print(index)