def bleatrix_trotter(N):
    """
    Function that returns "INSOMNIA" if the digit received by parameter is equal to 0. 
    If the digit received by parameter is greater than zero the function will be executed until the sheep see all digits 0 to 9.

    For this last case: 
        -As long as the list does not reach 10 elements the process will be executed.
        -It will multiply and parse the number received by parameter(N) to a list(digits) 
         and it will ask if each element of the list is already found or not in what the sheep has already visualized.
        -If it is not found, it is added to the list of those seen.
        -When 10 elements are reached, the loop is exited and the last number seen by the sheep is returned.
    """

    if N == 0:
        return "INSOMNIA"

    seen_by_sheep = []
    # list about digits that the sheep seen

    i = 1
    while len(seen_by_sheep) < 10:
        number = N * i
        digits = [int(d) for d in str(number)]
        # creation of a list of integers from a number.
        for digit in digits:
            if digit not in seen_by_sheep:
                seen_by_sheep.append(digit)
        i += 1
    return number