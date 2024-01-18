"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


# iterate each column and clean the phone number data into a format
# remove spance, parenthesis OR just take digits

def take_digit_from_calls(calls, texts):
    phone_numbers = []
    for i in range(len(calls)):
        # remove space or/and parenthesis
        phone_numbers.append(re.sub("\(|\)| ","", calls[i][0]))
        phone_numbers.append(re.sub("\(|\)| ","", calls[i][1]))

    for i in range(len(texts)):
        phone_numbers.append(re.sub("\(|\)| ","", texts[i][0]))
        phone_numbers.append(re.sub("\(|\)| ","", texts[i][0]))

    unique_numbers = set(phone_numbers)

    return len(list(unique_numbers))


take_digit_from_calls(calls, texts)