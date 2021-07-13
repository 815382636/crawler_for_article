from selenium import webdriver
from openpyxl import Workbook
from translate import translate


class ScrapyMe(object):
    def __init__(self, url, key_word):
        chrome_options = webdriver.ChromeOptions()
        # 使用headless无界面浏览器模式
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        # 启动浏览器，获取网页源代码
        self.browser = webdriver.Chrome(options=chrome_options)
        self.browser.implicitly_wait(10)
        self.url = url
        self.key_word = key_word

    def scrapy_mess(self):
        self.browser.get(self.url)
        # 检索
        self.browser.find_element_by_xpath('//input[@class="autocomplete-searchbar input-field-button"]').send_keys(
            self.key_word)
        self.browser.find_element_by_xpath('//div[@class="outlined-slot"]').click()
        # 检索内容
        content = self.search_mess()
        # xlsx保存
        self.store_mess(content)
        print("scrapy success !")

    def search_mess(self):
        wl = []
        for i in range(10):
            articles = self.browser.find_elements_by_xpath('//article[@class="search-result-component shadowed-box"]')
            for article in articles:
                title = article.find_element_by_xpath('.//span[@class="paper-title"]').text
                authors = article.find_element_by_xpath('.//div[@class="search-result-authors"]').text
                cites = article.find_element_by_xpath('.//div[@class="search-result-meta"]').text
                ab = article.find_element_by_xpath('.//div[@class="search-result-abstract folded"]/div').text
                translate_title, translate_ab = None, None
                if title:
                    translate_title = translate(title)
                if ab:
                    translate_ab = translate(ab)
                wl.append([title, authors, cites, ab, translate_title, translate_ab])
            self.browser.find_elements_by_xpath('//div[@class="page-selector flexrow"]/a')[-1].click()
        return wl

    def store_mess(self, content):
        wb = Workbook()
        ws = wb.active
        ws.append(['title', 'authors', 'cites', 'abstract', 'translate_title', 'translate_abstract'])
        for c in content:
            ws.append(c)
        wb.save(f"{self.key_word.replace(' ', '_')}.xlsx")
