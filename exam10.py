from fastapi import FastAPI

app = FastAPI()


async def factorial(x:int=0) -> int:
    if x == 1: # This is the base case
        return 1
    else: # This is the recursive base
        return (x * await factorial(x-1))

@app.get("/items/")
async def Recursive_Function(number:str="0") -> dict:
    if not isinstance(number,str):
        raise TypeError("\n\n An ERROR occur...!!!")
    else:
        n = int(number)
        fact = await factorial(n)
        return {"result":fact}
