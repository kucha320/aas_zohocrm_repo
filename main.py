# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 18:06:16 2021

@author: phoen
"""

import os
from dotenv import load_dotenv,find_dotenv
from aas_package import *

if __name__ == "__main__":
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

    refresh_token= os.getenv("ZCRM_REFRESHTOKEN")
    user_identifier= os.getenv("ZCRM_USEREMAIL")    
    
    h = handlers.handler(config,refresh_token,user_identifier)
    h.sync_records()    
    #a.sync_app_checklist()