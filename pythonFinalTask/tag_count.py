import requests
from bs4 import BeautifulSoup
import time
import boto3


def tag_counter(url: str="https://google.com", log_file: str="temp.log", s3_bucket: str='epamcourse'):
    page = requests.get(url)
    x = page.content
    soup = BeautifulSoup(x, "html.parser")
    y = [tag.name for tag in soup.find_all()]
    result = dict((i, y.count(i)) for i in y)
    total_count = sum(result.values())
    date_time = time.strftime("%Y/%m/%d %H:%M")
    log = "{}  {}  {} {} \n".format(date_time, url, total_count, result)
    with open(log_file, 'a') as f:
        f.write(log)
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file(log_file, s3_bucket, log_file)

url = input('Enter site url: ')
log_file = input('Enter log name: ')
s3_bucket = input('Enter your s3 bucket name: ')


tag_counter(url, log_file, s3_bucket)