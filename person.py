from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from helper import *

class Person(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 100
        self.laborPerTurn = 40
        self.utility = 0

    def step(self):
        self.utility = 0
        self.sellLabor()
        self.buyGoods()

    def sellLabor(self):
        priceOfLabor = self.model.laborMarket.getPrice()
        unitsSold = self.model.laborMarket.sell(self.laborPerTurn)
        self.wealth += priceOfLabor * unitsSold
    
    def buyGoods(self):
        priceOfGood = self.model.goodsMarket.getPrice()
        unitsToPurchase = maxUnitsAbleToPurchase(self.wealth, priceOfGood )
        unitsPurchased = self.model.goodsMarket.buy(unitsToPurchase)
        self.wealth -= unitsPurchased * priceOfGood
        self.utility += unitsPurchased
