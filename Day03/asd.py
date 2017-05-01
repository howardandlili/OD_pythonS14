#!/user/bin/env python
# -*- coding:utf-8 -*-
show_list = ({'www.baidu.com': [{'maxconn': '3000',
                                'weight': '20',
                                'name': '100.1.7.11',
                                'server': '100.1.7.11'}],
             'www.oldboy.org': [{'maxconn': '3000',
                                 'weight': '20',
                                 'name': '100.1.7.10',
                                 'server': '100.1.7.10'}]},
            ['www.oldboy.org', 'www.baidu.com'])
backend_all_dict = {'www.baidu.com': [{'maxconn': '3000',
                                'weight': '20',
                                'name': '100.1.7.11',
                                'server': '100.1.7.11'}],
             'www.oldboy.org': [{'maxconn': '3000',
                                 'weight': '20',
                                 'name': '100.1.7.10',
                                 'server': '100.1.7.10'}]}
backend_list = ['www.oldboy.org', 'www.baidu.com']
backend_show_dict = {'2': 'www.baidu.com', '1': 'www.oldboy.org'}

backend_all_dict['www.hy.com'] = [{'maxconn': '3000',
                                'weight': '20',
                                'name': '100.1.7.12',
                                'server': '100.1.7.12'}]
print(backend_all_dict)