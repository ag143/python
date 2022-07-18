"""
Read JSON data

Version: 0.1
Author: author
Date: 2018-03-13
"""

import json
import csv2

json_str = '{"name": "author", "age": 38, "title": "called beast"}'
result = json.loads(json_str)
print(result)
print(type(result))
print(result['name'])
print(result['age'])

# Pass the converted dictionary as a keyword argument to the Teacher's constructor
teacher = csv2.Teacher(**result)
print(teacher)
print(teacher.name)
print(teacher.age)
print(teacher.title)

# Please think about how to convert the weather data in JSON format below into an object and get the information we need
# Later we will explain how to get the JSON format data we need through the network API
"""
    {
        "wendu": "29",
        "ganmao": "The weather conditions are suitable, and the chance of getting a cold is low. But please avoid staying in an air-conditioned room for a long time to prevent a cold.",
        "forecast": [
            {
                "fengxiang": "Southern Wind",
                "fengli": "Level 3-4",
                "high": "High temperature 32℃",
                "type": "Cloudy",
                "low": "Low temperature 17℃",
                "date": "Tuesday the 16th"
            },
            {
                "fengxiang": "Southern Wind",
                "fengli": "Breeze level",
                "high": "High temperature 34℃",
                "type": "Sunny",
                "low": "Low temperature 19℃",
                "date": "Wednesday the 17th"
            },
            {
                "fengxiang": "Southern Wind",
                "fengli": "Breeze level",
                "high": "High temperature 35℃",
                "type": "Sunny",
                "low": "Low temperature 22℃",
                "date": "Thursday the 18th"
            },
            {
                "fengxiang": "Southern Wind",
                "fengli": "Breeze level",
                "high": "High temperature 35℃",
                "type": "Cloudy",
                "low": "Low temperature 22℃",
                "date": "Friday the 19th"
            },
            {
                "fengxiang": "Southern Wind",
                "fengli": "Level 3-4",
                "high": "High temperature 34℃",
                "type": "Sunny",
                "low": "Low temperature 21℃",
                "date": "Saturday the 20th"
            }
        ],
        "yesterday": {
            "fl": "Breeze",
            "fx": "South Wind",
            "high": "High temperature 28℃",
            "type": "Sunny",
            "low": "Low temperature 15℃",
            "date": "Monday the 15th"
        },
        "aqi": "72",
        "city": "Beijing"
    }
"""