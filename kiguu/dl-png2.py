import urllib.request
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"
mem = urllib.request.urlopen(url).read()
f = open(savename,mode = "wb")
f.write(mem)
print("保存しました")
f.close()