#!/usr/local/env python
# -*- coding: utf-8 -*-

import psutil
import datetime


'''
psutil是一个跨平台库，能够轻松实现获取系统运行进程和系统利用率（包括CPU、内存、磁盘、网络等）
主要应用于系统监控、分析和限制系统资源及进程的管理
实现了同等命令行管理，如：ps,top,lsof,netstat,ifconfig,who,df,kill,free,nice,ionice,iostat,
iotop,uptime,pidof,tty,,taskset,pmap等
目前支持32和64位的Linux、Windows、OSX、FreeBSD、Sun Slorias等操作系统，支持从2.4到3.4
'''

print '\033[31m获取系统性能信息\033[0m'

print '	   CPU信息:'
print 'CPU完整信息:'
print psutil.cpu_times()
print '逻辑CPU完整信息:'
print psutil.cpu_times(percpu=True)
print '逻辑CPU的个数:'
print psutil.cpu_count()
print '物理CPU的个数:'
print psutil.cpu_count(logical=False)

print '\n'
print '	   内存信息:'
print '完整内存信息:'
mem = psutil.virtual_memory()
print mem
print '完整交换分区信息:'
print psutil.swap_memory()
print '当前系统内存和已使用的内存(单位:GB)'
print  mem.total/1024/1024
print  mem.used/1024/1024

print '\n'
print '获取磁盘的完整信息:'
print psutil.disk_partitions()
print '获取分区的使用情况:'
print psutil.disk_usage('/')

print '获取硬盘总的IO个数:'
print psutil.disk_io_counters()
print '获取单个分区的IO个数:'
print psutil.disk_io_counters(perdisk=True)

print '\n'
print '	    网络信息:'
print '获取网络总的IO信息'
print psutil.net_io_counters()
print '输出每个网口的IO信息:'
print psutil.net_io_counters(pernic=True)


print '\n'
print '	    其他系统信息:'
print '获取当前登录系统用户的信息:'
print psutil.users()
print '获取开机时间:'
print psutil.boot_time()
print '转换成自然时间格式:'
print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

print '\n'
print psutil.pids()
p = psutil.Process(1)
print '实例化一个Process对象，参数为一个进程号:'
print p
print '进程名：'
print p.name
print '进程bin路径：'
print p.exe()
print '进程工作的绝对路径：'
print p.cwd()
print '进程工作状态：'
print p.status()
print '进程创建的时间,时间戳格式：'
print p.create_time()
print '进程的UID信息:'
print p.uids()
print '进程的GID信息:'
print p.gids()
print '进程的CPU时间信息，包括user/system两个CPU时间信息:'
print p.cpu_times()
print 'get进程CPU时间亲和度，如要设置CPU亲和度、将CPU号作为参数即可:'
print p.cpu_affinity()
print '进程内存利用率:'
print p.memory_percent()
print '进程内存rss、vms信息:'
print p.memory_info()
print '进程IO信息，包括读写IO数及字节数:'
print p.io_counters()
print '返回打开进程socket的namedutples列表,包括fs,family,laddr等信息:'
print p.connections()
print '进程开启的线程:'
print p.num_threads()
print ':'

print '\n'
print 'psutil提供popen类的作用是获取用户启动的应用进程信息，以便跟踪程序进程的运行状态'

from subprocess import PIPE

p = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"], stdout=PIPE)
print p
print p.name()
print p.username()
print p.communicate()
print p.cpu_times()
