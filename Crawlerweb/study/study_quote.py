#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from urllib.parse import quote

if __name__ == '__main__':
    # quote 示例
    # 这个方法是 urllib.parse 中专门为我们提供的 URL 转码的方法，我们还是拿上面一个示例的中文进行转码
    print(quote("极客挖掘机"))
