from urllib.request import urljoin
from bs4 import BeautifulSoup
import requests
from urllib.request import urlparse


# Taking user input for goal node, depth, branching factor
goalNode = input("Enter URL: ")
depth = int(input("Enter Depth: "))
branching_factor = int(input("Enter Branching Factor: "))
count = 0

# Creating a set for accessing internal domains
internalDomains = set()

# Creating a set for accessing external domains
externalDomains = set()


# Method for crawling a url at next level
def depthCrawler(goalNode):
    for_temp = set()
    currentURL = urlparse(goalNode).netloc

    # Creates beautiful soup object to extract html tags
    beautiful_soup_object = BeautifulSoup(
        requests.get(goalNode).content, "lxml")

    # Access all anchor tags from input url page and divide them into internal
    # and external domains
    for a in beautiful_soup_object.findAll("a"):
        href = a.attrs.get("href")
        if(href != "" or href != None):
            href = urljoin(goalNode, href)
            href_parsed = urlparse(href)
            href = href_parsed.scheme
            href += "://"
            href += href_parsed.netloc
            href += href_parsed.path
            finalParsedhref = urlparse(href)
            valid = bool(finalParsedhref.scheme) and bool(
                finalParsedhref.netloc)
            if valid:
                if currentURL not in href and href not in externalDomains:
                    print("External -> {}".format(href))
                    externalDomains.add(href)
                if currentURL in href and href not in internalDomains:
                    print("Internal -> {}".format(href))
                    internalDomains.add(href)
                    for_temp.add(href)
    return for_temp


if(depth == 0):
    print("Internal -> {}".format(goalNode))

elif(depth == 1):
    depthCrawler(goalNode)

else:
    # BFS Implementation
    queueBFS = []
    queueBFS.append(goalNode)
    for j in range(depth):
        for count in range(len(queueBFS)):
            url = queueBFS.pop(0)
            urls = depthCrawler(url)
            for i in urls:
                queueBFS.append(i)
                count = count + 1
                if count == branching_factor:
                    break
