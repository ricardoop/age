from datetime import *
from time import *

class age():
    def isValidDate_Brith(self):
        while True:
            input_date_brith = raw_input('please inter brithday yyyy-mm-dd:')
            try:
                if strptime(input_date_brith,"%Y-%m-%d"):
                    t=strptime(input_date_brith,"%Y-%m-%d")
                    by, bm, bd = t[0:3]
                    brith_day = datetime(by, bm, bd)
                    return brith_day
                    break
            except ValueError:
                print "you inter wrong date,please inter again"

    def isValidDate_Check(self):
        while True:
            input_date_check = raw_input('please inter checkday yyyy-mm-dd:')
            try:
                if strptime(input_date_check,"%Y-%m-%d"):
                    t=strptime(input_date_check,"%Y-%m-%d")
                    cy, cm, cd = t[0:3]
                    check_day = datetime(cy,cm, cd)
                    return check_day
                    break
            except ValueError:
                print "you inter wrong date,please inter again"

    def countAge(self,brithday,checkday):
        while True:
            diff_day = (checkday - brithday).days
            print diff_day
            if diff_day > 0 :
                if diff_day<=14:
                    das = 30 - int(diff_day)
                    print datetime.now() + timedelta(days=das)
                if diff_day <= 45 and diff_day>14:
                    das = 60 - int(diff_day)
                    print datetime.now() + timedelta(days=das)
                if diff_day <= 90 and diff_day>45:
                    das = 120 - int(diff_day)
                    print datetime.now() + timedelta(days=das)
                if diff_day <= 150 and diff_day>90:
                    das = 180 - int(diff_day)
                    print datetime.now() + timedelta(days=das)
                if diff_day <= 240 and diff_day>150:
                    das = 270 - int(diff_day)
                    print datetime.now() + timedelta(days=das)
                if diff_day <= 300 and diff_day>240:
                    das = 365 - int(diff_day)
                    print datetime.now() + timedelta(days=das)
                if diff_day <= 390 and diff_day>300:
                    das = 450 - int(diff_day)
                    print datetime.now() + timedelta(days=das)
                if diff_day <= 480 and diff_day>390:
                    das = 540 - int(diff_day)
                    print datetime.now() + timedelta(days=das)
                if diff_day <= 570 and diff_day>480:
                    das = 730 - int(diff_day)
                    print datetime.now() + timedelta(days=das)
                    break
            else:
                print "you enter wrong date"
                isValidDate_Brith()
                isValidDate_Check()

p=age()
brith_date = p.isValidDate_Brith()
check_date = p.isValidDate_Check()
nextAge = p.countAge(check_date,brith_date)



