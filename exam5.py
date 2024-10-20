from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def print_pattern(n: int = 8):
    pattern = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, i + 1):
            row.append(i * j)
        pattern.append(row)
    return {"pattern": pattern}