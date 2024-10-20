from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def print_All_4_Digits(n1:(str)=0 , n2:(str)=0) -> dict:
    if not isinstance(n1,str) or not isinstance(n2,str):
        raise TypeError("\n\n An ERROR occur...!!!")
    else:
        l = list()
        p1 = 0
        p2 = 0
        l2 = list()
        n1_str = int(n1)
        n2_str = int(n2)
        for i in range(n1_str, n2_str , 1):
            l = list(str(i))
            p1 = int(int(l[len(str(i)) - 1]) + int(l[len(str(i)) - 2]))
            p2 = int(int(l[0]) * int(l[1]))
            if p1 == p2:
                l2.append(str(i))
            else:
                continue
        return {"key": l2}