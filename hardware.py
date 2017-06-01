import matplotlib.pyplot as plt
class tag(object):
    "Describes the RFID tags as an object"
    def __init__(self,Id):
        "Defines the tag Id and pose"
        self.Id = Id
        self.pose = [0,0,0]
    def __str__(self):
        "Made the class plintable"
        return "Tag:" + str(self.Id) + " Pose:" + str(self.pose)
    def show(self):
        "Plot the tag as a point on its pose"
        plt.plot(self.pose[0],self.pose[1],'o')
    def newPose(self,new_pose):
        "Sets a new pose to the tag"
        self.pose = new_pose
    def getPose(self):
        "Returns the currently pose of the tag"
        return self.pose
    def predictDistance(self, point):
        "Predict the distance from the tag to a point on 3D space"
        return ((self.pose[0]-point[0])**2 + (self.pose[1]-point[1])**2 +
               (self.pose[2]-point[2])**2)**0.5

class antenna(object):
    "Describes the RFID Antenna as an object"
    def __init__(self,Id,pose,A=-0.09,b=9.8):
        "Defines the tag Id, pose and RSSI to meters params"
        self.Id = Id
        self.pose = pose
        self.A = A
        self.b = b
    def __str__(self):
        "Made the class plintable"
        return "Antenna:" + str(self.Id) + " Pose:" + str(self.pose)
    def show(self):
        "Plot the antenna as a star on its pose"
        plt.plot(self.pose[0],self.pose[1],'*')
    def RSSItoMeters(self,RSSI):
        return RSSI*self.A + self.b
    def showDist(self,RSSI):
        self.show()
        circle = plt.Circle((self.pose[0],self.pose[1]),self.RSSItoMeters(RSSI))
    def getPose(self):
        "Returns the currently pose of the tag"
        return self.pose
    def getRead(self, RSSI):
        "Returns the antenna's pose and the distance to the tag in meters"
        return self.pose,self.RSSItoMeters(RSSI)
