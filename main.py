from scrapy_certain import ScrapyCe
from scrapy_html import ScrapyMe


def main():
    key_word = input("1. 关键字查询 \n2. 具体网址查询 \n请选择查询方式：")
    if key_word == '1':
        key_word = input("请输入查询关键字：")
        url = 'https://www.connectedpapers.com/'
        sc = ScrapyMe(url, key_word.strip())
        sc.scrapy_mess()
    elif key_word == '2':
        url = input("请输入url地址：")
        # url = 'https://www.connectedpapers.com/main/c3229debfda1b015c88404cf98f1074237d80809/Pretraining-of-Graph-Augmented-Transformers-for-Medication-Recommendation/graph'
        sc = ScrapyCe(url)
        sc.scrapy_mess()
    else:
        print('查询失败 ！')


if __name__ == '__main__':
    main()
