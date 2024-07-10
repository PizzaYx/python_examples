# FastAPi uvicorn 学习
# 1.从fastapi包里导入FastAPI类,用于构建API应用
from fastapi import FastAPI


# 2.实例化FastAPI对象
app = FastAPI()


# 3.定义API路由
@app.get("/")
async def root():
    return {"程序状态": "Hello World"}

# 4.运行API服务
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
