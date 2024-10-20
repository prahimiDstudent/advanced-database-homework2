from fastapi import FastAPI

app = FastAPI()


# P1 - local variable function
async def P1() -> str:
    s1 = "I live in Khorramabad"
    return s1


# P2 - local variable function with print statement
async def P2() -> str:
    s2 = "I live in Khorramabad"
    print("inside function:", s2)
    return s2


# P3 - setting global variable inside async function
async def P3() -> str:
    global s3
    s3 = "I live in Khorramabad"
    print(s3)
    return s3


# P4 - another function with a local variable and print
async def P4() -> str:
    s4 = "I live in Khorramabad"
    print(s4)
    return s4


@app.get("/items/")
async def check_global_or_local_variable() -> dict:
    # Awaiting asynchronous functions
    p1 = await P1()
    p2 = await P2()
    p3 = await P3()
    p4 = await P4()

    # Printing values
    print("\nCan we read s2 here? No, it's a local variable.")

    # Printing s3 (global variable)
    print(f"Global variable s3 after P3 call: {s3}")

    # Returning response in dictionary format
    return {
        "p1": p1,
        "p2": p2,
        "p3": p3,
        "p4": p4
    }