from bs4 import BeautifulSoup
import unittest


def make_head(soup):
    list_of_h = ["h1", "h2", "h3", "h4", "h5", "h6"]
    num = 0
    headers = []
    check = []
    for h in list_of_h:
        headers += soup.find_all(h)
        i = 0
    for head in headers:
        s = ''
        chlildrens = [e.name for e in head.children if e.name is not None]
        if len(chlildrens) == 0:
            s = head.contents
            check += s
        elif len(chlildrens) >= 1:
            tag = head.next
            while True:
                if len(tag.contents) != 0:
                    check += tag.contents
                    break
                tag = tag.find_next_sibling()

    for n in check:
        line = str(n)
        if line[0] in "ETC":
            num += 1
    return num


def links(soup):
    linkslen = 0
    for a in soup.find_all('a'):
        l_len = 0
        for s in a.find_next_siblings():
            if s.name != 'a':
                break
            else:
                list_par = list(s.parents)
                n = 0
                for par in list_par:
                    if par.name != 'a':
                        n += 1
                if len(list_par) == n:
                    l_len += 1
        if linkslen < l_len:
            linkslen = l_len
        a = a.find_next('a')
    return linkslen


def lists_n(soup):
    ul = soup.find_all('ul')
    ol = soup.find_all('ol')
    num = 0
    for u in ul:
        n = 0
        list_par = list(u.parents)
        for par in list_par:
            if par.name != 'ul' and par.name != 'ol':
                n += 1
        if len(list_par) == n:
            num += 1
    for o in ol:
        n = 0
        list_par = list(o.parents)
        for par in list_par:
            if par.name != 'ul' and par.name != 'ol':
                n += 1
        if len(list_par) == n:
            num += 1
    return num

def parse(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as fo:
        lines = fo.readlines()
    html = ''
    for line in lines:
        html += line
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find_all('div')
    div_bc = ''
    for i in divs:
        try:
            if i["id"] == "bodyContent":
                div_bc = i
        except KeyError:
            pass
    list_of_img = div_bc.find_all("img")
    imgs = 0
    for img in list_of_img:
        try:
            if int(img["width"]) >= 200:
                imgs += 1
        except KeyError:
            pass
    headers = make_head(div_bc)
    linkslen = links(div_bc) + 1
    lists = lists_n(div_bc)
    return [imgs, headers, linkslen, lists]


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),
            )

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    unittest.main()

