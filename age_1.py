import time
import datetime
def age():
    def isValidDate(self,date):
        brithday_date = raw_input('please inter brithday yyyy-mm-dd:')
        try:
            while True:
                 t = time.strptime(brithday_date, "%Y-%m-%d")
                 y, m, d = t[0:3]
                 now_day = datetime.datetime(y, m, d)
        except:
            print "you inter wrong date"




    check_time = raw_input('inter check date yyyy-mm-dd:')
    ct = time.strptime(check_time, "%Y-%m-%d")
    cy, cm, cd = ct[0:3]
    check_day = datetime.datetime(cy,cm,cd)
    a=time.gmtime()
    dd=a[2]-d
    dm=a[1]-m
    dy=a[0]-y

    if dd<0:
        dd=dd+30
        dm=dm-1

        if dm<0:
            dm=dm+12
            dy=dy-1
    if dm<0:
        dm=dm+12
        dy=dy-1
    print dy,dm,dd
    diff_day = (check_day - now_day).days
    print  diff_day

    if diff_day<=14:
        das = 30 - int(diff_day)
        print datetime.datetime.now() + datetime.timedelta(days=das)
    if diff_day <= 45 and diff_day>14:
        das = 60 - int(diff_day)
        print datetime.datetime.now() + datetime.timedelta(days=das)
    if diff_day <= 90 and diff_day>45:
        das = 120 - int(diff_day)
        print datetime.datetime.now() + datetime.timedelta(days=das)
    if diff_day <= 150 and diff_day>90:
        das = 180 - int(diff_day)
        print datetime.datetime.now() + datetime.timedelta(days=das)
    if diff_day <= 240 and diff_day>150:
        das = 270 - int(diff_day)
        print datetime.datetime.now() + datetime.timedelta(days=das)
    if diff_day <= 300 and diff_day>240:
        das = 365 - int(diff_day)
        print datetime.datetime.now() + datetime.timedelta(days=das)
    if diff_day <= 390 and diff_day>300:
        das = 450 - int(diff_day)
        print datetime.datetime.now() + datetime.timedelta(days=das)
    if diff_day <= 480 and diff_day>390:
        das = 540 - int(diff_day)
        print datetime.datetime.now() + datetime.timedelta(days=das)
    if diff_day <= 570 and diff_day>480:
        das = 730 - int(diff_day)
        print datetime.datetime.now() + datetime.timedelta(days=das)

age()
