import os

def annograms(word):
    """
    Function that goes through the list getting every word that was in the source file 
    and compares if the length is equal to the word received by parameter and also if it is different from each other.

    Order each word in ascending order and if everything matches, it is an annogram. 

    Appended it to the new list. At the end return it.
    """
    
    folder_path = os.path.abspath("resources")
    file_name = "WORD.lst"
    file_path = os.path.join(folder_path, file_name)

    try:
        words = [w.rstrip() for w in open(file_path)]
        # line taken from the example given in the test.
        # line of code that loads a list of words from a text file by removing any extra whitespace at the end of the line
    except:
        print("Something else went wrong")
        raise Exception("Please, check if your WORD.lst file exists ;)")
    
    annograms_list = []

    for w in words:
        if len(w) == len(word) and w != word:
            if sorted(w) == sorted(word):
                annograms_list.append(w)
    
    return annograms_list