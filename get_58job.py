#! /usr/bin/env python
'''
Created on 2019年8月9日

@author: zyh
'''

import bs4
import requests

from cutter import cut

# 初始化
s = requests.Session()
form_data = {
    'action': 'save',
    'from_domain': 'i',
    'isread': 'on',
    'lang': 'c'
}
form_data['loginname'] = input('username:')
form_data['password'] = input('password:')
# form_data['password'] = getpass('password:')
# 登陆取得cookies
url = 'https://login.51job.com/login.php'
r = s.post(url, form_data, cut('header'))


def write(n):
    url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25A8%258B%25E6%2597%25A0%25E5%25BF%25A7%2B-%25E4%25BB%25A3%25E6%258B%259B%25E8%2581%2598%2B-51Job%25E6%258B%259B%25E8%2581%2598%25E4%25BC%259A,1,' + n + '.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    r = s.get(url)
    content = r.content.decode('gbk')
    soup = bs4.BeautifulSoup(content, 'html.parser')
    content = soup.body.find_all('div', class_='el')[16:65]
    for x in content:
        with open('information', 'a')as fp:
            fp.write(str(x.text))
            fp.write('\n')


write('1')
write('2')
write('3')
# 访问目标

# 退出
s.close()
