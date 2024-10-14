# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 解决跨域问题
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中，应该限定允许的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

@app.post("/api/chat")
async def chat(message: Message):
    # 简单模拟一个回复，可以替换为实际的聊天逻辑
    response_text = f"你说的是：{message.text}"
    return {"response": response_text}
