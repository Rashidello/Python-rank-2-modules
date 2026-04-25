class Plant():
    def show(self):
        print(f"{self.name} : {self.Height}cm, {self.Age} days old")


if __name__ == '__main__':
    print("=== Garden Plant Registry ===")
    rose = Plant()
    rose.name = "Rose"
    rose.Height = 25
    rose.Age = 30
    rose.show()

    Sunflower = Plant()
    Sunflower.name = "Sunflower"
    Sunflower.Height = 80
    Sunflower.Age = 45
    Sunflower.show()

    Cactus = Plant()
    Cactus.name = "Cactus"
    Cactus.Height = 15
    Cactus.Age = 120
    Cactus.show()
