import urllib.request as urllib

URL = "http://www.phys.uconn.edu/~gibson/Notes/Section{0}_{1}/Sec{0}_{1}.htm"

for chapter in range(0, 10):
    for section in range(0, 10):
        try:
            page = urllib.urlopen(URL.format(chapter, section)).read()
            with open("{0}_{1}.html".format(chapter,section), "wb") as f:
                f.write(page)
        except Exception as e:
            print(e)
        
