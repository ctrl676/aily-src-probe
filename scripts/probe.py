import urllib.request
print(urllib.request.urlopen('https://example.com/', timeout=12).read()[:400])
