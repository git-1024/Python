#!/usr/local/env python
# -*- coding: utf-8 -*-
import difflib

"""
'+'包含在第一个序列中，但不包含在第二个序列中
'-'包含在第二个序列中，但不包含在第一个序列中
' '两个序列一致
'?'标志两个序列存行在增量差异
'^'标志两个序列行存在差异字符
"""
text1 = """text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.7
add string
"""

text1_lines = text1.splitlines()	#以行进行分隔，以方便进行对比
text2 = """text2:
This module provides classes and functions for Comparing sequences.
including HTML and context and context and unified diffs.
difflib document v7.5"""

text2_lines = text2.splitlines()
d = difflib.Differ()
diff = d.compare(text1_lines,text2_lines)
print '\n'.join(list(diff))

