import urllib.request

wp = urllib.request.urlopen("http://google.com")
pw = wp.read()
print(pw)