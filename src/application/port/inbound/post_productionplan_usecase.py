from abc import ABC, abstractmethod

from src.domain.model import Fuels, PowerPlant, ProductionPlan

class PostProductionPlanUseCase(ABC):

    @abstractmethod
    def create_production_plan(self, load_demand: int, fuels: Fuels, power_plants: list[PowerPlant]) -> list[ProductionPlan]:
        """ Create a production plan based on the load demand, fuel prices and available power plants. """