from dayBank import DayBank
from auth import PBAuthentication
import datetime

if PBAuthentication().loginCheck():
    DayBank(date=datetime.datetime.now())

