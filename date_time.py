#!/usr/bin/env LearnPythonNotes

# ----------- Import Packages, and/or Modules: Classes, & Functions -----------
#from datetime import datetime
from datetime import date
import datetime
import time as t
import pytz

# --------------------------- Function Definitions ----------------------------
# Test
def calc_age(dob: int):
    print(type(dob))
    dob = int(dob)
    return datetime.date.today().year - dob

# Returns timestamp in this form '2016-11-16T14:31:18.130822-08:00'
# Requires import datetime, pytz
def time_stamp():
	utc_now = pytz.utc.localize(datetime.datetime.utcnow())
	pst_now = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))
    #return utc_now.isoformat()
	return pst_now.isoformat()

def main():
    print(f"---------- Current Timestamp => {time_stamp()} -----------")
    gvr = datetime.datetime(1970,12, 25)
    dtf ="{:%A, %B %d, %Y}"
    today = date.today()
    str_date = "01/14/1974"
    print(gvr)
    print(dtf.format(gvr))
    print(f"Today\'s date: {today}")
    print(f"Current date and time: {datetime.datetime.now()}")
    print(f"Day of the week Mon = 0: {date.weekday(today)}")
    print(datetime.datetime.strptime(str_date, "%m/%d/%Y"))

    print(date.today()) # datetime.date(2018, 11, 19)
    print(date.today().day) # 19
    print(date.today().year) # 2018
    print(date.today().month) # 11

    # Calculate date ranges
    start_date = date(1970,12, 25)
    end_date = date(2018, 11, 19)
    delta = end_date - start_date
    yr_since_birth = (end_date - start_date).days / 365
    print(f"Days since my birth: {delta.days}")
    print(f"Years since my birth: {(delta.days)/365}")
    print(f"{int(yr_since_birth)}")

    sam_dob = date(2001, 12, 25)
    td = date.today()
    sam_age = int((td - sam_dob).days / 365)
    print(f"Sam's age: {sam_age}")
    print(f"Sam's age: {(date.today() - date(2001, 12, 25)).days / 365}")

    # Time manipulation
    #print(tiempo.tzinfo)
    #print(tiempo.tzname())
    print(datetime.date(2001, 12, 25))
    ##print(tiempo.hour)

    print(f"Time: {t.time()}")
    print(f"Time Clock: {t.clock()}")
    # Time since Wed Dec 31 16:00:00 1969'
    # Or t.ctime(1) since Wed Dec 31 16:00:01 1969'
    print(f"Current time: {t.ctime()}")

    start_time = t.strftime("%b %d %Y %H:%M:%S", t.gmtime(t.time()))
    print(f"Started at {start_time}")
    st = t.time()
    for i in range(1,5,1):
        t.sleep(5)

    et = t.time()
    lapse = et - st
    lapse_time = t.strftime("%H:%M:%S", t.gmtime(lapse))
    print(f"Lapse time: {lapse_time}")
    end_time = t.gmtime(t.time())
    end_time = t.strftime("%b %d %Y %H:%M:%S", end_time)
    print(f"Ended at {end_time}")

    resp = input("Year of Birth (yyyy): ")
    print(calc_age(resp))

# Application entry point
if __name__ == '__main__':
    main()
