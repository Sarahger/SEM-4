from datetime import datetime
from dateutil.relativedelta import relativedelta

def date_difference(date1_str, date2_str):
    d1_parts = date1_str.split('-')
    d2_parts = date2_str.split('-')
    
    d1_int = [int(part) for part in d1_parts]
    d2_int = [int(part) for part in d2_parts]
    
    date1 = datetime(d1_int[2], d1_int[1], d1_int[0])
    date2 = datetime(d2_int[2], d2_int[1], d2_int[0])
    
    delta = relativedelta(date2, date1)
    print(f"Years difference: {delta.years}")

date1 = '01-08-2021'
date2 = '20-11-2022'
date_difference(date1, date2)
