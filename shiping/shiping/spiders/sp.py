import scrapy
from ..items import ShipingItem

class SpSpider(scrapy.Spider):
    name = 'sp'
    allowed_domains = ['mixkit.co']
    start_urls = ['https://mixkit.co/free-stock-video/nature/']
    b = 1
    base_url = 'https://mixkit.co/free-stock-video/nature/?page='

    def parse(self, response):

        li_div = response.xpath('//div[@class="item-grid-wrapper"]/div')    #包围所有视频的div
        for li in li_div:                                               #循环每一个视频div
            sp = str(li.xpath('.//video/@src').get()).replace('preview','download').replace('small','4k') #视频下载链接
            #sp = li.xpath('.//video/@src').get()
            link = 'https://mixkit.co/' + li.xpath('.//a/@href').get()  #视频连接
            name = str(li.xpath('.//h2/a/text()').get())+'-4k.mp4'   #这里截取h2标题中的文字
            tubiao = str(li.xpath('./div/div/@class').get())[-2:]
            if tubiao != '4k':      #判断不是4k视频就下载1080p
                sp = str(li.xpath('.//video/@src').get()).replace('preview','download').replace('-small','')
                name = str(li.xpath('.//h2/a/text()').get()) + '-1080p.mp4'
            # print(tubiao)
            # print(sp)
            # print(link) #测试
            # print(name)
            bookitem = ShipingItem(sp=sp, link=link, name=name)
            # 将bookitem对象传给管道
            yield bookitem
        if self.b < 42:
            self.b = self.b + 1
            url = self.base_url + str(self.b)
            print('正在爬取：',url)
            yield scrapy.Request(url=url, callback=self.parse)  # 发送请求 指定函数处理