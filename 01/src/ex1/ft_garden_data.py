class Plant:
    def __init__(self, name: str, height: str, age: str) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: ".capitalize(), f"{self.height}cm {self.age} days old")


def main() -> None:
    plant1 = Plant("rose", "25", "30")
    plant2 = Plant("sunflower", "80", "45")
    plant3 = Plant("cactus", "15", "120")
    plant1.show()
    plant2.show()
    plant3.show()
