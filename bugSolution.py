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