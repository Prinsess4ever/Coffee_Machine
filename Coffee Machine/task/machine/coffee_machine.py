# Write your code here
import sys
from dataclasses import dataclass


@dataclass
class Deliverable:
    name: str
    water: int
    coffee_beans: int
    milk: int
    cost: int
    cups: int = 1


deliverables = [
    Deliverable(name='espresso', water=250, coffee_beans=16, milk=0, cost=4),
    Deliverable(name='latte', water=350, coffee_beans=20, milk=75, cost=7),
    Deliverable(name='cappuccino', water=200, coffee_beans=12, milk=100, cost=6),
]


class NotEnough(Exception):
    pass


@dataclass
class CoffeeMachine:
    water: int
    coffee_beans: int
    milk: int
    cups: int
    money: int

    def _deliver(self, coffee: Deliverable) -> None:
        assert isinstance(coffee, Deliverable), "No coffee!!"
        if self.water < coffee.water:
            raise NotEnough('water')
        if self.milk < coffee.milk:
            raise NotEnough('milk')
        if self.coffee_beans < coffee.coffee_beans:
            raise NotEnough('coffee beans')
        if self.cups < coffee.cups:
            raise NotEnough('cups')

        print("I have enough resources, making you a coffee!\n")

        self.water -= coffee.water
        self.milk -= coffee.milk
        self.coffee_beans -= coffee.coffee_beans
        self.cups -= coffee.cups
        self.money += coffee.cost

    def buy(self) -> None:
        txt = "\nWhat do you want to buy? "
        for idx, coffee in enumerate(deliverables, start=1):
            txt += f'{idx} - {coffee.name}, '
        txt += 'back - to main menu\n'
        what_to_buy = input(txt)

        if what_to_buy == "back":
            return

        which_coffee = deliverables[int(what_to_buy) - 1]
        try:
            self._deliver(which_coffee)
        except NotEnough as missing_ingredient:
            print(f"Sorry, not enough {missing_ingredient}!")

    def fill(self):
        water_plus = int(input("\nWrite how many ml of water you want to add: \n"))
        milk_plus = int(input("Write how many ml of milk you want to add: \n"))
        coffee_beans_plus = int(input("Write how many grams of coffee beans you want to add: \n"))
        disposable_cups_plus = int(input("Write how many disposable cups you want to add: \n"))
        print("")

        self.water += water_plus
        self.milk += milk_plus
        self.coffee_beans += coffee_beans_plus
        self.cups += disposable_cups_plus

    def take(self) -> None:
        print(f"I gave you ${self.money}\n")
        self.money = 0

    def remaining(self) -> None:
        print(f"\nThe coffee machine has:")
        print(f"{self.water} ml of water")
        print(f"{self.milk} ml of milk")
        print(f"{self.coffee_beans} g of coffee beans")
        print(f"{self.cups} disposable cups")
        print(f"${self.money} of money\n")


def stage():
    machine = CoffeeMachine(water=400, coffee_beans=120, milk=540, cups=9, money=550)

    while True:
        action = input("Write action (buy, fill, take, remaining, exit): \n")

        if action == "buy":
            machine.buy()

        elif action == "fill":
            machine.fill()

        elif action == "take":
            machine.take()

        elif action == "remaining":
            machine.remaining()

        elif action == "exit":
            sys.exit(0)


stage()
