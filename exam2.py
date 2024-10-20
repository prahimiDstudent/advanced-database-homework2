from fastapi import FastAPI
from decimal import Decimal, getcontext

getcontext().prec = 1000


app = FastAPI()

def Factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("\n\n An ERROR occurred...!!!")

    fact = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(2, n+1 , 1):
            fact *= i

    return fact

@app.get("/items/")
async def compute_expression(n:(int)=0):
    result = Decimal(0)
    sign = 1

    n1=int(n)
    for i in range(0, n1+1, 1):
        factorial_part = ((2 * i) + 3)

        divisor = Decimal(i + 2)
        constant = Decimal(9 - (2 * i))

        if divisor + constant == 0:
            #print(f"Skipping division by zero at term {i}")
            continue

        term = (Decimal(Factorial(factorial_part))) / (divisor + constant)

        result += sign * term

        sign *= -1

    return result