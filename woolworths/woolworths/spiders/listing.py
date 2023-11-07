# -*- coding: utf-8 -*-
import scrapy
from woolworths.items import WoolworthsItem


class ListingSpider(scrapy.Spider):
    name = 'listing'
    allowed_domains = ['https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas']
    start_urls = ['http://https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas']

    def parse(self, response):
        item = WoolworthsItem()
        Breadcrumb = []
        Breadcrumb_1  = response.xpath('//*[@class="breadcrumbs ng-star-inserted"]/ul/li/span/a/text()').getall()
        Breadcrumb_2 = response.xpath('//*[@class="breadcrumbs ng-star-inserted"]/ul/li/span/span/text()').get()
        for i in Breadcrumb_1:
            Breadcrumb.append(i)
        Breadcrumb.append(Breadcrumb_2)

        print(Breadcrumb)
        
        for i in response.xpath('//*[@class="product-tile-v2"]'):
            item['Name'] = i.xpath("./div/a/@aria-label").get('').strip()
            item['item_url'] = i.xpath('./div/a/@href').get('').strip()
            item['thumbnail_url'] = i.xpath('./div/a/img/@src').get('').strip()
            item['price'] = i.xpath('./div[3]/div//div/div/text()').get('').strip()
            
        yield item
        
        
        
# this is provided by xpath code
# proper response we are getting from API is GET API 
        #Request URL:https://woolworthsfoodgroup.sc.omtrdc.net/b/ss/wfg-wx-global-prod/10/JS-2.23.0/s73594013463854?AQB=1&ndh=1&pf=1&callback=s_c_il[1].doPostbacks&et=1&t=7%2F10%2F2023%2016%3A31%3A1%202%20-330&d.&nsid=0&jsonv=1&.d&D=D%3D&mid=35953546181255126844036889578931233576&aamlh=12&ce=UTF-8&cdp=3&pageName=ww-sm%3Ashop%3Abrowse%3Adrinks%3Acordials-juices-iced-teas%3Aiced-teas&g=https%3A%2F%2Fwww.woolworths.com.au%2Fshop%2Fbrowse%2Fdrinks%2Fcordials-juices-iced-teas%2Ficed-teas&cc=AUD&ch=Products%20Section&server=www.woolworths.com.au&events=event1&c1=Woolworths&v1=D%3Dc1&c2=Supermarkets&v2=D%3Dc2&c3=Web&v3=D%3Dc3&c4=D%3DpageName&c6=%2Fshop%2Fbrowse%2Fdrinks%2Fcordials-juices-iced-teas%2Ficed-teas&v6=D%3DpageName&c8=link&c9=018b992c439600026db5f87321b20506f00540670086e&v9=D%3Dc6&c16=web_performance&v21=D%3Dmid&v62=none%7Cnone&c66=woolworths%2Fsupermarkets%2F202310260028&c72=D%3Dc8&c74=qurl3t&v120=not%20set&v129=webVitals&v131=CLS&v132=0.07522042286139237&v146=D%3DUser-Agent&v202=Unknown&v203=Unknown&v211=Unknown&v212=false&v213=false&v214=Unknown&pe=lnk_o&pev2=no%20link_name&s=1366x768&c=24&j=1.6&v=N&k=Y&bw=1366&bh=643&mcorgid=4353388057AC8D357F000101%40AdobeOrg&lrt=335&AQE=1
        # Request Method:GET
        # payload : {"AQB: 1
                    # ndh: 1
                    # pf: 1
                    # callback: s_c_il[1].doPostbacks
                    # et: 1
                    # t: 7/10/2023 16:31:1 2 -330
                    # d.: 
                    # nsid: 0
                    # jsonv: 1
                    # .d: 
                    # D: D=
                    # mid: 35953546181255126844036889578931233576
                    # aamlh: 12
                    # ce: UTF-8
                    # cdp: 3
                    # pageName: ww-sm:shop:browse:drinks:cordials-juices-iced-teas:iced-teas
                    # g: https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas
                    # cc: AUD
                    # ch: Products Section
                    # server: www.woolworths.com.au
                    # events: event1
                    # c1: Woolworths
                    # v1: D=c1
                    # c2: Supermarkets
                    # v2: D=c2
                    # c3: Web
                    # v3: D=c3
                    # c4: D=pageName
                    # c6: /shop/browse/drinks/cordials-juices-iced-teas/iced-teas
                    # v6: D=pageName
                    # c8: link
                    # c9: 018b992c439600026db5f87321b20506f00540670086e
                    # v9: D=c6
                    # c16: web_performance
                    # v21: D=mid
                    # v62: none|none
                    # c66: woolworths/supermarkets/202310260028
                    # c72: D=c8
                    # c74: qurl3t
                    # v120: not set
                    # v129: webVitals
                    # v131: CLS
                    # v132: 0.07522042286139237
                    # v146: D=User-Agent
                    # v202: Unknown
                    # v203: Unknown
                    # v211: Unknown
                    # v212: false
                    # v213: false
                    # v214: Unknown
                    # pe: lnk_o
                    # pev2: no link_name
                    # s: 1366x768
                    # c: 24
                    # j: 1.6
                    # v: N
                    # k: Y
                    # bw: 1366
                    # bh: 643
                    # mcorgid: 4353388057AC8D357F000101@AdobeOrg
                    # lrt: 335
                    # AQE: 1"}

