import requests
from bs4 import BeautifulSoup as bs 
import prettytable
import linecache


def cut(word):
    return [char for char in word]
  

def del_line(fn):
    f = open(fn)
    output = []
    for line in f:
        if not line.startswith('['):
            if not line.startswith(']'):
                if not line.startswith('/'):
                    if not line.startswith('span'):
                        if not line.startswith(' '):
                            if not line.startswith('fas'):
                                if line.strip():
                                    output.append(line)
    f.close()
    f = open(fn, 'w')
    f.writelines(output)
    f.close()

    
URL = "https://www.fanfiktion.de/"
LOGIN = "?a=l"

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
           'Origin': URL,
           'Referer': URL + LOGIN}

s = requests.session()

u = s.get(URL).cookies['u']

login_payload = {
    'u': u,
    'nickname': 'simonthies01',
    'passwd': " PUT THE PASSWORD HERE "
}

login_req = s.post(URL + LOGIN, headers=HEADERS, data=login_payload)

cookies = login_req.cookies

soup = bs(s.get(URL + 'stats').text, 'html.parser')


view = soup.find_all(attrs={'data-ff-sort-colname': 'hits'})
views_1 = str(cut(view[1]).pop())
views_2 = str(cut(view[2]).pop())

kap = soup.find_all(attrs={'data-ff-sort-colname': 'chaptercount'})
kap_1 = str(cut(kap[1]).pop())
kap_2 = str(cut(kap[2]).pop())

words = soup.find_all(attrs={'data-ff-sort-colname': 'storylen'})
words_1 = str(cut(words[1]).pop())
words_2 = str(cut(words[2]).pop())

rev = soup.find_all(attrs={'data-ff-sort-colname': 'reviewcount'})
rev_1 = cut(rev[1])
rev_1_1 = rev_1.pop()
rev_2 = cut(rev[2])
rev_2_2 = rev_2.pop()

empf = soup.find_all(attrs={'data-ff-sort-colname': 'recommendationcount'})
empf_1 = cut(empf[1])
empf_1_1 = empf_1.pop()
empf_2 = cut(empf[2])
empf_2_2 = empf_2.pop()

fav = soup.find_all(attrs={'data-ff-sort-colname': 'favcount'})
fav_1 = cut(fav[1])
fav_1_1 = fav_1.pop()
fav_2 = cut(fav[2])
fav_2_2 = fav_2.pop()

stats_1 = soup.find_all('span', class_='fas fa-coffee titled-icon')
s_1 = str(stats_1)

stats_2 = soup.find_all('span', class_='fas fa-unlink titled-icon')
s_2 = str(stats_2)

chars = '<>"'
for x in range(len(chars)):
    s_1 = s_1.replace(chars[x], '\n')
    s_2 = s_2.replace(chars[x], '\n')

    
st = open("../Source Files/Stats.md", 'w+')
st.truncate()
st.write(s_1)
st.write(s_2)
st.close()
del_line("../Source Files/Stats.md")

table = prettytable.PrettyTable(['Name', 'Chapter', 'Words', 'Reviews', 'Reccomendations', 'Views', 'Favourites', 'Status'])

sta = open("../Source Files/Stats.md", 'r')

table.add_row(['Eragon und Arya', kap_1, words_1, str(cut(rev_1_1).pop()), str(empf_1_1), views_1, str(cut(fav_1_1).pop()), linecache.getline("../Source Files/Stats.md", 1)])

table.add_row(['Eragon Eine neue Ära', kap_2, words_2, str(cut(rev_2_2).pop()), str(empf_2_2), views_2, str(cut(fav_2_2).pop()), linecache.getline("../Source Files/Stats.md", 2)])

print(table)
