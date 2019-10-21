from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import sys
def crawl(url, depth, maxDepth, visited):
    depthTab = "\t"
    for t in range(depth - 1):
        depthTab += depthTab

    print(depthTab + url)
    if url in visited:
        return
    if depth >= maxDepth:
        return
    visited.append(url)
    try:
        urls = findLinks(url)
        if urls:
            for u in urls:
                absUrl = (makeAbs(u, url))
                crawl(absUrl, depth + 1, maxDepth, visited)


    except Exception as e:
        print(f"Failed to get {url} because {e}")

def makeAbs(url, parentUrl):
    parsed = urlparse(url)

    if parsed.scheme == "" and parsed.netloc == "":
        return parentUrl + url
    else:
        return url

def findLinks(url):
    html = requests.get(url).text
    urls = []
    try:
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a')
        if links:
            # print("URLs linked in this document are:")
            for a in links:
                urls.append(f"{a.get('href')}")
        # else:
            # print("No hyperlinks were found in this document")
    except Exception as e:
        print(f"An exception occurred: {e}")
    return urls

def isAbs(url):
    parsed = urlparse(url)
    if parsed.scheme == "":
        return False
    else:
        return True
def main():
    if len(sys.argv) < 2:
        print("Error: no URL supplied")
    elif not isAbs(sys.argv[1]):
        print("Error: Invalid URL supplied. \nPlease supply an absolute URL to this program")
    elif len(sys.argv) < 3:
        crawl(sys.argv[1], 0, 3, [])
        print(f"Crawling from {sys.argv[1]} to a maximum distance of 3 links")
    else:
        crawl(sys.argv[1], 0, int(sys.argv[2]), [])
        if sys.argv[2] == 1:
            links = "link"
        else:
            links = "links"
        print(f"Crawling from {sys.argv[1]} to a maximum distance of {sys.argv[2]} {links}")



main()