

from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from person import Person
from firm import Firm


class market(Agent):
    """ A market, which is an interface between consumers and producers."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.supply = 500
        self.price = 1
        self.soldThisTurn = 0
        self.underSupply = 0

    def step(self):
        self.adjustPrice()
        self.underSupply = 0


    def adjustPrice(self):
        if self.supply > 0:
            self.price -= self.price * (self.supply / (self.soldThisTurn + self.supply))
        else:
            self.price += self.price * (self.underSupply / (self.soldThisTurn + self.underSupply))
        return

    def getPrice(self):
        return self.price
    
    # Agent buys a good from the market
    def buy(self, amount):
        if amount > self.supply:
            amountBought = self.supply
            self.underSupply += amount - self.supply
            self.supply = 0
        else: 
            self.supply -= amount
            amountBought = amount
        self.soldThisTurn += amountBought
        return amountBought

    # Agent sells a good to the market
    def sell(self, amount):
        self.supply += amount
        return amount

class Economy(Model):
    """A model with some number of agents."""
    def __init__(self, numPeople, numFirms):
        self.numPeople = numPeople
        self.numFirms = numFirms
        self.people = RandomActivation(self)
        self.firms = RandomActivation(self)

        # Create People
        for i in range(self.numPeople):
            a = Person(i, self)
            self.people.add(a)
        # Create Firms
        for i in range(self.numFirms):
            a = Firm(i, self)
            self.firms.add(a)
        
        # Create Markets
        self.laborMarket = market(0, self)
        self.goodsMarket = market(1, self)

        # self.datacollector = DataCollector(
        #     model_reporters={"Gini": compute_gini},  # `compute_gini` defined above
        #     agent_reporters={"Wealth": "wealth"})

    def step(self):
        '''Advance the model by one step.'''
        # self.datacollector.collect(self)
        self.laborMarket.soldThisTurn = 0
        self.goodsMarket.soldThisTurn = 0
        self.people.step()
        self.firms.step()
        self.laborMarket.step()
        print("Labor Price " + str(self.laborMarket.getPrice()))
        print("Labor Sold " + str(self.laborMarket.soldThisTurn))
        print("Labor Supply " + str(self.laborMarket.supply))
        self.goodsMarket.step()
        print("Goods Price " + str(self.goodsMarket.getPrice()))
        print("Goods Sold " + str(self.goodsMarket.soldThisTurn))
        print("Goods Supply " + str(self.goodsMarket.supply))