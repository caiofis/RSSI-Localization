import matplotlib.pyplot as plt
class tag(object):
    def __init__(self,Id):
        self.Id = Id
        self.pose = [0,0,0]
    def __str__(self):
        return "Tag:" + str(self.Id) + " Pose:" + str(self.pose)
    def show(self):
        plt.plot(self.pose[0],self.pose[1],'o')
    def newPose(self,new_pose):
        self.pose = new_pose

class antenna(object):
    def __init__(self,Id,pose,A=-0.09,b=9.8):
        self.Id = Id
        self.pose = pose
        self.A = A
        self.b = b
    def __str__(self):
        return "Antenna:" + str(self.Id) + " Pose:" + str(self.pose)
    def show(self):
        plt.plot(self.pose[0],self.pose[1],'*')
    def RSSItoMeters(self,RSSI):
        return RSSI*self.A + self.b
    def showDist(self,RSSI):
        self.show()
        circle = plt.Circle((self.pose[0],self.pose[1]),self.RSSItoMeters(RSSI))
