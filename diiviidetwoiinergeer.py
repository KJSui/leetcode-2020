def divide3(dividend, divisor):
    a = abs(dividend)
    b = abs(divisor)

    res = 0
    while a >= b:
        c = 0
        while a >= b<<c:
            a - = b<<c
            res += 1<<c
            c += 1
        

    return -res if (dividend > 0) ^ (divisor > 0) else res