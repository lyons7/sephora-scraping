import scrapy

class SephoraPerfumeSpider(scrapy.Spider): # Create sephora perfume subclass of Spider class provided by Scrapy
    name = 'sephora_perfume'
    start_urls = ['https://www.sephora.com/shop/perfume']
    # What we want to do is get the HTML content and then get pull data out of tags
    # For this we're going to want the brand, the price, the name of the perfume
    # We'll also want the link to the page to get the description
    def parse(self, response):
        # To get item attributes:
        # span_selector = 'span'
        name_selector = 'span[data-at="sku_item_name"]'
        brand_selector = 'span[data-at="sku_item_brand"]'
        price_selector = 'span[data-at="sku_item_price_list"]'
        for item in response.css(span_selector):
            name_selector = 'span[data-at="sku_item_name"]::text'
            brand_selector = 'span[data-at="sku_item_brand"]::text'
            price_selector = 'span[data-at="sku_item_price_list"]::text'
            # if item.css(name_selector).get() != None and item.css(brand_selector) != None:
            yield{
                'product_name': item.css(name_selector).getall(),
                'brand_name': item.css(brand_selector).getall(),
                'price_range': item.css(price_selector).getall(),
                }
