import scrapy

class SephoraPerfumeSpider(scrapy.Spider): # Create sephora perfume subclass of Spider class provided by Scrapy
    name = 'sephora_perfume'
    # start_urls = ['https://www.sephora.com/shop/perfume?currentPage=%' % page for page in range(1,14)] # Range should be one more than you want
    start_urls = ['https://www.sephora.com/shop/perfume']
    # What we want to do is get the HTML content and then get pull data out of tags
    # For this we're going to want the brand, the price, the name of the perfume
    # We'll also want the link to the page to get the description
    def parse(self, response):
        # To get attributes we want, define selectors
        name_selector = 'span[data-at="sku_item_name"]::text'
        brand_selector = 'span[data-at="sku_item_brand"]::text'
        price_selector = 'span[data-at="sku_item_price_list"]::text'
        product_names = response.css(name_selector).getall()
        product_brands = response.css(brand_selector).getall()
        product_prices = response.css(price_selector).getall()

        for index,product in enumerate(product_names):
            yield{
            'product_name': product_names[index],
            'brand_name': product_brands[index],
            'product_price': product_prices[index]
        }
