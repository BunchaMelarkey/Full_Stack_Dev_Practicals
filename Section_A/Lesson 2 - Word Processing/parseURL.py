link = "http://www.example.com?p1=10&p2=20&p3=30"

# Grabs the host address from an input URL
def getHost(link):
    split_url = link.split("?")
    host_https = split_url[0]
    host = host_https.split("//") 
    x = host[1]

    return x

print("Host is: " + getHost(link))

def getNames():
    split_url = link.split("?")
    value_https = split_url[1].split("&")

    for i in value_https:
        values = i.split("=")
        print("Name is: " + values[0] + ", Value is: " + values[1])

getNames()