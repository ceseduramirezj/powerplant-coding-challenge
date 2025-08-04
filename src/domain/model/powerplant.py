class PowerPlant:

    def __init__(self, name: str, type: str, efficiency: float,  min_power_production: int, max_power_production: int):
        self.name = name
        self.type = type
        self.efficiency = efficiency
        self.min_power_production = min_power_production
        self.max_power_production = max_power_production

    def get_name(self) -> str:
        return self.name
    
    def get_type(self) -> str:
        return self.type

    def get_efficiency(self) -> float:
        return self.efficiency
    
    def get_min_power_production(self) -> int:
        return self.min_power_production
    
    def get_max_power_production(self) -> int:
        return self.max_power_production
    
    def set_name(self, name: str):
        self.name = name

    def set_type(self, type: str):
        self.type = type

    def set_efficiency(self, efficiency: float):
        self.efficiency = efficiency

    def set_min_power_production(self, min_power_production: int):
        self.min_power_production = min_power_production

    def set_max_power_production(self, max_power_production: int):
        self.max_power_production = max_power_production