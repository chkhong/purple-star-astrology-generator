from fastapi import APIRouter

router = APIRouter(prefix='/users')

@router.get('/')
async def hello():
  return {"router": "users"}