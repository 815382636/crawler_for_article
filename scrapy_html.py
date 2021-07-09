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
        self.browser.find_element_by_xpath('//input[@class="autocomplete-searchbar input-field-button"]').send_keys(
            self.key_word)
        self.browser.find_element_by_xpath('//div[@class="outlined-slot"]').click()
        # 检索内容
        self.search_mess()

    def search_mess(self):
        articles = self.browser.find_elements_by_xpath('//article[@class="search-result-component shadowed-box"]')

        for article in articles:
            title = article.find_element_by_xpath('.//span[@class="paper-title"]').text
            authors = article.find_element_by_xpath('.//div[@class="search-result-authors"]').text
            cites = article.find_element_by_xpath('.//div[@class="search-result-meta"]').text
            ab = article.find_element_by_xpath('.//div[@class="search-result-abstract folded"]/div').text
