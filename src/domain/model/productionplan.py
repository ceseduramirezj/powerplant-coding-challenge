class ProductionPlan:

    def __init__(self, powerplant_name: str, power_to_produce: float):
        self.powerplant_name = powerplant_name
        self.power_to_produce = power_to_produce

    def get_powerplant_name(self) -> str:
        return self.powerplant_name

    def get_power_to_produce(self) -> float:
        return self.power_to_produce
    
    def set_powerplant_name(self, powerplant_name: str):
        self.powerplant_name = powerplant_name

    def set_power_to_produce(self, power_to_produce: float):
        self.power_to_produce = power_to_produce

    