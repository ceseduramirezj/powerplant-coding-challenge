from typing import List

from fastapi import APIRouter, Depends, Body

from src.config.dependencies import get_post_productionplan_usecase
from src.application.port.inbound import PostProductionPlanUseCase
from src.infrastructure.inbound.router.dto import ProductionPlanDto, FuelsDto, PowerPlantDto
from src.domain.model import Fuels, PowerPlant, ProductionPlan

class ProductionPlanRouter:

    def __init__(self):
        self.router = APIRouter(tags=["ProductionPlan"])
        self.router.post("/productionplan")(self.post_productionplan)

    def post_productionplan(
            self, 
            usecase: PostProductionPlanUseCase = Depends(get_post_productionplan_usecase),
            load: int = Body(...), 
            fuels: FuelsDto = Body(...), 
            powerplants: List[PowerPlantDto] = Body(...) 
    ) -> List[ProductionPlanDto]:

        fuels_model = Fuels(
            gas_euro_per_MWh=fuels.get_gas(),
            kerosine_euro_per_MWh=fuels.get_kerosine(),
            wind_percentage=fuels.get_wind()
        )

        powerplant_models = [
            PowerPlant(
                name=pp.get_name(),
                type=pp.get_type(),
                efficiency=pp.get_efficiency(),
                min_power_production=pp.get_pmin(),
                max_power_production=pp.get_pmax()
            ) for pp in powerplants
        ]

        production_plan_list: list[ProductionPlan] = usecase.create_production_plan(load, fuels_model, powerplant_models)

        return [ProductionPlanDto(
            name=pp.get_powerplant_name(),
            p=pp.get_power_to_produce()
        ) for pp in production_plan_list]