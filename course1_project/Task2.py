"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def logest_call(calls):
    # filter year in 2016
    calls_2016 = []
    for i in range(len(calls)):
        if calls[i][2] >= "01-01-2016":
            calls_2016.append(calls[i])


    # find longest call info
    logest_call = None
    
    for i in range(len(calls_2016)):
        if logest_call is None or calls_2016[i][3] > logest_call[3]:
            logest_call = calls_2016[i]
    
    res = f"{logest_call[0]} spent the longest time, {logest_call[3]} seconds, on the phone during September 2016."

    return print(res)

logest_call(calls)