# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 22:58:40 2020

@author: Admin
"""

import sys
#sys.path.append("D:\home\python364x64\Lib\site-packages")
#sys.path.append("D:\home\python364x64\Lib\site-packages\zcrm")
sys.path.append("D:\home\python364x86\Lib\site-packages")
sys.path.append("D:\home\python364x86\Lib\site-packages\zcrm")

import zcrmapi, aws_rds_sql #azuresql

from datetime import datetime, timedelta
deleted_since = datetime.strftime(datetime.now() - timedelta(5), '%Y-%m-%dT00:00:00+00:00')
#deleted_since = datetime.now() - timedelta(2)
#print(deleted_since)

### users ###
mylists = []
mylists = zcrmapi.get_api_users('all')
#print(mylists)
aws_rds_sql.sql_sync_users(mylists)

### Lead ### after 1/1/2018
mylists = []
mylists = zcrmapi.api_get_leads(False)
#print(mylists)
aws_rds_sql.sql_sync_leads(mylists)

### Contact ###
mylists = []
mylists = zcrmapi.api_get_contacts(False)
#print(mylists)
aws_rds_sql.sql_sync_contacts(mylists)

"""
### institutions ###
mylists = []
mylists = zcrmapi.api_get_institutions(False)
#print(mylists)
aws_rds_sql.sql_sync_institutions(mylists)

### programs ###
mylists = []
mylists = zcrmapi.api_get_programs(False)
#print(mylists)
aws_rds_sql.sql_sync_programs(mylists)

### applications ### 
mylists = []
myappprogram = []
mystagehistory = []
mylists, myappprogram, mystagehistory = zcrmapi.api_get_applications(False)
#print(myappprogram)
#print(mylists)
#print(mystagehistory)
aws_rds_sql.sql_sync_applications(mylists)
aws_rds_sql.sql_sync_app_program(myappprogram)
aws_rds_sql.sql_sync_app_stage_history(mystagehistory)

### Campaigns ###
mylists = []
mylists = zcrmapi.api_get_campaigns(False)
#print(mylists)
aws_rds_sql.sql_sync_campaigns(mylists)

### tasks ###
mylists = []
mylists = zcrmapi.api_get_tasks(False,False)
#print(mylists)
aws_rds_sql.sql_sync_tasks(mylists)

mylists = []
mylists.append(zcrmapi.api_get_deleted_records('Leads',deleted_since))
mylists.append(zcrmapi.api_get_deleted_records('Contacts',deleted_since))
mylists.append(zcrmapi.api_get_deleted_records('Vendors',deleted_since))
mylists.append(zcrmapi.api_get_deleted_records('Products',deleted_since))
mylists.append(zcrmapi.api_get_deleted_records('Deals',deleted_since))
mylists.append(zcrmapi.api_get_deleted_records('Tasks',deleted_since))
mylists.append(zcrmapi.api_get_deleted_records('Campaigns',deleted_since))
#print(mylists)
#print('after sql')
aws_rds_sql.sql_mark_deleted_records(mylists)
"""

aws_rds_sql.sql_close_conn()

last_run_datetime = datetime.strftime(datetime.now(), '%Y-%m-%dT00:00:00+00:00')
print(f'{last_run_datetime}')