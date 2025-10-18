from fastapi import APIRouter
from ..services.gpio import get_gpio, ACTIVE, INACTIVE

router = APIRouter()

@router.get("/on/{number}")
async def turnon(number: int):
  with get_gpio(number) as led:
    led.set_value(number, ACTIVE)
 
  return {"status": "ok", "ok": True}


@router.get("/off/{number}")
async def turnoff(number: int):
  with get_gpio(number) as led:
    led.set_value(number, INACTIVE)
 
  return {"status": "ok", "ok": True}


