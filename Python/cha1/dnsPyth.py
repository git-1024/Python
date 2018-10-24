#!/usr/local/env python
# -*- coding: utf-8 -*-

import dns.resolver

'''
dnspython是Python实现的一个DNS工具包，他支持几乎所有的记录类型，可以用来查询、传输并动态更新
ZONE信息，同事支持TSIG（事物签名）验证消息和EDNS0(拓展DNS)。在系统管理方面我们可以利用其查询功能来
实现服务监控以及解析结果的教养，可以代替nslookup及dig等工具，轻松做到与现有平台的整合
'''
print '实现A记录查询方法源码：'
domain = raw_input('Please input an domain: ')  #输入域名地址www.baidu.com
A = dns.resolver.query(domain, 'A')  #指定查询类型为A记录
for i in A.response.answer:
    for j in i.items:
        print j.address

print '\n'
print '实现MX记录查询方法源码'
domain = raw_input('Please input an domain: ')  #例如：163.com
MX = dns.resolver.query(domain, 'MX')  #指定查询类型为MX记录
for i in MX:
    print 'MX preference =', i.preference, 'mail exchanger =', i.exchange

print '\n'
print '实现NS记录查询方法源码'
domain = raw_input('Please input an domain: ')  #例如：baidu.com
ns = dns.resolver.query(domain, 'NS')  #指定查询类型为MX记录
for i in ns.response.answer:
    for j in i.items:
        print j.to_text()


print '\n'
print '实现NS记录查询方法源码'
domain = raw_input('Please input an domain: ')  #例如：baidu.com
cname = dns.resolver.query(domain, 'CNAME')  #指定查询类型为MX记录
for i in cname.response.answer:
    for j in i.items:
        print j.to_text()

