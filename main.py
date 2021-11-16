from scrapy_certain import ScrapyCe
from scrapy_html import ScrapyMe

# words = ['Intracerebral injury',
#          'Intracerebral hemorrhage,traumatic',
#           'Intracerebral hemorrhage in cerebellum',
words = ['Intracerebral hemorrhage In parenchyma',
         'Intracerebral hemorrhage hypertensive',
         'Intrarentricular hemorrhage',
         'Intrarentricular conducition delay',
         'Intrarentricular hemorrhage neonatal',
         'Intrarentricular hemorrhage of prematurity',
         'Intrarentricular sepatal defect',
         'Intrarentricular Fraction',
         'Intrarentricular hemorrhage',
         'Intrarentricular hemorrhage',
         'Intrarentricular conducition delay',
         'Intrarentricular hemorrhage neonatal',
         'Intrarentricular hemorrhage of prematurity',
         'Intrarentricular sepatal defect',
         'Intrarentricular Fraction',
         'Intrarentricular Opacification',
         'Intrarentricular hemorrhage',
         'Sroke',
         'Stroke Acute',
         'Stroke Sequelae',
         'Stroke ischemic',
         'Stroke syndrome',
         'Stroke Lacunar',
         'Stroke hemorrhagic',
         'Stroke thrombotic',
         'Stroke cardiovascular',
         'Cerebrovascular disease',
         'Cerebrovascular disease sequelae',
         'Cerebrovascular disease small ressel',
         'Cerebral Palsy',
         'Cerebral infarction',
         'Cerebral ischemia',
         'Cerebral edema',
         'Cerebral hemorrhage',
         'Cerebral vasospasm',
         'Cerebral stroke',
         'Cerebral tumor',
         'Cerebral palsy',
         'Cerebral spastic',
         'Intracerebral hemorrhage',
         'Intracerebral hematoma'
         ]


def main():
    key_word = input("1. 关键字查询 \n2. 具体网址查询 \n请选择查询方式：")
    if key_word == '1':
        # key_word = input("请输入查询关键字：")
        key_words = words
        url = 'https://www.connectedpapers.com/'
        sc = ScrapyMe(url, key_words)
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
