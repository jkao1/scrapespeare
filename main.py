from bs4 import BeautifulSoup
import urllib2
import sys

url = "http://nfs.sparknotes.com/henryv/"
filename = "nofear.html"
start = int(sys.argv[1])
end = int(sys.argv[2])

output = """
<style>
tr, td, table {
  border: 1px solid #000;
  padding: 5px
}
td.noFear-left { width:50%; }
</style>
"""

for i in range(start/2, (end+2)/2):        
    sceneUrl = url + "page_" + str(i*2) + ".html"
    print("analyzing the contents of %s" % (sceneUrl))
    content = urllib2.urlopen(sceneUrl).read()
    soup = BeautifulSoup(content, "html.parser")
    output += str(soup.find(id="noFear-comparison").table) + "\n"

file = open(filename, "w")
file.write(output)
file.close()
print("output written to %s" % (filename))
