from scrapy_html import ScrapyMe


def main():
    key_word = input("请输入查询关键字：")
    url = 'https://www.connectedpapers.com/'
    sc = ScrapyMe(url, key_word.strip())
    sc.scrapy_mess()


if __name__ == '__main__':
    main()
