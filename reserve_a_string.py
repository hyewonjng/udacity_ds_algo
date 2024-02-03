def reverse_string(input):
    """
    Return reversed input string
    
    Examples:
       reverse_string("abc") returns "cba"
    
    Args:
      input(str): string to be reversed
    
    Returns:
      a string that is the reverse of input
    """

    if len(input)==0:
        return ""
    
    last_char = input[0]
    indexing = slice(1, None)
    recursive_input = input[indexing]
    
    return reverse_string(recursive_input) + last_char
    