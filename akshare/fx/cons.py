# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Author: Albert King
date: 2019/10/20 10:58
contact: jindaxiang@163.com
desc: 
"""
# headers
SHORT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
}
# url
FX_SPOT_URL = "http://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/rfx-sp-quot.json"
FX_SWAP_URL = "http://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/rfx-sw-quot.json"
FX_PAIR_URL = "http://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/cpair-quot.json"
# payload
SPOT_PAYLOAD = {
    "t": {}
}
