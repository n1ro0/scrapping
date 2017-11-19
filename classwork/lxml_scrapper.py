from lxml import html
import requests, settings, re, time


def get_page(url):
    req = requests.get(url, headers=settings.ZF_FM_HEADERS)
    page = html.fromstring(req.content.decode(req.encoding))
    return page

def parse_zf_fm():
    url = 'https://zf.fm/mp3/search?keywords=nightwish'
    mainxpath = '//div[contains(@class, "song-xl")][contains(@class, "song")]/span/@data-title'
    xpath = '//a[@class="next next-btn"]/@href'
    while True:
        page = get_page(url)
        result = page.xpath(mainxpath)
        paths = page.xpath(xpath)
        for i in result:
            if re.search(r'^.+ -*', i) != None:
                print(i)
        if len(paths) == 0:
            break
        url = 'https://zf.fm' + paths[0]
        time.sleep(2)

if __name__ == "__main__":
    parse_zf_fm()
    # url = "https://www.google.com.ua/search?rlz=1C1CHBF_enUA748UA749&ei=AO0OWunnM4ni6ATnx72YAg&q=olx&oq=olx&gs_l=psy-ab.3..0i71k1l4.0.0.0.138903.0.0.0.0.0.0.0.0..0.0....0...1..64.psy-ab..0.0.0....0.gPMY6aIvvu8"
    # uo = urlopen("https://habrahabr.ru/")
    # reqq = requests.get("https://habrahabr.ru/")
    # page = html.parse(uo).getroot()
    # result = page.xpath('//li/article[contains(@class,"post_preview")]/h2/a/@href')
    #result = page.xpath('//li/article[contains(@class,"post_preview")]/h2/a/@href')
    # for i in result:
    #     print(i)

    #method2
    #url = "https://play.google.com/store/apps/details?id=ua.slando&hl=ru"




    # req = requests.get(url, headers=settings.HEADERS)
    # page2 = html.fromstring(req.content)
    # result = page2.xpath('//div[@class="rc"]/h3[@class="r"]//a/text()[1]')
    # for i in result:
    #     print(i)
    # result = page2.xpath('//div[@class="rc"]/h3[@class="r"]//a/@href')
    # for i in result:
    #     print(i)
    # for urli in result:
    #     req = requests.get(urli, headers=settings.HEADERS)
    #     page = html.fromstring(req.content.decode())
    #     resultn = page.xpath('//title//text()[1]')
    #     resultr = page.xpath('//meta//@charset')
    #     if len(resultn) != 0:
    #         print(resultn[0])
