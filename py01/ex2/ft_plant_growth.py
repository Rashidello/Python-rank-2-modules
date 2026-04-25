#!/usr/bin/env python3

class Plant():
    def __init__(self, name_input: str, height_input: float,
                 age_input: int) -> None:
        self.name = name_input
        self.height = height_input
        self.plant_age = age_input
        self.initial_height = height_input

    def age(self):
        self.plant_age += 1

    def grow(self):
        self.age_growth = 0.8
        self.height += self.age_growth
        self.height = round(self.height, 2)

    def main(self):
        print("=== Garden Plant Growth ===")
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")

        for i in range(1, 8):
            self.age()
            self.grow()
            print(f"=== Day {i} ===")
            print(f"{self.name}: {self.height}cm, {self.plant_age} days old")

        nl = self.height - self.initial_height
        print(f"Growth this week: {round(nl, 2)}")


if __name__ == "__main__":
    name = Plant("Rose", 25.0, 30)
    name.main()