import urllib2
import bs4

class Parser(object):

	def __init__(self):
		web = self.get_web("https://www.packtpub.com/packt/offers/free-learning/")
		self.html_summary = self.parse(web, "dotd-main-book-summary float-left")
		self.html_image = self.parse(web, "dotd-main-book-image float-left")

    # Get webs content.
	def get_web(self, url):
		f = urllib2.urlopen(url)
		web = f.read()
		f.close()
		return web

    # We filter the part of HTML that contains (among other things) the title,
    # summary and important points of the free book of the day.
	def parse(self, html, clas):
		html = bs4.BeautifulSoup(html, "lxml")
		return html.find("div", {"class": clas})

    # Returns book's title.
	def get_title(self):
		title = self.html_summary.find("h2")
		return title.text.lstrip()

    # Returns book's abstract
	def get_abstract(self):
		abstract = self.html_summary.find_all("div")
		return abstract[2].text.lstrip()

    # Returns book's important points
	def get_points(self):
		points = self.html_summary.find_all("li")
		return [u'\u2022' + ' ' + point.text.lstrip() for point in points]

    # Returns book's image
	def get_image(self):
		 return [x['src'] for x in self.html_image.findAll('img')][0][2:]

    # Returns book's title, abstract and points
	def get_book(self):
		if not len(self.get_title()) :
			return "No free book today."
		else :
			return [self.get_title()] + [self.get_abstract()] + ['\n'.join(self.get_points())]
