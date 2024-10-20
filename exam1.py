from fastapi import FastAPI

app = FastAPI()

result = list();

@app.get("/items/")
async def print_even_separated(number:(int)=0) -> dict:
    if not isinstance(number,int):
        raise TypeError("\n\n invalid inputs...!!!");
    else:
        num_str = str(number)

        for i in num_str:
            if int(i) % 2 == 0:
                result.append(i);
            else:
                continue;

        #print("\n\n your output is : ",'*'.join(result));
        return {"key":'*'.join(result)}

@app.post("/add/{number:int}")
async def addNumbers(number:(int)=0) -> dict:
    if not isinstance(number,int):
        raise TypeError("\n\n an ERROR occur...!!!")
    else:
        result.append(number)
        return {"key":str(result)}

@app.put("/put/{number:int}")
async def putNumbers(number:(int)=0 , index:(int)=0) -> dict:
    if not isinstance(number,int) or not isinstance(index,int):
        raise Exception("\n\n An ERROR Occur...!!!")
    else:
        result[index] = number;
        return {"key":str(result)}

@app.delete("/delete/{number:int}")
async def deleteNumber(number:(int)=0) -> dict:
    if not isinstance(number,int):
        raise TypeError("\n\n An ERROR Occur...!!!")
    else:
        result.remove(number)
        return {"key":str(result)}