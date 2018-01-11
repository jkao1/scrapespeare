from bs4 import BeautifulSoup
import urllib2, webbrowser
import sys

book_to_end = {
    'henryv': 4,
    'muchado': 238,
    'twelfthnight': 242,
    'lear': 310
}

def scrape_book(book_slug):
    url = "http://nfs.sparknotes.com/%s/" % book_slug
    output = """
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<style>
div {
  font-size: 20px;
}
tr, td, table {
  border: 1px solid #000;
  padding: 5px
}
td.noFear-left { width:50%; }
</style>
    """
    for i in range(1, (book_to_end[book_slug]+2)/2):
        sceneUrl = url + "page_" + str(i*2) + ".html"
        print("analyzing the contents of %s" % (sceneUrl))
        content = urllib2.urlopen(sceneUrl).read()
        soup = BeautifulSoup(content, "html.parser")
        output += str(soup.find(id="noFear-comparison").table) + "\n"

    file = open(book_slug + '.html', "w")
    file.write(output)
    file.close()
    webbrowser.open('file:///Users/jasonkao/cs_projects/scrapespeare/%s.html' % book_slug)

if __name__ == '__main__':
    for book_slug in book_to_end:
        scrape_book(book_slug)

