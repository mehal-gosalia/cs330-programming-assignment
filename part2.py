import time
import random

code_array = []  # array for temporary memory
sec_code = []  # security code array of 5 digits
print("Please set your secret key")
y = input()  # get the secret key
for i in y:  # Create the sec_code array
    sec_code.append(int(i))

locked = True  # lock logic holder


def lock_mechanism(code):
    t_lock = locked

    if (len(code) != 0):  # check if the input is not empty
        if (len(code) > 1):  # check if the code enter is only 1 digit
            code = 0  # if length of the input is greater than 1 digit make the code to 0 by default
        else:
            if (len(code_array) > 5):  # check if the code array length is more than 5
                code_array.pop(0)  # if more than 5 digits remove the first element
            code_array.append(int(code[0]))  # append the element to the array to the end

            print(code_array)
            if (code_array[:-1] == sec_code):  # Check if the first 5 elements match the requried code

                if (code_array[-1] == 1 and t_lock):  # check if the last element if 1 or 4 for lock and unlock
                    t_lock = False  # update the lock logic

                if (code_array[-1] == 4 and not t_lock):  # if the last digit is 4 lock the system
                    t_lock = True  # update the logic

    return t_lock


def main():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Press enter to start ...")
    input()

    # record start time
    start = time.time()
    count = 0

    while True:
        count += 1
        digit = random.choice(digits)
        status = lock_mechanism(str(digit))
        if not status:
            # record end time
            break
    end = time.time()

    print("Number of iterations :", count)

    print("The time of execution of above program is :", (end - start) * 10 ** 3 / 1000, "s")


main()