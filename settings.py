URL = 'https://habrahabr.ru/flows/develop/'
URLS_XPATH = '//h2[@class="post__title"]/a/@href'
TITLE_XPATH = '//span[@class="post__title-text"]/text()'
HUBS_XPATH = '//ul[@class="post__hubs post__hubs_full-post inline-list"]/*/a'
ARTICLE_XPATH = '//div[@class="post__text post__text-html js-mediator-article"]'


GOOGLE_HEADERS = {
    'authority': 'www.google.com.ua',
    'path': '/search?rlz=1C1CHBF_enUA748UA749&ei=AO0OWunnM4ni6ATnx72YAg&q=olx&oq=olx&gs_l=psy-ab.3..0i71k1l4.0.0.0.138903.0.0.0.0.0.0.0.0..0.0....0...1..64.psy-ab..0.0.0....0.gPMY6aIvvu8',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'utf-8',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '_ga=GA1.1.1522051236.1498400927; SID=ZAWrxCXKMGPiw_QJprRv8fKTIacqcO8Y6uev_k6lHHzUsPjIlw3pEgI8M5jzViOEemiuBw.; HSID=AiYOQ13yCnFuCnKvc; SSID=AUH95gubOOBdT7hhD; APISID=nsrt4EAOPKlhoq2T/Adn2oi9K0U7Pz7Jep; SAPISID=TUClcdQl5k5FDHWM/AzRO7YX03GmpiGUpo; CONSENT=YES+NL.en+V7; NID=117=RMmN4k1ntsPSyNxLicdThyj_GtbuiFGgcJE9rz7fsKoDhR7IE-hQjnKzzSZQIY7yIPWTv4TBcnvHCelJdRWPWSIFQPTSdNtkzlIJKTmMFQnjB6f_voy_ZTxp-nN1mbRxDibA0lxmfVWpPgDpdwVLJKIlRJzy9N-efgTGpg1qlniMWdJmN3wk-F0-RpjrzMiKUjkPan_6pe7KaD8I; 1P_JAR=2017-11-17-14; DV=o1Wmcp1kXGZDEOtutUnHL6TE2Nyk_JXOrgRKHXJblgQAAMDORODQfnDhKwEAANB-P1AgQfHzTAAAAA',
    'referer': 'https://www.google.com.ua/',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'x-client-data': 'CKG1yQEIjbbJAQiitskBCMS2yQEI+pzKAQipncoBCJOiygEIqKPKAQ==',
    }

ZF_FM_HEADERS = {
    'authority': 'zf.fm',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'ZvcurrentVolume=100; __cfduid=dd8ab0f52903f2489d1198ecbbc5f47bc1497435556; zvAuth=1; zvLang=0; _ym_uid=14974357681057556198; PHPSESSID=54nvt2mngovf7j7tremh66gqh2; notice=11; ZvcurrentVolume=100; _ga=GA1.2.302250451.1497435756; _gid=GA1.2.1482314633.1510992911',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
