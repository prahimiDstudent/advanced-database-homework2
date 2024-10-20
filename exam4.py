from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def print_all_3_digits_numbers(n1:(str)="0" , n2:(str)="0") -> dict:
    if not isinstance(n1,str) or not isinstance(n2,str):
        raise TypeError("\n\n An ERROR occur...!!!")
    else:
        n1_str = int(n1)
        n2_str = int(n2)
        l = list();
        for i in range(n1_str , n2_str , 1):
            number = str(i)
            if (all(int(digits) %2 == 0 for digits in number)):
                l.append(str(i))
            else:
                continue
        return {"key":l}