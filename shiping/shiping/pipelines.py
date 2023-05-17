# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import pymysql
from scrapy.pipelines.files import FilesPipeline
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import requests
import os
class ShipingPipeline:
     def process_item(self, item, spider):
         return item


class DownloadPipeline(FilesPipeline):
    #def process_item(self,item,sider):
    def get_media_requests(self, item, info):
        # print(item.get('sp'))
        # print(item.get('name'))
        url = item.get('sp')
        name = item.get('name')
        # 依次对视频地址发送请求，meta用于传递视频的文件名
        yield scrapy.Request(url=url, meta={'name':name})

    def file_path(self, request, response=None, info=None, *, item=None):

        filename = request.meta['name']  # 获取视频文件名
        return filename  # 返回下载的视频文件名

    def item_completed(self, results, item, info):
        print('正在下载：',item.get('name'))
        return item


class MysqlPipeline():
    #连接数据库
    def open_spider(self,spider):
        print('=======open_spider=======')
        # 获取settings属性
        host = spider.settings.get('DB_HOST')  # 主机
        port = spider.settings.get('DB_PORT')  # 端口号
        user = spider.settings.get('DB_USER')  # 用户名
        password = spider.settings.get('DB_PASSWORD')  # 密码
        db = spider.settings.get('DB_NAME')  # 数据库名
        charset = spider.settings.get('DB_CHARSET')  # 字符编码
        # 连接数据库pymysql.connect(host,port,user,password,db,charset)
        self.connect = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset)
        self.cursor = self.connect.cursor()
        # sql建表语句
        sql = '''
        create table if not exists mixkit(id int primary key auto_increment,
        sp_name varchar(200) not null,
        download_link varchar(200) not null,
        sp_link varchar(200));
        '''
        # 执行sql语句 创建dang_book表
        self.cursor.execute(sql)
    #数据库写入数据
    def process_item(self,item,spider):
        #编写sql语句
        sql = 'insert into mixkit(sp_name,download_link,sp_link) values ("{}","{}","{}")'\
            .format(str(item.get('name')),str(item.get('sp')),str(item.get('link')))
        # 执行sql语句
        self.cursor.execute(sql)
        # 提交
        self.connect.commit()
        print(item.get('name'),'    数据写入成功！')
        return item
    #关掉连接
    def close_spider(self,spider):
        print('=======数据库已关闭=======')
        # 关闭数据库连接
        self.cursor.close()
        self.connect.close()






