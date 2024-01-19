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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.



Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def call_from_bangalore(calls):
    # find phone number starting with (080)
    # add into list and remove duplicates
    phone_number_list = []

    for i in range(len(calls)):
        call_number_1 = calls[i][0]
        call_number_2 = calls[i][1]
        search_code_col1 = re.search("^\(080\)", call_number_1)
        search_code_col2 = re.search("^\(080\)", call_number_2)

        if search_code_col1:
            phone_number_list.append(call_number_1)
          
        if search_code_col2:
            phone_number_list.append(call_number_2)
    
    unique_phone_number = list(dict.fromkeys(phone_number_list))
    unique_phone_number.sort()
    
    heading = "The numbers called by people in Bangalore have codes: \n"

    if len(unique_phone_number) > 0:
        for i in range(0, len(unique_phone_number)-1):
            heading += unique_phone_number[i]
            heading += ', \n'
        heading += unique_phone_number[-1]
    
    return print(heading)
        

def number_of_bangalore(calls):
    # find phone number starting with (080)
    # add into list and remove duplicates
    phone_number_list = []

    for i in range(len(calls)):
        call_number_1 = calls[i][0]
        call_number_2 = calls[i][1]
        search_code_col1 = re.search("^\(080\)", call_number_1)
        search_code_col2 = re.search("^\(080\)", call_number_2)

        if search_code_col1:
            phone_number_list.append(call_number_1)
          
        if search_code_col2:
            phone_number_list.append(call_number_2)
    
    unique_phone_number = list(dict.fromkeys(phone_number_list))
    
    return len(unique_phone_number)

def rate_of_both_bangalore(calls):
    
    # check if 1st and 2nd columns begin with (080):
    both_080 = 0

    for i in range(len(calls)):
        call_number_1 = calls[i][0]
        call_number_2 = calls[i][1]
        search_code_col1 = re.search("^\(080\)", call_number_1)
        search_code_col2 = re.search("^\(080\)", call_number_2)

        if search_code_col1 and search_code_col2:
            both_080 += 1
    
    total_number = number_of_bangalore(calls)
    rate = round(both_080/total_number, 2)
    

    return print(f"{rate} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")