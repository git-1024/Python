#!/use/local/env python
# -*- coding: utf-8 -*-

import pexpect
import sys

set timeout=60

child = pexpect.spawn('ssh root@192.168.43.166')
fout = file('/wnh/Python/mylog.txt','w')
child.logfile = fout

child.expect("password:")
child.sendline("root1234")
child.expect('#')
child.expect('df -h')
child.expect('#')
child.expect('ls /home')
