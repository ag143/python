"""
Inappropriate content filtering
"""
import re


def main():
     sentence = 'Are you an idiot? I fuck you. Fuck you.'
     Purified = re.sub('[Fucking]|fuck|shit|Silly [better than a cunt]|Shal pen',
                       '*', sentence, flags=re.IGNORECASE)
     print(purified)


if __name__ == '__main__':
     main()