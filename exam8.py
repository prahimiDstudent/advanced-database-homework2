from fastapi import FastAPI, HTTPException

app = FastAPI()

def F1(number):
    max_digit = max(str(number))
    return int(max_digit)


def F2(number, max_digit):
    number_str = str(number)
    number_str = number_str.replace(str(max_digit), '', 1)
    return int(number_str) if number_str else 0


@app.get("/items/")
async def calculate_n(number: int) -> dict:
    if len(str(number)) != 5:
        raise HTTPException(status_code=400, detail="Please enter a 5-digit number.")

    max_digit = F1(number)
    final_number = F2(number, max_digit)

    return {"max-digit": max_digit, "final-number": final_number}