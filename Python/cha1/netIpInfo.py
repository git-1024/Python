#!/usr/local/env python
# -*- coding: utf-8 -*-

from IPy import IP

print 'IPv类型:'
print IP('10.0.0.0/8').version()
ip = IP('192.168.1.0/24')
print 'IP网段个数:'
print ip.len()

for x in ip:
    print(x)
ip = IP('192.168.1.20')
print '反向解析地址:'
print ip.reverseNames()
print '私网类型举例：'
print ip.iptype()
print '公网类型举例：'
print IP('8.8.8.8').iptype()
print '换成整形格式：'
print IP('8.8.8.8').int()
print '换成整形格式：'
print IP('8.8.8.8').strHex()
print '换成整形格式：'
print IP('8.8.8.8').strBin()
print '十六进制转换为IP格式：'
print (IP(0x8080808))

print '\n'
print 'IP方法也支持网络地址转换，例如根据IP雨掩码生产网段格式：'
print (IP('192.168.1.0').make_net('255.255.255.0'))
print (IP('192.168.1.0/255.255.255.0', make_net=True))
print (IP('192.168.1.0-192.168.1.255', make_net=True))
print '使用strNormal方法指定不同wantprefixlen参数值以定制不同输出类型的网段'
print IP('192.168.1.0/24').strNormal(0)
print IP('192.168.1.0/24').strNormal(1)
print IP('192.168.1.0/24').strNormal(2)
print IP('192.168.1.0/24').strNormal(3)

print '\n'
print IP('10.0.0.0/24') < IP('12.0.0.0/24')
print 'IP包含关系'
print IP('192.168.1.0/24') in IP('192.168.0.0/16')
print '判断两个网段是否重复:返回1代表重叠，0代表不重叠'
print IP('192.168.0.0/23').overlaps('192.168.1.0/24')
print IP('192.168.1.0/23').overlaps('192.168.2.0/24')
