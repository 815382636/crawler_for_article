from selenium import webdriver


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
        self.browser.find_element_by_xpath('//input[@class="jig-ncbiclearbutton jig-ncbiautocomplete"]').send_keys(
            self.key_word)
        self.browser.find_element_by_xpath('//button[@class="button_search nowrap"]').click()
        # # 检索内容
        find_url = []
        while True:
            trs = self.browser.find_elements_by_xpath('//tr[@class="rprt"]')
            for i in trs:
                find_url.append(i.find_element_by_xpath('.//a').get_property('href'))
            try:
                self.browser.find_element_by_xpath('//a[@class="active page_link next"]').click()
            except:
                break
        for i in find_url:
            print(i)
            self.browser.get(i)
            

        print("scrapy success !")


if __name__ == '__main__':
    sc = ScrapyMe('https://www.ncbi.nlm.nih.gov/gene', '(Cerebrovascular) AND "Homo sapiens"[porgn:__txid9606]')
    sc.scrapy_mess()
