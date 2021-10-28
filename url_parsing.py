import urllib.request
import urllib.parse
import re
# no run  I'm trying to automate web scraping on SEC / EDGAR financial reports
# url = 'http://pythonprogramming.net/'
# urlf = 'http://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231.htm'
# urln = 'https://www.israelnationalnews.com/'
#
# values = {'s': 'basics',
#           'submit' : 'search'}
#
# data = urllib.parsee.urlencode(values)
# data = data.encode('utf-8')
# req = urllib.request.Request(urlf, data)
# resp = urllib.request.urlopen(req)
# respData = resp.read()
#
# print(respData)

# test_url = 'https://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231.htm'
# data = str(get_data(test_url))
# list_data = data.split('/s/')
#
# for i in range(3, len(list_data)):
#     alpa = list_data[i].split('</p></td>')  # (1, 4)
#     # alpa = list_data[i].split('</span>') # (2)
#     # alpa = list_data[i].split('</td>') # (3)
#     ##print(alpa)
#     ##print(alpa[1])
#     ##print(alpa[2])
#     beta = alpa[2].split(';">')  # (1,4,3,)
#     # beta = alpa[2].split('%">') # (2)
#     print(alpa[0], '-->', beta[len(beta) - 1])

# test_url = 'https://www.sec.gov/Archives/edgar/data/1770787/000177078721000009/txg-20201231.htm'
# data = str(get_data(test_url))
# list_data = data.split('/s/')
# for i in range(3, len(list_data)):
#     #alpa = list_data[i].split('</p></td>') # (1, 4)
#     alpa = list_data[i].split('</span>') # (2)
#     #alpa = list_data[i].split('</td>') # (3)
#     #beta = alpa[2].split(';">') #(1,4,3,)
#     beta = alpa[1].split('%">') # (2)
#     print(alpa[0], '-->', beta[len(beta) - 1])


# test_url = 'https://www.sec.gov/Archives/edgar/data/1427925/000143774921006074/acrx20201231_10k.htm'
# data = str(get_data(test_url))
# list_data = data.split('/s/')
# for i in range(3, len(list_data)):
#     #alpa = list_data[i].split('</p></td>') # (1, 4)
#     #alpa = list_data[i].split('</span>') # (2)
#     alpa = list_data[i].split('</td>') # (3)
#     beta = alpa[2].split(';">') #(1,4,3,)
#    # beta = alpa[2].split('%">') # (2)
#     print(alpa[0], '-->', beta[len(beta) - 1])

import requests


# test_url = 'https://www.sec.gov/Archives/edgar/data/3662/0000950170-98-000413.txt'


def get_data(link):
    hdr = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36'}

    req = requests.get(link, headers=hdr)
    content = req.content

    return content


def parse_name_title_p_td(test_url):
    try:
        data = str(get_data(test_url))
        list_data = data.split('/s/')
        for i in range(3, len(list_data)):
            alpha = list_data[i].split('</p></td>')  # (1, 4)
            beta = alpha[2].split(';">')  # (1,4,3,)
            print(alpha[0].replace('&#xa0;', ''), '-->', beta[len(beta) - 1].replace('&#xa0;', ''))
    except:
        return False
    else:
        return True


def parse_name_title_span(test_url):
    try:
        data = str(get_data(test_url))
        list_data = data.split('/s/')
        for i in range(3, len(list_data)):
            alpha = list_data[i].split('</span>')  # (2)
            beta = alpha[1].split('%">')  # (2)
            print(alpha[0].replace('&#xa0;', ''), '-->', beta[len(beta) - 1].replace('&#xa0;', ''))
    except:
        return False
    else:
        return True


def parse_name_title_td(test_url):
    try:
        data = str(get_data(test_url))
        list_data = data.split('/s/')
        for i in range(3, len(list_data)):
            alpha = list_data[i].split('</td>')  # (3)
            beta = alpha[2].split(';">')  # (1,4,3,)
            print(alpha[0].replace('&#xa0;', ''), '-->', beta[len(beta) - 1].replace('&#xa0;', ''))
    except:
        return False
    else:
        return True


test_url_p_td = 'https://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231.htm'
test_url_span = 'https://www.sec.gov/Archives/edgar/data/1770787/000177078721000009/txg-20201231.htm'
test_url_td = 'https://www.sec.gov/Archives/edgar/data/1427925/000143774921006074/acrx20201231_10k.htm'

test = [test_url_p_td, test_url_span, test_url_td]


def get_company_name(url_link):
    return url_link.split('/')[-1]



def parse_name(test_url):
    if parse_name_title_p_td(test_url):
        return
    if parse_name_title_span(test_url):
        return
    if parse_name_title_td(test_url):
        return
    print(test_url, "Can't be parse")


for link in test:
    print(get_company_name(link))
    parse_name(link)
    print()

# parse_name_title_p_td(test_url_p_td)
# print('*****')
#
# parse_name_title_span(test_url_span)
# print('*****')
#
# parse_name_title_td(test_url_td)
