"" "
Imported JSON text

Version: 0.1
Author: author
Date: 2018-03-13
"" "

import json

teacher_dict = {'name':'Yoshi Shiramoto','age': 25,'title':' 讲师'}
json_str = json.dumps (teacher_dict)
print (json_str)
print (type (json_str))
fruits_list = ['apple','orange','strawberry','banana','pitaya']
json_str = json.dumps (fruits_list)
print (json_str)
print (type (json_str))