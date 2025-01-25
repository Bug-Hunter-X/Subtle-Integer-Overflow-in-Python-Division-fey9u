# Subtle Integer Overflow in Python Division

This repository demonstrates a subtle integer overflow bug in Python that can occur when dividing very large integers.

## Problem Description

The `function_with_uncommon_error` function attempts to handle division by zero and type errors. However, it doesn't explicitly handle the potential for integer overflow when dividing very large integers.

If the integers `a` and `b` are large enough, their division may result in an overflow that leads to an incorrect result without raising an exception.

## Bug

The `bug.py` file contains the code that demonstrates the integer overflow error:

```python
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
```

## Solution

The `bugSolution.py` file provides a solution that uses the `decimal` module to handle arbitrary-precision decimal arithmetic, preventing the integer overflow:

```python
from decimal import Decimal

def function_with_uncommon_error_solution(a, b):
    try:
        a = Decimal(str(a))
        b = Decimal(str(b))
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid input types"

print(function_with_uncommon_error_solution(2**63, 2**62))
```