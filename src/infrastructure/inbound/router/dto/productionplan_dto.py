from pydantic import BaseModel

class ProductionPlanDto(BaseModel):
    name: str
    p: float

    def get_name(self) -> str:
        return self.name

    def get_p(self) -> float:
        return self.p
    
    def set_name(self, name: str):
        self.name = name

    def set_p(self, p: float):
        self.p = p