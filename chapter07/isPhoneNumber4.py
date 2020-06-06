#coding=utf-8

import re

#findall()方法测试
#返回一组字符串，包含被查找字符串中的所有匹配
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')           #没有分组，返回字符串列表
phoneNumList = phoneNumRegex.findall('Cell:415-555-9999 work:215-555-0000')
print(phoneNumList)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')     #有分组，返回元组列表
phoneNumTuple = phoneNumRegex.findall('Cell:415-555-9999 work:215-555-0000')
print(phoneNumTuple)
