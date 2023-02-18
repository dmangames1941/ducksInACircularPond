import math, random, Duck
class Simulation:
  def __init__(self, totalDucks, angle):
    r = 125
    self.duckList= []
    self.totalSucess = 0
    for x in range(totalDucks):
      xyList = giveNewDucksCoords(r)
      angleREL = relativeAngleForDuck(xyList[0],xyList[1],r)
      self.duckList.append(Duck.Duck(xyList[0],xyList[1],angleREL))
    self.totalSucess = checkSucess(self.duckList,angle)
  def getTotalSucess(self):
    return self.totalSucess
  def getDuckList(self):
    return self.duckList

def giveNewDucksCoords(r):
  randomangle = random.random() * math.pi*2
  x = math.cos(randomangle)*r
  y = math.sin(randomangle)*r
  return [int(x),int(y)]
def relativeAngleForDuck(x,y,r):
    angle = math.atan(int(y)/int(x))
    angle=int(angle*(180/math.pi))
    if(x<0 and y>=0):
        angle=abs(angle)+270
    elif(x<0 and y<0):
        angle=angle+180
    elif(x>=0 and y<0):
        angle=angle+90
    return angle
def checkSucess(duckList,angle):
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