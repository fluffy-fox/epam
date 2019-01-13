import requests
from bs4 import BeautifulSoup
import time
import boto3


url = "https://google.com"
page = requests.get(url)
x = page.content
soup = BeautifulSoup(x, "html.parser")
y = [tag.name for tag in soup.find_all()]
result = dict((i, y.count(i)) for i in y)

total_count = sum(result.values())
date_time = time.strftime("%Y/%m/%d %H:%M")
log = "{}  {}  {} {} \n".format(date_time, url, total_count, result)
with open("temp.log", 'a') as f:
    f.write(log)
# print(log)

s3 = boto3.resource('s3')
s3.meta.client.upload_file('temp.log', 'epamcourse', 'temp.log')
