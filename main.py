from typing import Union

from fastapi import FastAPI

# Fast API 객체 생성
app = FastAPI()

# localhost:8000/
@app.get("/")
def read_root():
    print
    return {"Hello": "fastapi"}

# 단축키: ctrl + . : 모듈 자동 임폴트 기능

# 경로 매개변수
# localhost:8000/itmes/1
# localhost:8000/itmes/2
# localhost:8000/itmes/aaa

# 쿼리 매개변수 : q: Union[str, None]=None)
# http://127.0.0.1:8000/items/111?q="헬로"
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    print("헬로",item_id,q)
    # 비즈니스로직 처리
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)


#fastapi 서비스 실행
# uvicorn main:app [--port=8000] --reload