import scrapy

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.54.06.00.00.00.html']

    def parse(self, response):

        books = response.css('.bigimg li')

        for book in books:
            title = book.css('.name a::text').get()
            author = book.css('.author a::text').get()
            price = book.css('.price .search_now_price::text').get()

            yield {
                'title': title,
                'author': author,
                'price': price,
            }

        next_page = response.css('.next::attr(href)').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
