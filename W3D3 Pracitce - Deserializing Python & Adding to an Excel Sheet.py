

import requests
import json
 

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
json_data = response.text
data = json.loads(json_data)

print(data)



from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "Posts"


for row, post in enumerate(data, 1):
    for column, post_value in enumerate(post.values(), 1):
        ws.cell(row=row, column=column, value=str(post_value))

wb.save("C:/Users/moise/Downloads/Data Analysis/VetsInTech/Python Fundamentals/week_3-1/week_3/spreadsheets/ITP Weewk 3 Day 3 Practice.xlsx")