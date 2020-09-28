import numpy as np
import random
from math import floor

CrewList = ["Crew0", "Crew1", "Crew2", "Crew3", "Crew4", "Crew5", "Crew6", "Crew7"]

BufferList = ["Crew4", "Crew2", "Crew5", "Crew1"] # The first will be lastest

testiter = 100000

def RandomPickOld(CrewList:list, BufferList:list):

  n = len(CrewList)
  nb = len(BufferList)

  RemainList = []

  for i in CrewList:
    if i not in BufferList:
      RemainList.append(i)

  nr = len(RemainList)

  if nb + nr != n:
    raise ValueError("Wrong BufferList!\n")

  BufferWeight = np.linspace(0.0, 1.0, nb, endpoint=False)
  RemainWeight = np.ones(nr)

  Weights = np.concatenate((BufferWeight, RemainWeight))
  ReList = BufferList + RemainList

  SumWeight = np.sum(Weights)

  MyRand = random.uniform(0.0, SumWeight)
  for idx, ele in np.ndenumerate(Weights):
    MyRand -= ele
    if MyRand < 0.0:
      return ReList[idx[0]]
      break

def RandomPick(CrewList:list, BufferList:list):

  n = len(CrewList)
  nb = len(BufferList)
  BufferWeight = np.linspace(0.0, 1.0, nb, endpoint=False)
  Weights = np.ones(n)

  for i, x in enumerate(BufferList):
    idx = CrewList.index(x)
    Weights[idx] = BufferWeight[i]

  SumWeight = np.sum(Weights)

  MyRand = random.uniform(0.0, SumWeight)
  for idx, ele in np.ndenumerate(Weights):
    MyRand -= ele
    if MyRand < 0.0:
      return CrewList[idx[0]]
      break

def RandomPick2(CrewList:list, BufferList:list):

  n = len(CrewList)
  nb = len(BufferList)
  BufferWeight = np.linspace(0.0, 1.0, nb, endpoint=False)
  Weights = np.ones(n)

  for i, x in enumerate(BufferList):
    idx = CrewList.index(x)
    Weights[idx] = BufferWeight[i]

  while True:
    Randi = random.randrange(n)
    MyRand = random.random()
    if MyRand < Weights[Randi]:
      return CrewList[Randi]

def TestResult(CrewList:list, BufferList:list, testiter:int, RPFun:object):

  n = len(CrewList)
  nb = len(BufferList)

  RemainList = []

  for i in CrewList:
    if i not in BufferList:
      RemainList.append(i)

  nr = len(RemainList)

  if nb + nr != n:
    raise ValueError("Wrong BufferList!\n")

  BufferWeight = np.linspace(0.0, 1.0, nb, endpoint=False)
  RemainWeight = np.ones(nr)

  Weights = np.concatenate((BufferWeight, RemainWeight))
  ReList = BufferList + RemainList

  SumWeight = np.sum(Weights)
  Score = np.zeros(n)

  for i in range(testiter):
    Winner = RPFun(CrewList, BufferList)
    idx = ReList.index(Winner)
    Score[idx] += 1

  Score /= testiter

  print(list(zip(ReList, Score)))

# TestResult(CrewList, BufferList, testiter, RandomPick2)
print(RandomPick2(CrewList,BufferList))
