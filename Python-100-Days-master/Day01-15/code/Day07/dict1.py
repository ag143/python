"""
Define and use dictionaries

Version: 0.1
Author: author
Date: 2018-03-06
"""


def main():
     scores = {'author': 95, 'Bai Yuanfang': 78, 'Di Renjie': 82}
     print(scores['author'])
     print(scores['Di Renjie'])
     for elem in scores:
         print('%s\t--->\t%d' % (elem, scores[elem]))
     scores['Bai Yuanfang'] = 65
     scores['Zhuge Wanglang'] = 71
     scores.update(cold noodles=67, Fang Qihe=85)
     print(scores)
     if 'Wu Zetian' in scores:
         print(scores['Wu Zetian'])
     print(scores.get('Wu Zetian'))
     print(scores.get('Wu Zetian', 60))
     print(scores.popitem())
     print(scores.popitem())
     print(scores.pop('author', 100))
     scores.clear()
     print(scores)


if __name__ == '__main__':
     main()