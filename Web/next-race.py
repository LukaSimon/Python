import requests
from bs4 import BeautifulSoup as bs
import prettytable
import hashlib 


def del_line_3(fn):
    f = open(fn)
    output = []
    str = ' <meta content="'
    for line in f:
        if line.startswith(str):
            line = line.strip(str)
            output.append(line)
    f.close()
    f = open(fn, 'w')
    f.writelines(output)
    f.close()


def del_line_4(fn):
    f = open(fn)
    output = []
    str = 'https'
    for line in f:
        if not line.startswith(str):
            line = line.strip(str)
            output.append(line)
    f.close()
    f = open(fn, 'w')
    f.writelines(output)
    f.close()


def del_line_5(fn):
    f = open(fn)
    output = []
    for line in f:
        if line.startswith('2021') or line.startswith('2022'):
            output.append(line)
        elif not line[0].isdigit():
            output.append(line)
    f.close()
    f = open(fn, 'w')
    f.writelines(output)
    f.close()


def del_line_6(fn):
    f = open(fn)
    output = []
    str = ['" itemprop="name"/', '" itemprop="address"/', '" itemprop="startDate"/', '" itemprop="endDate"/']
    for line in f:
        line = line.replace(str[0], '')
        line = line.replace(str[1], '')
        line = line.replace(str[2], '')
        line = line.replace(str[3], '')
        output.append(line)
    f.close()
    f = open(fn, 'w')
    f.writelines(output)
    f.close()


def doubles(input, output):
    comp_lines = set()
    output_file = open(output, "w")
    for line in open(input, "r"):
        hash_value = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
        if hash_value not in comp_lines:
            output_file.write(line)
            comp_lines.add(hash_value)
    output_file.close()


URL = 'https://www.formel1.de/'
PFAD = 'formel-1-kalender/2021'

s = requests.session()

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
           'Host': URL,
           'Referer': URL + PFAD}

s.post(URL, headers=HEADERS)

soup = bs(s.get(URL + PFAD).text, 'html.parser')

next_race = soup.find_all('tr', class_='next-race')

char = '<>'
for x in range(len(char)):
    a = str(next_race).replace(char[x], '\n')

f = open("location.txt", 'w+')
f.truncate()
f.write(a)
f.close()
del_line_3('location.txt')
del_line_4('location.txt')
del_line_5('location.txt')
del_line_6('location.txt')
doubles('location.txt', 'location_2.txt')

f = open('location_2.txt', 'r')
content = f.readlines()
a = content[4].replace('T', ', ')
tabel = prettytable.PrettyTable(['Track', 'Country, Name', 'Grand Prix', 'Date, Time'])
tabel.add_row([content[0], content[1], content[2], a])
print(tabel)
