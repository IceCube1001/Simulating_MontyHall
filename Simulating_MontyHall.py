# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 14:27:34 2020
Simulating Monty Hall
There are 3 doors in front of you, and there is a prize behind one of them.
Once you select a door, Host will open one of the other doors that not have a prize behind it
You will then have the opportunity to switch from the door you originally selected
@author: Roy.Zhou

"""

import numpy as np
import matplotlib.pyplot as plt

number_of_games = 10000

chance_of_win_by_switching = np.zeros(number_of_games,dtype=np.double)
chance_of_win_by_stay = np.zeros(number_of_games,dtype=np.double)

options = [1,2,3]

for i in range(number_of_games):
    door_host_open = options.copy()
    door_win = np.random.randint(1,4)
    door_host_open.remove(door_win)
    door_i_choose = np.random.randint(1,4)
    if (door_i_choose!=door_win): door_host_open.remove(door_i_choose)
    door_to_switch = options.copy()
    door_to_switch.remove(door_i_choose)
    door_to_switch.remove(door_host_open[0])
    if i==0:
        if (door_to_switch[0]==door_win):
            chance_of_win_by_switching[i] = 1.0
        else:
            chance_of_win_by_stay[i] = 1.0
    else:
        if (door_to_switch[0]==door_win):
            chance_of_win_by_switching[i] = (chance_of_win_by_switching[i-1]*np.double(i) + 1.0)/np.double(i+1)
            chance_of_win_by_stay[i] = chance_of_win_by_stay[i-1]*np.double(i)/np.double(i+1)
        else:
            chance_of_win_by_stay[i] = (chance_of_win_by_stay[i-1]*np.double(i) + 1.0)/np.double(i+1)
            chance_of_win_by_switching[i] = chance_of_win_by_switching[i-1]*np.double(i)/np.double(i+1)

trials = np.linspace(1,number_of_games,number_of_games)
plt.semilogx(trials, chance_of_win_by_switching, color='red')
plt.semilogx(trials, chance_of_win_by_stay, color='green')
plt.legend(['switch' , 'stay'])
plt.xlabel('Game Number')
plt.ylabel('Probability of winnig')
plt.show()