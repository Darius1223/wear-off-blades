from dataclasses import dataclass


@dataclass
class WearData:
    # 1
    after_test: float = 0
    before_test: float = 0
    wear: float = 0
    # 2
    radius: float = 0
    width: float = 0
    blunting: float = 0

    def calculate_wear(self):
        self.wear = self.before_test - self.after_test
        return self.wear

    def calculate_blunting(self):
        self.blunting = 2 * self.radius / self.width * 100
        return self.blunting
