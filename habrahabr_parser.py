from lxml import html
import requests, settings, re, time, json


def get_page(url):
    req = requests.get(url)
    page = html.fromstring(req.content.decode(req.encoding))
    return page

def parse_post_title(page):
    title = next((item for item in page.xpath(settings.TITLE_XPATH) if item is not None), 'No title')
    return title

def parse_post_hub(element):
    hub = {}
    link = next((item for item in element.xpath('@href') if item is not None), 'No link')
    name = next((item for item in element.xpath('text()') if item is not None), 'No name')
    hub['name'] = name
    hub['link'] = link
    return hub

def parse_post_hubs(page):
    hubs_elements = page.xpath(settings.HUBS_XPATH)
    hubs = []
    for element in hubs_elements:
        hubs.append(parse_post_hub(element))
    return hubs


def parse_article_text(element):
    return  ''.join(element.xpath('.//text()'))


def parse_article_images(element):
    return element.xpath('.//@src')


def parse_article_link(element):
    link = {}
    link['text'] = next((item for item in element.xpath('text()') if item is not None), 'No text')
    link['link'] = next((item for item in element.xpath('@href') if item is not None), 'No link')
    return link


def parse_article_links(element):
    links = []
    link_elements = element.xpath('a')
    for element in link_elements:
        links.append(parse_article_link(element))
    return links


def parse_post_article(page):
    article = {}
    article_element = next((item for item in page.xpath(settings.ARTICLE_XPATH) if item is not None), None)
    if article is None:
        return 'No article'
    article['text'] = parse_article_text(article_element)
    article['images'] = parse_article_images(article_element)
    article['links'] = parse_article_links(article_element)
    return article

def parse_habrahabr_post(url):
    post = {}
    page = get_page(url)
    post['title'] = parse_post_title(page)
    post['hubs'] = parse_post_hubs(page)
    post['article'] = parse_post_article(page)
    return post

def parse_habrahabr_posts():
    page = get_page(settings.URL)
    urls = page.xpath(settings.URLS_XPATH)
    posts = []
    for url in urls:
        posts.append(parse_habrahabr_post(url))
    return posts

def save_to_json(filename):
    data = json.dumps(posts)
    with open('{}.json'.format(filename), 'w') as f:
        f.write(data)


if __name__ == "__main__":
    posts = parse_habrahabr_posts()
    for post in posts:
        print(post)
    save_to_json('habrahabr_posts')


