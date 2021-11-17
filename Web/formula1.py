import requests
from bs4 import BeautifulSoup as bs
import prettytable


def cut(word):
  return [char for char in word]


def del_line(fn):
    f = open(fn)
    output = []
    for line in f:
        if not line.startswith("["):
            if not line.startswith("]"):
                if not line.startswith("span"):
                    if not line.startswith("/span"):
                        if not line.startswith(","):
                            if not line.startswith("td"):
                                if not line.startswith("/"):
                                    if not line.startswith("a"):
                                        if line.strip():
                                            output.append(line)
    f.close()
    f = open(fn, 'w')
    f.writelines(output)
    f.close()

URL = 'https://www.formula1.com/'
PFAD = 'en/results.html/2021/drivers.html'
s = requests.session()

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
           'Host': URL,
           'Referer': URL + PFAD
           }

s.post(URL, headers=HEADERS)

soup = bs(s.get(URL + PFAD).text, 'html.parser')

driver_1 = soup.find_all('span', class_="hide-for-tablet")
a_1 = str(cut(driver_1))

driver_2 = soup.find_all('span', class_="hide-for-mobile")
a_2 = str(cut(driver_2))

points = soup.find_all('td', class_="dark bold")
b = str(points)

team = soup.find_all('a', class_="grey semi-bold uppercase ArchiveLink")
c = str(team)

char = '<>'
for x in range(len(char)):
    a_1 = a_1.replace(char[x], '\n')
for x in range(len(char)):
    a_2 = a_2.replace(char[x], '\n')
for i in range(len(char)):
    b = b.replace(char[i], '\n')
for i in range(len(char)):
    c = c.replace(char[i], '\n')

f = open("../Source Files/Pos_1.txt", 'w+')
f.truncate()
f.write(a_1)
f.close()
del_line('../Source Files/Pos_1.txt')

f = open("../Source Files/Pos_2.txt", 'w+')
f.truncate()
f.write(a_2)
f.close()
del_line('../Source Files/Pos_2.txt')

p = open('../Source Files/Point.txt', 'w+')
p.truncate()
p.write(b)
p.close()
del_line('../Source Files/Point.txt')

y = open("../Source Files/Team.txt", 'w+')
y.truncate()
y.write(c)
y.close()
del_line('../Source Files/Team.txt')

driver_1 = open('../Source Files/Pos_1.txt', 'r')
driver_2 = open('../Source Files/Pos_2.txt', 'r')
point = open('../Source Files/Point.txt', 'r')
team = open('../Source Files/Team.txt', 'r')


table = prettytable.PrettyTable(['Position', 'Driver', 'Team', 'Points'])

line_driver_1 = driver_1.readline()
line_driver_2 = driver_2.readline()
line_point = point.readline()
line_team = team.readline()

while line_driver_1:
    while line_point:
        while line_team:
            for i in range(1, 22):
                table.add_row([i, line_driver_1 + line_driver_2, line_team, line_point])
                line_driver_1 = driver_1.readline()
                line_driver_2 = driver_2.readline()
                line_point = point.readline()
                line_team = team.readline()
driver_1.close()
driver_2.close()
point.close()
team.close()

print(table)
