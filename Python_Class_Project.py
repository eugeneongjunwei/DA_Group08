#Perform Get request on website
import requests
url = 'https://brickset.com/sets/year-2005'
r = requests.get(url)
print(r.text)

#Displays OK retun status
print("Status code:")
print("\t*",r.status_code)

#Display website header
h = requests.head(url)
print("Header:")
print("**********")
for x in h.headers:
    print("\t",x,":",h.headers[x])
print("**********")

#modify the Header user-agent to display "mobile"
headers = {
    'User-Agent':'Iphone X'
}
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)

import scrapy

class NewSpider(scrapy.Spider):
    name = "new_spider"

    start_urls = ['http://10.10.11.178/index.html']
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'

            yield{
                'Image Link': x.xpath(newsel).extract_first(),
            }

        Page_selector = '.next a ::attr(href)'

        next_page = response.css(Page_selector).extract_first()

        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

import unittest

class Python_Class_Project(unittest.TestCase):

    def test_EngineType(self):
        print("Testing")

if __name__ == '__main__':
    unittest.main()
