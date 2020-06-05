#coding=utf-8
#用正则表达式匹配更多模式

import re

#利用括号分组
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('第一组:' + mo.group(1))
print('第二组:' + mo.group(2))
print('第零组方法1:' + mo.group(0))
print('第零组方法2:' + mo.group())

#一次获取所有分组
areaCode, mainNumber = mo.groups()
print('areaCode:' + areaCode)
print('mainNumber:' + mainNumber)

#文本中匹配括号，使用反斜杠进行字符转义
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print('第一组:' + mo.group(1))
print('第二组:' + mo.group(2))

#用管道匹配多个分组
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

#用管道匹配Bat开始的任意一个
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

#用问号实现可选匹配

#用星号匹配零次或多次

#用加号匹配一次或多次

#用花括号匹配特定次数
