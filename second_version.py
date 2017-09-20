from datetime import *
from time import *
from datetime import date
from dateutil.relativedelta import relativedelta

class age():
    def isValidDate_Brith(self):
        while True:
            input_date_brith = raw_input('please enter brithday yyyy-mm-dd:')
            try:
                if strptime(input_date_brith,"%Y-%m-%d"):
                    t=strptime(input_date_brith,"%Y-%m-%d")
                    by, bm, bd = t[0:3]
                    brith_day = datetime(by, bm, bd)
                    return brith_day
                    break
            except ValueError:
                print "you enter wrong date,please inter again"

    def isValidDate_Check(self):
        while True:
            input_date_check = raw_input('please enter checkday yyyy-mm-dd:')
            try:
                if strptime(input_date_check,"%Y-%m-%d"):
                    t=strptime(input_date_check,"%Y-%m-%d")
                    cy, cm, cd = t[0:3]
                    check_day = datetime(cy,cm, cd)
                    return check_day
                    break
            except ValueError:
                print "you enter wrong date,please inter again"

    
    
    def countAge(self,check,brith):
        diff_day = (check- brith).days
        
        print "your baby age is: %s days"  %diff_day
        if diff_day < 0 :
            print "you enter wrong date"
        else:
            if diff_day <= 183:
                two_months = check + relativedelta(months=+2)
                print "next time to check: %s " %two_months
            if diff_day >183 and diff_day <548:
                three_months = check + relativedelta(months=+3)
                print "next time to check: %s " %three_months
            if diff_day >=548 and diff_day <730:
                six_months = check + relativedelta(months=+6)
                print "next time to check: %s " %six_months
            if diff_day >=730:
                one_year = check + relativedelta(months=+12)
                print "next time to check: %s " %one_year
"""

    def countAge(self,checkday,brithday):        
        diff_day = (checkday- brithday).days
        print diff_day
        if diff_day < 0 :
            print "you enter wrong date"
        else:
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
                
"""
p=age()
brith_date = p.isValidDate_Brith()
check_date = p.isValidDate_Check()
nextAge = p.countAge(check_date,brith_date)



