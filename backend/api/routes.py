from fastapi import APIRouter

from backend.model.spin_result import SpinResult
from backend.services.spin_service import SpinService

router = APIRouter()
spin_service = SpinService()

@router.get("/spin", response_model=SpinResult)
def spin():
    return spin_service.spin()