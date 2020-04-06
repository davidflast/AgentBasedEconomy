from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector



class market(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.supply = 0
        self.price = 0

    def step(self):
        return

    def adjustPrice(self):
        return

    def getPrice(self):
        return self.price
    
    def buy(self, amount):
        self.supply -= amount


    def sell(self, amount):
        self.supply += amount
        
            
