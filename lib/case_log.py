import json
from config.config import *
def log_case_info(case_name,url,args,exp,r):
    if isinstance(args,dict):
        args=json.dumps(args,ensure_ascii=False)
    logging.info("��������:{}".format(case_name))
    logging.info("url:{}".format(url))
    logging.info("�������:{}".format(args))
    logging.info("�������:{}".format(exp))
    logging.info("ʵ�ʽ��:{}".format(r))