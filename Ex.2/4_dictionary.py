def factorials(n:int):
    if n < 0:
        raise ValueError("Input should be  a non-negative number. ")
    
    result_dict = {}
    factorial_value = 1
    
    for i in range(1, n+1):
        factorial_value *= i
        result_dict[i] = factorial_value
        
    return result_dict


n = factorials(5)
print(n[1])
print(n[3])
print(n[5])

"""
n = 5
factorials_dict = factorials(n)
print(factorials_dict)"""