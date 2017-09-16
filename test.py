import datetime
import time

def isValidDate():
    while True:
        brithday_date = raw_input('please inter brithday yyyy-mm-dd:')
        try:
            if time.strptime(brithday_date,"%Y-%m-%d"):
                t=time.strptime(brithday_date,"%Y-%m-%d")
                y, m, d = t[0:3]
                now_day = datetime.datetime(y, m, d)
                print now_day
                break
        except ValueError:
            print "you inter wrong date,please inter again"

isValidDate()


