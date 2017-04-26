#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
info = {
    'zhangsan':500,
    'lisi':600,
    'zhaowu':700
}
b = {
    'lisi':789,
    1:2,
    3:4
}
'''
print(type(info))
print(info)
print(info['lisi'])
info['lisi'] = '李四'
print(info)
info['wangwu'] = '王五'
print(info)
del info['zhaowu']
print(info)
print(info.get('lili'))
print('lili' in info)

info.setdefault('lisi',{456})
print(info)

info.update(b)
'''
A = info.items()
A = info.fromkeys([7,8,9])

print(A)