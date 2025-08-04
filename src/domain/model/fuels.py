class Fuels:

    def __init__(self, gas_euro_per_MWh: float, kerosine_euro_per_MWh: float, wind_percentage: float):
        self.gas_euro_per_MWh = gas_euro_per_MWh
        self.kerosine_euro_per_MWh = kerosine_euro_per_MWh
        self.wind_percentage = wind_percentage

    def get_gas_euro_per_MWh(self) -> float:
        return self.gas_euro_per_MWh

    def get_kerosine_euro_per_MWh(self) -> float:
        return self.kerosine_euro_per_MWh

    def get_wind_percentage(self) -> float:
        return self.wind_percentage

    def set_gas_euro_per_MWh(self, gas_euro_per_MWh: float):
        self.gas_euro_per_MWh = gas_euro_per_MWh

    def set_kerosine_euro_per_MWh(self, kerosine_euro_per_MWh: float):
        self.kerosine_euro_per_MWh = kerosine_euro_per_MWh

    def set_wind_percentage(self, wind_percentage: float):
        self.wind_percentage = wind_percentage