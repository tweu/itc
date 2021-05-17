import random
import os
import sys
names = ["AIBEK", "JOOMART", "ADINAI", "ERMEK", "ATAI", "ASLAN", "LYAZAT", "SALAVAT", "DANIYAR", "BOLOTBEK", "ALYMBEK", "DASTAN","MAKSAT"]
random.shuffle(names)
team1=[]
team2=[]
team3=[]
team4=[]
team1.extend(names[0:3])
team2.extend(names[4:7])
team3.extend(names[7:10])
team4.extend(names[10:13])
print(team1)
print(team2)
print(team3)
print(team4)