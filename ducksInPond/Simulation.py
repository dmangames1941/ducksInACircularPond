import math, random, Duck
import matplotlib.pyplot as plt
import numpy as np
class Simulation:
  def __init__(self, totalDucks, iterations,angle):
            r = 10
            duckList= []
            totalSucess = 0
            currentIt = 1
            for x in range(iterations):
                duckList.clear()
                for x in range(totalDucks):
                    xyList = giveNewDucksCoords(r)
                    angleREL = relativeAngleForDuck(xyList[0],xyList[1],r)
                    duckList.append(Duck.Duck(xyList[0],xyList[1],angleREL))
                totalSucess = totalSucess+ checkSucess(duckList,angle)
                currentIt += 1
            return totalSucess/iterations

def giveNewDucksCoords(r):
  randomangle = random.random() * math.pi*2
  x = math.cos(randomangle)*r
  y = math.sin(randomangle)*r
  return [x,y]
def relativeAngleForDuck(x,y,r):
    angle = math.atan(y/x)
    angle=angle*(180/math.pi)
    if(x<0 and y>=0):
        angle=abs(angle)+270
    elif(x<0 and y<0):
        angle=angle+180
    elif(x>=0 and y<0):
        angle=angle+90
    return angle
def checkSucess(duckList,angle):
  createGraph(duckList)
  angleList = []
  for x in range(len(duckList)):
    angleList.append(duckList[x].getRelativeAngle())
  angleList.sort()
  if (abs(angleList[0]-angleList[-1]))<=angle:
    return 1
  for x in range(len(angleList)):
    angleList[x]= angleList[x]+angle
    if angleList[x] >=360:
      angleList[x]=angleList[x]-360
  angleList.sort()
  if (abs(angleList[0]-angleList[-1]))<=angle:
    return 1
  else: 
    return 0

def createGraph(duckList):
  center = (0,0)
  r = 10
  theta = np.linspace(0, 2*np.pi, 100)
  x = center[0] + r * np.cos(theta)
  y = center[1] + r * np.sin(theta)
  fig, ax = plt.subplots()
  ax.plot(x, y)
  xArray = []
  yArray = []
  for i in range(len(duckList)):
    xArray.append(duckList[i].getX())
    yArray.append(duckList[i].getY())
  print("plotting")
  ax.plot(xArray,yArray)
  print("paused")
  plt.pause(5)
  plt.close()
  plt.title("Ducks In A Circular Pond Simulation")
  plt.show() 