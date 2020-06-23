from urllib.request import urlopen
content = urlopen('https://github.com/login')
URL = content.read()
print(str(URL, 'utf-8'))
