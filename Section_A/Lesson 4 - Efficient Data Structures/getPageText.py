import urllib.request
response = urllib.request.urlopen("http://www.ulster.ac.uk")
html = str(response.read())

pageText, pageWords = "", []
html = html[html.find("<body")+5:html.find("</body>")]

finished = False
while not finished:
	nextCloseTag = html.find(">")
	nextOpenTag = html.find("<")
	if (nextOpenTag > -1):
		content = " ".join(html[nextCloseTag+1:nextOpenTag].strip().split())
		pageText = pageText + " " + content
		html = html[nextOpenTag+1:]
	else:
		finished = True
		
for word in pageText.split():
	if word[0].isalnum() and word not in pageWords:
		pageWords.append(word)
			
print(pageWords)
print("{} unique words found".format(len(pageWords)))