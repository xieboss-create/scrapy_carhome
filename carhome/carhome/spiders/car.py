# -*- coding: utf-8 -*-
import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['https://car.autohome.com.cn/price/brand-33.html']
    # 如果爬取的是页面  那么一定要注意起始url的路径后的/
    start_urls = ['https://car.autohome.com.cn/price/brand-33.html']

    # parse方法返回的是一个可以迭代的对象
    def parse(self, response):
        # src //div[@id="brandtab-1"]/div[@class="list-cont"]//img/@src
        # name //div[@id="brandtab-1"]/div[@class="list-cont"]//div[@class="main-title"]/a/text()
        # price //div[@id="brandtab-1"]/div[@class="list-cont"]//span[@class="font-arial"]/text()
        div_list = response.xpath('//div[@id="brandtab-1"]/div[@class="list-cont"]')

        car_list = []

        for div in div_list:
            # xpath方法的返回值类型 一定是列表
            src = div.xpath('.//img/@src').extract_first()
            name = div.xpath('.//div[@class="main-title"]/a/text()').extract_first()
            price = div.xpath('.//span[@class="font-arial"]/text()').extract_first()
            car = {}
            car['src'] = src
            car['name'] = name
            car['price'] = price
            car_list.append(car)
        return car_list