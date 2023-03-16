def thousands_with_commas(i):
    
    str_number = str(i)
    # cast the number received to a string

    if len(str_number) <= 3:
        return str_number

    count = 0
    number_with_commas = ""
    
    for x in reversed(range(len(str_number))):
        # iterator that traverses in reverse order through the index of the digits of the str_number.
        if count == 3:
            number_with_commas = "," + number_with_commas
            count = 0
        number_with_commas = str_number[x] + number_with_commas
        # concatenate each digit of the number 'str_number' received by parameter to the string 'number_with_commas'.
        count += 1
        
    return number_with_commas