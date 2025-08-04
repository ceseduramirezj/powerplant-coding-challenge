from pydantic import BaseModel, Field

class FuelsDto(BaseModel):

    gas: float = Field(..., alias="gas(euro/MWh)")
    kerosine: float = Field(..., alias="kerosine(euro/MWh)")
    co2: float = Field(..., alias="co2(euro/ton)")
    wind: float = Field(..., alias="wind(%)")

    def get_gas(self) -> float:
        return self.gas
    
    def get_kerosine(self) -> float:
        return self.kerosine
    
    def get_co2(self) -> float:
        return self.co2
    
    def get_wind(self) -> float:
        return self.wind
    
    def set_gas(self, gas: float):
        self.gas = gas

    def set_kerosine(self, kerosine: float):
        self.kerosine = kerosine

    def set_co2(self, co2: float):
        self.co2 = co2

    def set_wind(self, wind: float):
        self.wind = wind