from pydantic import BaseModel

class PowerPlantDto(BaseModel):
    name: str
    type: str
    efficiency: float
    pmin: int
    pmax: int

    def get_name(self) -> str:
        return self.name
    
    def get_type(self) -> str:
        return self.type

    def get_efficiency(self) -> float:
        return self.efficiency
    
    def get_pmin(self) -> int:
        return self.pmin
    
    def get_pmax(self) -> int:
        return self.pmax
    
    def set_name(self, name: str):
        self.name = name

    def set_type(self, type: str):
        self.type = type

    def set_efficiency(self, efficiency: float):
        self.efficiency = efficiency

    def set_pmin(self, pmin: int):
        self.pmin = pmin
    
    def set_pmax(self, pmax: int):
        self.pmax = pmax