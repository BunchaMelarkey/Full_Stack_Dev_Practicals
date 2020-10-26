import urllib.request
bbc = 'http://www.bbc.co.uk/news'
url_inp = input("Please enter a URL to search: ")
response = urllib.request.urlopen(url_inp)
# The data returned here is a byte stream - We convert it to a String
html = str(response.read())

# Check the second half of what the other bits and pieces are involved with in spite of the o hg
pos = 0
allFound, linksFound = False, 0
while not allFound:
	# Find the first denotion of a hyperlink
	aTag = html.find("<a href=", pos)
	if aTag > -1:
		# Here we find rhe inverted commas containing the URL
		href = html.find('"', aTag+1)
		endHref = html.find('"', href+1)
		url = html[href+1:endHref]
		if url.startswith("http://") or url.startswith("https://"):
			if url.endswith('/'):
				url = url[:-1]
			print(url)
			# Below we increment our found links and find the URL's closing tag
			linksFound = linksFound+1
			closeTag = html.find("</a>", aTag)
			pos = closeTag+1
		else:
			pass
	else:
		# We have reached the HTML's endpoint - No more links can be found
		allFound = True   

print("{} hyperlinks found".format(linksFound))