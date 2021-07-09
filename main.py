from scrapy_html import ScrapyMe


def main():
    key_word = 'Medication Recommendation'
    url = 'https://www.connectedpapers.com/'
    sc = ScrapyMe(url, key_word)
    sc.scrapy_mess()


if __name__ == '__main__':
    main()
