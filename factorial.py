"""
this file computes factorial
"""
import time

final_list = []

def factorial(number_:int):
    """
    this function computes factorial for one number
    """
    time.sleep(.1)
    res = 1
    for i in range (1,number_+1):
        res = res * i
    return res

def sum_factorial():
    """
    this function computes sum of factorials
    """
    for i in range(50):

        final_list.append(factorial(i)) 

    result=sum(final_list)

    print(f"Final SUM is = {result}")

    return result

if __name__ == "__main__":

    sum_factorial()
