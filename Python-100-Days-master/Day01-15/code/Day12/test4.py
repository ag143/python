import re


def main():
     # Create a regular expression object Use look-ahead and look-back to ensure that numbers should not appear before and after the phone number
     pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}| 17[678]\d{8})(?=\D)')
     sentence = '''
     Important things have been said 8130123456789 times, my mobile phone number is 13512346789, this pretty number,
     It's not 15600998765, it's also 110 or 119. Wang Dazhui's mobile phone number is 15600998765.
     '''
     # Find all matches and save to a list
     mylist = re.findall(pattern, sentence)
     print(mylist)
     print('-------Ornate divider-------')
     # Take out the matching object through the iterator and get the matching content
     for temp in pattern.finditer(sentence):
         print(temp.group())
     print('-------Ornate divider-------')
     # Find all matches by specifying the search location with the search function
     m = pattern.search(sentence)
     while m:
         print(m.group())
         m = pattern.search(sentence, m.end())


if __name__ == '__main__':
     main()