# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 16:58:05 2021

@author: phoen
"""

from datetime import datetime, timedelta
try:
    from .zcrmapi import zcrmapi
    from .aws_rds_mysql import aws_rds_mysql
except ImportError:
    from zcrmapi import zcrmapi
    from aws_rds_mysql import aws_rds_mysql
    
class handler():
    def config_zcrmapi(self,config,refresh_token,user_identifier):
        self.zcrmapi = zcrmapi(config,refresh_token,user_identifier)
    
    def config_mysql(self,server, database, username, password):
        self.aws_rds_mysql = aws_rds_mysql(server, database, username, password)
    
    def sync_users(self):    
        ## users ###
        mylists = []
        mylists = self.zcrmapi.get_api_users('all')
        #print(mylists)
        self.aws_rds_mysql.sql_sync_users(mylists)

    def sync_leads(self):         
        # ## Lead ### after 1/1/2018
        mylists = []
        mylists = self.zcrmapi.api_get_leads(False)
        #print(mylists)
        self.aws_rds_mysql.sql_sync_leads(mylists)
    
    def sync_contacts(self): 
        ### Contact ###
        mylists = []
        mylists = self.zcrmapi.api_get_contacts(False)
        #print(mylists)
        self.aws_rds_mysql.sql_sync_contacts(mylists)
        
    def sync_institutions(self): 
        ### institutions ###
        mylists = []
        mylists = self.zcrmapi.api_get_institutions(False)
        #print(mylists)
        self.aws_rds_mysql.sql_sync_institutions(mylists)
    
    def sync_programs(self): 
        ### programs ###
        mylists = []
        mylists = self.zcrmapi.api_get_programs(False)
        #print(mylists)
        self.aws_rds_mysql.sql_sync_programs(mylists)

    def sync_applications(self):         
        ### applications ### 
        mylists = []
        myappprogram = []
        mystagehistory = []
        mylists, myappprogram, mystagehistory = self.zcrmapi.api_get_applications(False)
        #print(myappprogram)#print(mylists)
        #print(mystagehistory)
        self.aws_rds_mysql.sql_sync_applications(mylists)
        self.aws_rds_mysql.sql_sync_app_program(myappprogram)
        self.aws_rds_mysql.sql_sync_app_stage_history(mystagehistory)

    def sync_campaigns(self):         
        ### Campaigns ###
        mylists = []
        mylists = self.zcrmapi.api_get_campaigns(False)
        #print(mylists)
        self.aws_rds_mysql.sql_sync_campaigns(mylists)
    
    def sync_tasks(self): 
        ### tasks ###
        mylists = []
        mylists = self.zcrmapi.api_get_tasks(False,False)
        #print(mylists)
        self.aws_rds_mysql.sql_sync_tasks(mylists)
        
    def sync_deleted_records(self):     
        deleted_since = datetime.strftime(datetime.now() - timedelta(5), '%Y-%m-%dT00:00:00+00:00')
        #deleted_since = datetime.now() - timedelta(2)
        #print(deleted_since)
        mylists = []
        mylists.append(self.zcrmapi.api_get_deleted_records('Leads',deleted_since))
        mylists.append(self.zcrmapi.api_get_deleted_records('Contacts',deleted_since))
        mylists.append(self.zcrmapi.api_get_deleted_records('Vendors',deleted_since))
        mylists.append(self.zcrmapi.api_get_deleted_records('Products',deleted_since))
        mylists.append(self.zcrmapi.api_get_deleted_records('Deals',deleted_since))
        mylists.append(self.zcrmapi.api_get_deleted_records('Tasks',deleted_since))
        mylists.append(self.zcrmapi.api_get_deleted_records('Campaigns',deleted_since))
        #print(mylists)
        #print('after sql')
        self.aws_rds_mysql.sql_mark_deleted_records(mylists)
    
    def close_mysql(self):
        self.aws_rds_mysql.sql_close_conn()
    
    def sync_app_checklist(self):
        ### Update app checklist ###
        mylists = []
        mylists = self.zcrmapi.api_get_tasks(False,True)
        #print(mylists)
        self.zcrmapi.api_update_app_checklist(mylists)
    
