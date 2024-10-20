from fastapi import FastAPI
from math import sqrt

app = FastAPI()

l = []

@app.get("/items/")
async def calculateN(n1: str = "0", n2: str = "0", n3: int = 0, n4: int = 0, n5: int = 0):
    try:
        n1, n2 = int(n1), int(n2)
    except ValueError:
        return {"error": "n1 and n2 must be valid integers"}

    l.clear()
    l.extend([n1, n2, n3, n4, n5])

    maximum = max(l)
    minimum = min(l)
    sum_values = sum(l)
    average = sum_values / len(l)

    N = len(l)
    mu = average
    variance_sum = sum((x - mu) ** 2 for x in l)
    variance = variance_sum / N
    standard_deviation = sqrt(variance)

    return {
        "Maximum": maximum,
        "Minimum": minimum,
        "Average": average,
        "Standard Deviation": standard_deviation
    }

@app.post("/items/{number:int}")
async def addNumber(number: int) -> dict:
    l.append(number)
    return {"updated_list": l}

@app.put("/items/put/")
async def putNumber(number: int = 0, index: int = 0) -> dict:
    if 0 <= index < len(l):

        l[index] = number
        return {"updated_list": l}
    else:
        return {"error": "Index out of range"}