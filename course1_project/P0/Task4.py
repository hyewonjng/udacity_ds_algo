"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def send_text(texts):
    send_text_list = []
    for i in range(len(texts)):
        if texts[i][0] not in send_text_list:
            send_text_list.append(texts[i][0])
    
    return send_text_list

def receive_text(texts):
    receive_text_list = []
    for i in range(len(texts)):
        if texts[i][1] not in receive_text_list:
            receive_text_list.append(texts[i][0])
    
    return receive_text_list

def receive_call(calls):
    receive_call_list = []
    for i in range(len(calls)):
        if calls[i][1] not in receive_call_list:
            receive_call_list.append(calls[i][0])
    
    return receive_call_list

def tel_marketing(calls):
    tel_marketing_list = []

    sending_txt_list = send_text(texts)
    receiving_txt_list = receive_text(texts)
    receiving_call_list = receive_call(calls)

    for i in range(len(calls)):
        if calls[i][0] not in sending_txt_list and calls[i][0] not in receiving_txt_list and calls[i][0] not in receiving_call_list:
            tel_marketing_list.append(calls[i][0])

    tel_marketing_list = tel_marketing_list.sort()

    return tel_marketing_list

def listing_telemarketing(tel_marketing_list):
    heading = "These numbers could be telemarketers:\n"
    if len(tel_marketing_list) > 0:
        for i in range(0, len(tel_marketing_list)-1):
            heading += tel_marketing_list[i] 
            heading += '\n'
        heading += tel_marketing_list[-1]
    
    return heading