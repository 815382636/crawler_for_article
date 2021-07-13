import time

from selenium import webdriver
from openpyxl import Workbook
from translate import translate


class ScrapyCe(object):
    def __init__(self, url):
        chrome_options = webdriver.ChromeOptions()
        # 使用headless无界面浏览器模式
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        # 启动浏览器，获取网页源代码
        self.browser = webdriver.Chrome(options=chrome_options)
        self.browser.implicitly_wait(10)
        self.url = url

    def scrapy_mess(self):
        self.browser.get(self.url)
        box = self.browser.find_element_by_xpath('//div[@class="abtract-scrollbox shadowed-box"]')
        time.sleep(3)
        title = self.browser.find_element_by_xpath(
            '//div[@class="abtract-scrollbox shadowed-box"]/a[@class="title_link"]').text
        authors = ''.join([i.text for i in self.browser.find_elements_by_xpath(
            '//div[@class="abtract-scrollbox shadowed-box"]/div[@class="metadata"]')])
        cites = self.browser.find_element_by_xpath(
            '//div[@class="abtract-scrollbox shadowed-box"]/div[@class="flexrow"]').text
        ab = self.browser.find_element_by_xpath(
            '//div[@class="abtract-scrollbox shadowed-box"]/div[@class="searchable-text abstract-text"]').text
        translate_title, translate_ab = None, None
        if title:
            translate_title = translate(title)
        if ab:
            translate_ab = translate(ab)
        wl = [[title, authors, cites, ab, translate_title, translate_ab]]
        for article in self.browser.find_elements_by_xpath('//div[@class="list-group minilist-list"]/div'):
            article.click()
            title = self.browser.find_element_by_xpath(
                '//div[@class="abtract-scrollbox shadowed-box"]/a[@class="title_link"]').text
            authors = ''.join([i.text for i in self.browser.find_elements_by_xpath(
                '//div[@class="abtract-scrollbox shadowed-box"]/div[@class="metadata"]')])
            cites = self.browser.find_element_by_xpath(
                '//div[@class="abtract-scrollbox shadowed-box"]/div[@class="flexrow"]').text
            ab = self.browser.find_element_by_xpath(
                '//div[@class="abtract-scrollbox shadowed-box"]/div[@class="searchable-text abstract-text"]').text
            translate_title, translate_ab = None, None
            if title:
                translate_title = translate(title)
            if ab:
                translate_ab = translate(ab)
            wl.append([title, authors, cites, ab, translate_title, translate_ab])

        self.store_mess(wl)
        print("scrapy success !")

    def store_mess(self, content):
        wb = Workbook()
        ws = wb.active
        ws.append(['title', 'authors', 'cites', 'abstract', 'translate_title', 'translate_abstract'])
        for c in content:
            ws.append(c)
        wb.save(f"{self.url.split('/')[-2].strip()}.xlsx")


def main():
    url = 'https://www.connectedpapers.com/main/c3229debfda1b015c88404cf98f1074237d80809/Pretraining-of-Graph-Augmented-Transformers-for-Medication-Recommendation/graph'
    sc = ScrapyCe(url)
    sc.scrapy_mess()


if __name__ == '__main__':
    main()
