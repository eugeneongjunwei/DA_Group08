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
# first commit
