#coding=utf8
import  logging

#app configure
#执行间隔
run_interval = 3 #seconds
#执行次数: <0:永不停止
run_times = 10

#执行命令:依次执行
commands = ["./test.sh",
            ]

pid_file = 'fuckcrontab.pid'

#log
log_logger_name = "fuckcrontab"
log_level = logging.DEBUG
log_format = '[%(asctime)s][%(levelname)s][%(filename)s:%(lineno)d]%(message)s'
log_date_format = '%Y-%m-%d %H:%M:%S'
log_file = 'fuckcrontab.log'
