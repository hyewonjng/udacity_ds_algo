def get_alphabet(number):
    return chr(number+96) # 97 == 'a'

def all_codes(number):
    if number == 0:
        return [""]
    
############ CASE I ################    
    remainder = number % 10 # last
    alphabet = get_alphabet(remainder) # last digit char
    output_10 = all_codes(number // 10) # front digits except for the last
    
    for index, element in enumerate(output_10):
        output_10[index] = element + alphabet
    
    
############ CASE II ################        
    
    remainder = number % 100 # last 2 digits, i.e., 23
    output_100 = list()
    
    if remainder <= 26 and number > 9 :
        alphabet = get_alphabet(remainder) # 23 (w)
        output_100 = all_codes(number // 100) # front digit, i.e., 1
        
        for index, element in enumerate(output_100):
            output_100[index] = element + alphabet
    
    output = list()
    output.extend(output_100)
    output.extend(output_10)
    
    return output