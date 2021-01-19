# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 20:08:48 2021

@author: phoen
"""

import sys
sys.path.append("../aas_zohocrm_repo/aas_package")

try:
    from .handlers import handler
    from .zcrmapi import zcrmapi
    from .aws_rds_mysql import aws_rds_mysql
except ImportError:
    from handlers import handler
    from zcrmapi import zcrmapi
    from aws_rds_mysql import aws_rds_mysql