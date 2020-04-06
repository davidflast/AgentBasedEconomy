from model import Economy

economy = Economy(100, 1)

for i in range(10):
    economy.step()

import matplotlib.pyplot as plt

agent_wealth = [a.wealth for a in economy.people.agents]
plt.hist(agent_wealth)
plt.show()


