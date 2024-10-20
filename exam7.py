from fastapi import FastAPI
from math import sqrt

app = FastAPI()

numbers_list = []


async def Max1(l: list) -> int:
    if not isinstance(l, list):
        raise Exception("\n\n An ERROR occurred...!!!")
    else:
        maximum = int(l[0])
        for i in range(1, len(l) , 1):
            if int(l[i]) > maximum:
                maximum = int(l[i])
        return maximum


async def Min1(l: list) -> int:
    if not isinstance(l, list):
        raise TypeError("\n\n An ERROR occurred...!!!")
    else:
        minimum = int(l[0])
        for i in range(1, len(l) , 1):
            if int(l[i]) < minimum:
                minimum = int(l[i])
        return minimum


async def Ave1(l: list) -> float:
    if not isinstance(l, list):
        raise TypeError("\n\n An ERROR occurred...!!!")
    else:
        total_sum=0
        for i in range(0 , len(l) , 1):
            total_sum += int(l[i])
        length = len(l)
        return total_sum / length


async def STD1(l: list) -> float:
    if not isinstance(l, list):
        raise Exception("\n\n An ERROR occurred...!!!")
    else:
        length = len(l)
        average = await Ave1(l)

        sumation = 0
        for i in range(0 , len(l) , 1):
            sumation += ((int(l[i]))-average)**2
        variance = sumation / length
        return sqrt(variance)


@app.get("/items/")
async def calculate_some_functions(n1: int = 0, n2: int = 0, n3: int = 0, n4: int = 0, n5: int = 0) -> dict:
    if not all(isinstance(i, int) for i in [n1, n2, n3, n4, n5]):
        raise TypeError("\n\n Please enter valid integer numbers...!!!")
    else:
        numbers_list.clear()
        numbers_list.extend([n1, n2, n3, n4, n5])

        maximum_number = await Max1(numbers_list)
        minimum_number = await Min1(numbers_list)
        average = await Ave1(numbers_list)
        standard_deviation = await STD1(numbers_list)

        return {
            "maximum": maximum_number,
            "minimum": minimum_number,
            "average": average,
            "standard_deviation": standard_deviation
        }