#!/usr/bin/env python
import sys
import os
import time
import datetime
import logging

import daemon
import conf


def DoJob():
    logging.info("********************** start job! *********************")
    logging.info('*%s                         *', str(datetime.datetime.now()))
    logging.info("*******************************************************")

    try:
        for command in conf.commands:
            logging.info(os.popen(command, 'r').read())
    except Exception, e:
        logging.error(e)

    logging.info("******************* job finished! *********************")
    logging.info('*%s                         *', str(datetime.datetime.now()))
    logging.info("*******************************************************")



class App(daemon.Daemon):
    def usage(self):
        print __file__ + ' test|start|stop'
        print 'test: no daemon, run once, output log to stdout'
        print 'start: start job'
        print 'stop: exit job'

    def run(self):
        run_count = 0

        while True:
            if conf.run_times > 0 and run_count >= conf.run_times :
                break

            DoJob()
            run_count += 1
            time.sleep(conf.run_interval)



if __name__ == '__main__':
    app = App(conf.pid_file)

    if len(sys.argv) < 2:
        app.usage()
    elif sys.argv[1] == 'test':
        logging.basicConfig(level= conf.log_level,
            format= conf.log_format,
            datefmt= conf.log_date_format)
        DoJob()
    else:
        logging.basicConfig(level= conf.log_level,
            format= conf.log_format,
            datefmt= conf.log_date_format,
            filename= conf.log_file,
            filemode='w')
        if sys.argv[1] == 'start':
            app.start()
        elif sys.argv[1] == 'stop':
            app.stop()
        else:
            print("Invalid commond.")
