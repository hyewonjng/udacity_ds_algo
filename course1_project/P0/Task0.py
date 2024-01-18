"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from datetime import datetime

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    # text records in list
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# formatting str to datatime type
def datetime_formatting(datetime_info):
    return datetime.strptime(datetime_info, '%d-%m-%Y %H:%M:%S')
    

def first_text(texts):
    first_rec = None
    incoming_n = None
    answering_n = None
    timeToPrint = None 
    for i in range(len(texts)):
        time=datetime_formatting(texts[i][2])
        if first_rec is None or first_rec >= time:
            first_rec = time
            incoming_n = texts[i][0]
            answering_n = texts[i][1]
            timeToPrint = texts[i][2]
    
    return f"First record of texts, {incoming_n} texts {answering_n} at time {timeToPrint}"

def last_call(calls):
    last_rec = None
    incoming_n = None
    answering_n = None
    last_time = None
    during = None
    
    for i in range(len(calls)):
        time=datetime_formatting(calls[i][2])

        if last_rec is None or last_rec <= time:
            last_rec = time
            incoming_n = calls[i][0]
            answering_n = calls[i][1]
            last_time = calls[i][2]
            during = calls[i][3]

    return f"Last record of calls, {incoming_n} calls {answering_n} at time {last_time}, lasting {during} seconds"

print(first_text(texts))
print(last_call(calls))