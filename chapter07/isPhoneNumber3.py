#coding=utf-8

import re

#贪心和非贪心匹配
#python默认为贪心的，如果要非贪心的，在结束的花括号后跟一个问号
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())