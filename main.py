import os
from src import exercise_1, exercise_2, exercise_3

while True:
    print("\n")
    print("Menu:")
    print("1. Execute exercise 1")
    print("2. Execute exercise 2")
    print("3. Execute exercise 3")
    print("4. Execute exercise 4")
    print("5. Exit")

    option = int(input("Choose an option: "))

    if option == 1:
        assert exercise_1.thousands_with_commas(1234) == '1,234'
        print("Correctly placed commas")
        assert exercise_1.thousands_with_commas(123456789) == '123,456,789'
        print("Correctly placed commas")
        assert exercise_1.thousands_with_commas(12) == '12'
        print("Correctly placed commas")

    elif option == 2:
        print(exercise_2.annograms("train"))
        print('--')
        print(exercise_2.annograms('drive'))
        print('--')
        print(exercise_2.annograms('python'))

    elif option == 3:
        folder_path = os.path.abspath("resources")
        file_name = "c-input.in"
        file_path = os.path.join(folder_path, file_name)
        
        try:
            with open(file_path, "r") as input_file:
                # open the input file
                T = int(input_file.readline())
                # first line (number of test cases)
                for i in range(T):
                    # loop the test file
                    N = int(input_file.readline())
                    # read the next line
                    result = exercise_3.bleatrix_trotter(N)
                    print("Case #{}: {}".format(i+1, result))
                    # print output
        except:
            print("Something else went wrong")
            raise Exception("Please, check if your WORD.lst file exists ;)")

    elif option == 4:
        print("     To view this exercise please go to the path:")
        print("     test-DE-winclap/src/exercise_4.ipynb")
        print("     If you have Jupiter Notebook or Lab installed open it there, if not open it in your visual studio code.")
        print("     Thank you :)")

    elif option == 5:
        print("Exiting...")
        break
    else:
        print("Invalid option. Please try again.")