from fastapi import APIRouter, status

router = APIRouter(prefix="/laboratory", tags=["Laboratory"])


@router.post("/analysis", status_code=status.HTTP_201_CREATED)
async def order_laboratory_analysis():
    pass


@router.get("/analysis/{id}", status_code=status.HTTP_200_OK)
async def receive_analysis_result(id):
    pass


@router.patch("/analysis/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_analysis_info(id):
    pass
