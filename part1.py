code_array = []  # array for temporary memory
sec_code = [8, 4, 6, 3, 3]  # security code array of 5 digits
locked = False  # lock logic holder
while True:  # run for unlimited number of times
    print("Enter the code")
    code = input()  # get the inputs from the user

    if (len(code) != 0):  # check if the input is not empty
        if (len(code) > 1):  # check if the code enter is only 1 digit
            code = 0  # if length of the input is greater than 1 digit make the code to 0 by default
            print("Please enter only one digit at a time")
        else:
            if (len(code_array) > 5):  # check if the code array length is more than 5
                code_array.pop(0)  # if more than 5 digits remove the first element
            code_array.append(int(code[0]))  # append the element to the array to the end

            # print(code_array)
            if (code_array[:-1] == sec_code):  # Check if the first 5 elements match the requried code

                if (code_array[-1] == 1 and locked):  # check if the last element if 1 or 4 for lock and unlock
                    locked = False # update the lock logic
                    print("Unlocked!!!!!!!")  # print the status of the system
                if (code_array[-1] == 4 and not locked):  # if the last digit is 4 lock the system
                    locked = True  # update the logic
                    print("Locked!!!!!!!")  # print the status of the system


