from src.application.port.inbound.post_productionplan_usecase import PostProductionPlanUseCase
from src.domain.model import Fuels, PowerPlant, ProductionPlan
from src.domain.constants.powerplant_types import GASFIRED, TURBOJET, WINDTURBINE

class ProductionPlanService(PostProductionPlanUseCase):

    def __get_min_power_to_produce__(self, power_plant: PowerPlant, fuels: Fuels) -> float:
        power_to_produce: float = power_plant.get_min_power_production()
        if power_plant.get_type() == WINDTURBINE:
            power_to_produce = (fuels.get_wind_percentage() / 100) * power_plant.get_min_power_production()
        return round(power_to_produce, 1) 

    def __get_max_power_to_produce__(self, power_plant: PowerPlant, fuels: Fuels) -> float:
        power_to_produce: float = power_plant.get_max_power_production()
        if power_plant.get_type() == WINDTURBINE:
            power_to_produce = (fuels.get_wind_percentage() / 100) * power_plant.get_max_power_production()
        return round(power_to_produce, 1)

    def create_production_plan(self, load_demand: int, fuels: Fuels, power_plants: list[PowerPlant]) -> list[ProductionPlan]:

        power_plant_cost_per_MWh: dict[str, float] = {}

        for power_plant in power_plants:

            cost_per_MWh: float = None

            if power_plant.get_type() == GASFIRED:
                cost_per_MWh = fuels.get_gas_euro_per_MWh() / power_plant.get_efficiency()

            elif power_plant.get_type() == TURBOJET:
                cost_per_MWh = fuels.get_kerosine_euro_per_MWh() / power_plant.get_efficiency()

            elif power_plant.get_type() == WINDTURBINE:
                cost_per_MWh = 0.0

            else:
                raise ValueError(f"Unknown power plant type: {power_plant.get_type()}")
            
            power_plant_cost_per_MWh[power_plant.get_name()] = cost_per_MWh

        sorted_power_plant_cost_per_MWh: dict[str, float] = dict(sorted(power_plant_cost_per_MWh.items(), key=lambda item: item[1]))

        sorted_power_plants_by_cost: list[PowerPlant] = sorted(power_plants, key=lambda power_plant: list(sorted_power_plant_cost_per_MWh.keys()).index(power_plant.get_name()))

        load: int = 0

        production_plan_list: list[ProductionPlan] = []

        for i, power_plant in enumerate(sorted_power_plants_by_cost):

            next_power_plant = sorted_power_plants_by_cost[i + 1] if i + 1 < len(sorted_power_plants_by_cost) else None
            
            power_to_produce: float = self.__get_max_power_to_produce__(power_plant, fuels)

            # Adjust power to produce if load demand is exceeded in total
            if load + power_to_produce > load_demand:

                power_to_produce = load_demand - load if load_demand - load >= power_plant.get_min_power_production() else 0.0

            # Adjust power to prevent not reaching the minimum power production of the next power plant, this way we ensure reaching load demand
            elif next_power_plant and load + power_to_produce + self.__get_min_power_to_produce__(next_power_plant, fuels) > load_demand:

                adjusted_power_to_produce: float = load_demand - load - self.__get_min_power_to_produce__(next_power_plant, fuels)
                power_to_produce = adjusted_power_to_produce if adjusted_power_to_produce >= power_plant.get_min_power_production() else 0.0 

            load += power_to_produce

            production_plan_list.append(ProductionPlan(powerplant_name=power_plant.get_name(), power_to_produce=power_to_produce))

        return production_plan_list
