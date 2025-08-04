from src.application.port.inbound import PostProductionPlanUseCase
from src.application.services import ProductionPlanService

def get_post_productionplan_usecase() -> PostProductionPlanUseCase:
    return ProductionPlanService()
