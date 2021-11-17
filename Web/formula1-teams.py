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
PFAD = 'en/results.html/2021/team.html'
s = requests.session()

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
           'Host': URL,
           'Referer': URL + PFAD
           }

s.post(URL, headers=HEADERS)

soup = bs(s.get(URL + PFAD).text, 'html.parser')

name = soup.find_all('a', class_='dark bold uppercase ArchiveLink')
a = str(name)

points = soup.find_all('td', class_='dark bold')
b = str(points)

char = '<>'
for x in range(len(char)):
    a = a.replace(char[x], '\n')
for x in range(len(char)):
    b = b.replace(char[x], '\n')

    
f = open("../Source Files/Teams.txt", 'w+')
f.truncate()
f.write(a)
f.close()
del_line("../Source Files/Teams.txt")


f = open("../Source Files/Pts.txt", 'w+')
f.truncate()
f.write(b)
f.close()
del_line("../Source Files/Pts.txt") 

Team = open("../Source Files/Teams.txt", 'r')
Points = open("../Source Files/Pts.txt", 'r')

table = prettytable.PrettyTable(["Position", "Team", "Points"])

line_team = Team.readline()
line_points = Points.readline()

while line_team:
    while line_points:
        for i in range(1, 11):
            table.add_row([i, line_team, line_points])
            line_team = Team.readline()
            line_points = Points.readline()

Team.close()
Points.close()

print(table)
