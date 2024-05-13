import logging
import os
# 项目路径
prj_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path=os.path.join(prj_path,"data")
test_path=os.path.join(prj_path,"test")
test_case_path=os.path.join(prj_path,'test','case')
log_file=os.path.join(prj_path, 'log',"log.txt")
report_file=os.path.join(prj_path, 'report',"report.html")
data_file=os.path.join(prj_path,"data","test_user_data.xlsx")
test_list_file=os.path.join(prj_path,"test","test_list.txt")
test_fails_file=os.path.join(prj_path,"last_fails.pickle")
last_fails_file=os.path.join(prj_path,"last_fails.pickle")
# log文件配置
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(funcName)s, %(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=log_file,
    filemode='a',
)
# 数据库配置
db_host='127.0.0.1'
db_port=3306
db_user='root'
db_ps='root'
db='xzs'
# 邮件配置

smtp_server='smtp.qq.com'
smtp_user='2889229108@qq.com'
smtp_ps='rvpipnavhrrrdced'
sender=smtp_user
receiver='2889229108@qq.com'
subject='接口测试报告'
# 命令参数解析
paeser=OptionParser()
paeser.add_option("--collect-only",action="store_true",dest="collect_only",help="仅收集测试用例,不执行测试")
paeser.add_option("--makesuite-tag",action="store",dest="makesuite-tag",default="level1",help="根据标签生成测试套件")
paeser.add_option("--rerun-fails",dest="rerun-fails",action="store_true",help="重新运行失败的用例")
(options,args)=paeser.parse_args()
if __name__ == '__main__':
    logging.info("接口测试")