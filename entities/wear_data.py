from dataclasses import dataclass
import math


@dataclass
class WearData:
    """Хранение данных для вычилений (первое окно)"""

    # 1
    after_test: float = 0
    before_test: float = 0
    wear: float = 0
    # 2
    radius: float = 0
    width: float = 0
    blunting: float = 0
    # 3
    frequency: float = 0
    time_test: float = 0
    operating_time: float = 0
    # 4
    max_speed: float = 0
    resource: float = 0
    # 5
    ratio: float = 0

    def calculate_wear(self):
        self.wear = self.before_test - self.after_test
        return self.wear

    def calculate_blunting(self):
        self.blunting = 2 * self.radius / self.width * 100
        return self.blunting

    def calculate_operating_time(self):
        self.operating_time = math.pi * self.frequency * self.time_test * (self.after_test + self.before_test) / 2000
        return self.operating_time

    def calculate_resource(self):
        self.resource = self.operating_time / (60 * self.max_speed)
        return self.resource

    def calculate_ratio(self):
        self.ratio = self.operating_time / (self.time_test * self.max_speed)
        return self.ratio
