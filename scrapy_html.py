import csv
import time
from openpyxl import load_workbook
from selenium import webdriver
from openpyxl import Workbook
from translate import translate
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ScrapyMe(object):
    def __init__(self, url, key_words):
        chrome_options = webdriver.ChromeOptions()
        # 使用headless无界面浏览器模式
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        # 启动浏览器，获取网页源代码
        self.browser = webdriver.Chrome(options=chrome_options)
        self.browser.implicitly_wait(10)
        self.url = url
        self.key_words = key_words

    def scrapy_mess(self):
        self.browser.get(self.url)
        # 检索
        for key_word in self.key_words:
            # self.browser.find_element_by_xpath('//input[@class="autocomplete-searchbar input-field-button"]').send_keys(
            #     key_word)
            self.browser.get(f"https://www.connectedpapers.com/search?q={key_word.replace('%', ' ')}")
            # self.browser.find_element_by_xpath('//div[@class="outlined-slot"]').click()
            # 检索内容
            content = self.search_mess()
            print(key_word, len(content))
            # xlsx保存
            self.store_mess(content, key_word)
            print(key_word + "scrapy success !")

    def search_mess(self):
        wl = []
        # for q in range(33):
        while True:
            articles = self.browser.find_elements_by_xpath('//article[@class="search-result-component shadowed-box"]')
            for article in articles:
                title = article.find_element_by_xpath('.//span[@class="paper-title"]').text
                authors = article.find_element_by_xpath('.//div[@class="search-result-authors"]').text
                cites = article.find_element_by_xpath('.//div[@class="search-result-meta"]').text
                a = cites.split('.')
                b, c = a[0], a[-1]
                href = article.find_elements_by_xpath('.//div[@class="search-result-links flexrow links-box"]/a')[
                    0].get_property('href')
                # print(href)
                # ab = article.find_element_by_xpath('.//div[@class="search-result-abstract folded"]/div').text
                # translate_title, translate_ab = None, None
                # if title:
                #     translate_title = translate(title)
                # if ab:
                #     translate_ab = translate(ab)
                # wl.append([title, authors, cites, href, ab, translate_title, translate_ab])
                wl.append([title, authors, b, c, href])
            try:
                if self.browser.find_elements_by_xpath('//div[@class="page-selector flexrow"]/a')[-1].get_property(
                        'href') == self.browser.current_url:
                    break
            except:
                break
            try:
                self.browser.find_elements_by_xpath('//div[@class="page-selector flexrow"]/a')[-1].click()
            except:
                break
        return wl

    def store_mess(self, content, keyword):
        # wb = Workbook()
        # ws = wb.active
        # # ws.append(['title', 'authors', 'cites', 'href', 'abstract', 'translate_title', 'translate_abstract'])
        # ws.append(['title', 'authors', 'periodical', 'cites', 'href'])
        # for c in content:
        #     ws.append(c)
        # wb.save(f"{keyword.replace(' ', '_')}.xlsx")
        with open('medical.csv', 'a') as wf:
            writer = csv.writer(wf)
            writer.writerows(content)
        print(f"{keyword} to csv success")


if __name__ == '__main__':
    # with open('medical.csv', 'w') as wf:
    #     writer = csv.writer(wf)
    #     writer.writerow(['title', 'authors', 'periodical', 'cites', 'href'])
    with open('medical.csv', 'r') as rf:
        reader = csv.reader(rf)
        s = set()
        me = []
        for i in reader:
            if i[0] not in s:
                me.append(i)
                s.add(i[0])
        with open('nmedical.csv', 'w') as wf:
            writer = csv.writer(wf)
            writer.writerows(me)


