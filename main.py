from fastapi import FastAPI
from src.infrastructure.inbound.router import ProductionPlanRouter

app: FastAPI = FastAPI()

production_plan_router: ProductionPlanRouter = ProductionPlanRouter()
app.include_router(production_plan_router.router)