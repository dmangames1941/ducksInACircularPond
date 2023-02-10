class Duck:
  def __init__(self, x, y,angle):
    self.xCord = x
    self.yCord = y
    #relative to orgin 
    self.relativeAngle = angle
  def getX(self):
    return self.xCord
  def getY(self):
    return self.yCord
  def getRelativeAngle(self):
    return self.relativeAngle
  def setRelativeAngle(self,angle):
    self.relativeAngle = angle