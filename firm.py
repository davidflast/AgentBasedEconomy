from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector

from helper import maxUnitsAbleToPurchase

class Firm(Agent):
    """ A firm that buys labor, and uses it to produce goods"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 100
        self.inventory = 0
        self.labor = 0
        self.productivity = 5

    def produce(self):
        self.inventory += self.labor * self.productivity
        self.labor = 0
        unitPrice = self.model.goodsMarket.sell(self.inventory)
        self.wealth += unitPrice * self.inventory
        self.inventory = 0

    def buyLabor(self):
        price = self.model.laborMarket.getPrice()
        unitsToPurchase = maxUnitsAbleToPurchase(self.wealth, price)
        unitsPurchased = self.model.laborMarket.buy(unitsToPurchase)
        self.wealth -= unitsPurchased * price
        self.labor += unitsPurchased
        

    def step(self):
        self.buyLabor()
        self.produce()
