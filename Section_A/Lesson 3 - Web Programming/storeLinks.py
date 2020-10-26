import urllib.request
response = urllib.request.urlopen('http://www.bbc.co.uk/news')
html = str(response.read())

links, pos = [], 0
allFound, linksFound = False, 0
while not allFound:
	aTag = html.find("<a href=", pos)
	if aTag > -1:
		href = html.find('"', aTag+1)
		endHref = html.find('"', href+1)
		url = html[href+1:endHref]
		if url[:7] == "http://" or url[:8] == 'https://':
			if url[-1] == "/":
				url = url[:-1]
			links.append(url)     
			print(url)
			linksFound = linksFound+1
		closeTag = html.find("</a>", aTag)
		pos = closeTag+1
	else:
		allFound = True   
print("{} hyperlinks found".format(linksFound))
print(links)