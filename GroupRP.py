import numpy as np
import random
from math import floor

CrewList = ["Crew0", "Crew1", "Crew2", "Crew3", "Crew4", "Crew5", "Crew6", "Crew7"]

BufferList = ["Crew4", "Crew2", "Crew5", "Crew1"] # The first will be lastest

testiter = 100000

def TestResult(CrewList:list, BufferList:list, testiter:int):

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
    MyRand = random.uniform(0.0, SumWeight)
    for idx, ele in np.ndenumerate(Weights):
      MyRand -= ele
      if MyRand < 0.0:
        Score[idx] += 1
        break

  Score /= testiter

  print(list(zip(ReList, Score)))

def ThisResult(CrewList:list, BufferList:list):

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
      # print(ReList[idx[0]])
      return ReList[idx[0]]
      break

def TestResult2(CrewList:list, BufferList:list, testiter:int):

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
    Winner = ThisResult(CrewList, BufferList)
    idx = ReList.index(Winner)
    Score[idx] += 1

  Score /= testiter

  print(list(zip(ReList, Score)))
