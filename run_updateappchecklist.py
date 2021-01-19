# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 12:59:19 2020

@author: Admin
"""

import sys
#sys.path.append("D:\home\python364x64\Lib\site-packages")
#sys.path.append("D:\home\python364x64\Lib\site-packages\zcrm")
sys.path.append("D:\home\python364x86\Lib\site-packages")
sys.path.append("D:\home\python364x86\Lib\site-packages\zcrm")

import zcrmapi

### Update app checklist ###
mylists = []
mylists = zcrmapi.api_get_tasks(False,True)
#print(mylists)
zcrmapi.api_update_app_checklist(mylists)