# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Reference
Go to Zoho Developer Console to generate the grant token
Developer Console : https://github.com/zoho/zcrm-python-sdk
Application : Self Client
Scope : AAAServer.profile.read,ZohoCRM.Modules.ALL,ZohoCRM.Users.Read
Grant permission Zoho CRM API Access Setup --> Users and Control --> Security Control 

https://github.com/zoho/zcrm-python-sdk
"""
import sys
sys.path.append("D:\home\env\Lib\site-packages")
#sys.path.append("C:\Python27\Lib\site-packages")
#sys.path.append("D:\home\site\wwwroot\env\Lib\site-packages")

import os
from dotenv import load_dotenv,find_dotenv

from pathlib import Path
home = str(Path().cwd())

#print(home)

envars = find_dotenv()
#print(envars)
load_dotenv(envars,verbose=True,override=True)
applicationLogFilePath = os.getenv("ZCRM_LOGFILEPATH")
#print(applicationLogFilePath)

import zcrmsdk
from zcrmsdk import ZCRMRestClient, ZohoOAuth, ZCRMRecord

def ZCRMConnection():
    config = {
        "client_id": os.getenv("ZCRM_CLIENTID"),
        "client_secret": os.getenv("ZCRM_CLIENTSECRET"),
        "apiBaseUrl":"https://www.zohoapis.com",
        "apiVersion":"v2",
        "currentUserEmail": os.getenv("ZCRM_USEREMAIL"),
        #multi-user authentication : threading.current_thread().setattr('current_user_email','user@email.com')
        "sandbox":"False",
        "applicationLogFilePath": os.getenv("ZCRM_LOGFILEPATH"),
        #"applicationLogFilePath": "D:\home\env\zcrm_log\log",
        "redirect_uri":"http://localhost:8000/some_path",
        "accounts_url":"https://accounts.zoho.com",
        #"token_persistence_path":".",
        "token_persistence_path": os.getenv("ZCRM_TOKENPERSISTENCEPATH"),
        #"token_persistence_path": "D:\home\env\zcrm_log",
        "access_type":"online",
        #Use the below keys for MySQL DB persistence
        "mysql_username":"",
        "mysql_password":"",
        "mysql_port":"3306",
        #Use the below keys for custom DB persistence
        "persistence_handler_class" : "Custom",
        "persistence_handler_path": os.getenv("ZCRM_PERSISTENCEHANDLERPATH")
        #"persistence_handler_path": "D:\home\env\zcrm_log\CustomPersistance.py"
        }
        
    zcrmsdk.ZCRMRestClient.initialize(config)

    """
    #generate access tokens from grant_token 
    oauth_client = zcrmsdk.ZohoOAuth.get_client_instance()
    grant_token = "1000.e056d54e5b377ae9d96678d9aebbc6ce.47241630ae10ec4ef46da5a3c0906dc8"
    oauth_tokens = oauth_client.generate_access_token(grant_token)
    """
    #generate access tokents from refresh token
    oauth_client = zcrmsdk.ZohoOAuth.get_client_instance()
    refresh_token= os.getenv("ZCRM_REFRESHTOKEN")
    user_identifier= os.getenv("ZCRM_USEREMAIL")
    oauth_tokens = oauth_client.generate_access_token_from_refresh_token(refresh_token,user_identifier)
    
    #print(oauth_tokens)

"""
# test connection
ZCRMConnection()
record = ZCRMRecord.get_instance('Leads', 1068421000000123005) #3719520000000276035 is Invoices ID
resp = record.get()
print(resp.data.field_data)
"""

"""
module_ins = zcrmsdk.ZCRMModule.get_instance('Leads')
#lead_response = lead_record_instance.get()
lead_response = module_ins.search_records_by_criteria('(Email:equals:mywong.1173@gmail.com)')
print(lead_response)
"""

"""
#record = ZCRMRecord.get_instance('Leads', 1068421000000123005) #3719520000000276035 is Invoices ID
#resp = record.get()
#print(resp.data.field_data)
module_ins = zcrmsdk.ZCRMModule.get_instance('leads')
resp = module_ins.search_records_by_email('chushoumeizi@gmail.com')
record_ins_arr = resp.data
for record_ins in record_ins_arr:
    print(record_ins.field_data)
#print(resp.data.get_field_value('id'))
"""

#resp = module_ins.search_records_by_criteria('(Office:equals:Macau)')
#print(resp.status_code)
#resp_info = resp.info
#print(resp_info.count)
#print(resp_info.page)
#print(resp_info.per_page)
#print(resp_info.is_more_records)
#record_ins_arr = resp.data
#for record_ins in record_ins_arr:
#    print(record_ins.field_data)
#    print("\n\n")

"""
#def get_records(self):
try:
    module_ins = zcrmsdk.ZCRMModule.get_instance('Leads')  # module API Name
    resp = module_ins.get_records()
    print(resp.status_code)
    record_ins_arr = resp.data
    importleads = []
    i = 0
    for record_ins in record_ins_arr:
        #resp_r = record_ins.get_relatedlist_records('Campaigns')
        print(record_ins.entity_id)
        print(record_ins.owner.name)
        print(record_ins.created_by.name)
        print(record_ins.modified_by.name)
        print(record_ins.created_time)
        print(record_ins.modified_time)
        record_ins_data = record_ins.field_data
        #for key in product_data:
        #    print(key + ":" + str(product_data[key]))

        #print(record_ins.field_data)
        if 'First_Name' in record_ins_data:
            print(record_ins.field_data['First_Name'])
        print(record_ins.field_data['Last_Name'])
        print(record_ins.get_field_value('Sources'))
        if 'Campaign' in record_ins_data:
            print(record_ins.field_data['Campaign']['name'])

        print("\n\n")
        i = i + 1
        #print(record_ins.field_data)
    
    print(i)
except zcrmsdk.ZCRMException as ex:
    print(ex.status_code)
    print(ex.error_message)
    print(ex.error_code)
    print(ex.error_details)
    print(ex.error_content)
"""
"""
#def get_record(self):
try:
    record = ZCRMRecord.get_instance('Leads',1068421000018416989) #3719520000000276035 is Invoices ID
    resp_1 = record.get().data.field_data
    if 'Campaign' in resp_1:
        print(record.get().data.field_data['Campaign']['name'])
    resp = record.get_relatedlist_records('Campaigns')  # related list API Name
    print(resp.status_code)
    record_ins_arr = resp.data
    for record_ins in record_ins_arr:

        print(record_ins.get_field_value('Campaign_Name'))

        print(record_ins.field_data)
        print("\n\n")
except ZCRMException as ex:
    print(ex.status_code)
    print(ex.error_message)
    print(ex.error_code)
    print(ex.error_details)
    print(ex.error_content)
"""