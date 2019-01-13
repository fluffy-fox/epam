'''
файл логов в архиве access
'''

import re
from collections import Counter
class LogParser(object):


    def __init__(self, filename: str):
        self.filename = filename

    def get_most_common(self, number):
        ipregex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        iplist = re.findall(ipregex, open(self.filename).read())
        return Counter(iplist).most_common(number)

    def log_by_http_code(self, file_to_save: str, code: int):
        codstr = "[' " + str(code) + " ']"
        with open(self.filename, 'r') as file:
            with open(file_to_save, "w") as new_file:
                for line in file:
                    if str(re.findall('\s' + str(code) + '\s', line)) == codstr:
                        new_file.write(line)
