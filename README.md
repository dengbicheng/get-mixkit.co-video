# 爬取mixkit网站上视频

这是一个用于从mixkit.co网站爬取免费的自然主题库存视频的Scrapy爬虫。

## 功能

该爬虫从起始URL 'https://mixkit.co/free-stock-video/nature/' 开始，解析响应以提取有关每个视频的信息。

### 解析函数(parse)

解析函数`parse`用于从响应中提取视频信息。它通过XPath选择器定位到包含所有视频的`div`元素，并对每个视频进行循环处理。

对于每个视频，它会提取视频的下载链接、视频连接和名称。视频下载链接根据规则进行处理，以获得适当的视频质量（4K或1080p）。视频名称是通过截取`h2`标题中的文字生成的。

然后，它会创建一个`ShipingItem`对象，将提取的信息赋值给对象的属性，并通过`yield`语句将该对象传递给管道进行进一步处理。

### 翻页处理

爬虫使用`self.b`作为翻页计数器，并根据需要构建下一页的URL。它将继续发送请求并调用`parse`函数，直到达到最大页数。

请注意，爬虫处理每页的视频信息后，会打印当前正在爬取的URL。

------

以上是对`sp`爬虫的简要介绍和功能说明。根据上述代码，这个爬虫旨在从mixkit.co网站爬取免费的自然主题库存视频。