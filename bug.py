def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid input types"

# Uncommon error:  a subtle integer overflow that may lead to unexpected results 
# If a and b are very large integers, their division may result in an overflow error.
# This error can be difficult to detect because it may not immediately crash the program. 
# Instead, it may produce an incorrect result.
print(function_with_uncommon_error(2**63 ,2**62)) # May lead to overflow