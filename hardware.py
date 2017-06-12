import matplotlib.pyplot as plt
import numpy as np
from ekf import EKF

class tag(object):
    "Describes the RFID tags as an object"
    def __init__(self,Id):
        "Defines the tag Id and pose"
        self.Id = Id
        self.pose = [0,0,0]
        self.filter = EKF(x=np.array(self.pose),P=np.eye(3),V=np.diag([0.0001,0.0001,0.0001]),
                          R=np.diag([7.5,7.50,4.50]))
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
    def Update(self, antenna, distance):
        self.filter.Prediction()
        self.filter.Update(antenna,distance)
        self.newPose(self.filter.x)

class antenna(object):
    "Describes the RFID Antenna as an object"
    def __init__(self,Id,pose,A=-0.09,b=9.8):
        "Defines the tag Id, pose and RSSI to meters params"
        self.Id = Id
        self.pose = pose
        self.A = A
        self.b = b
        self.last_dist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    def __str__(self):
        "Made the class plintable"
        return "Antenna:" + str(self.Id) + " Pose:" + str(self.pose)
    def show(self):
        "Plot the antenna as a star on its pose"
        plt.plot(self.pose[0],self.pose[1],'*')
    def RSSItoMeters(self,RSSI,smooth=False):
        dist = RSSI*self.A + self.b
        if smooth:
            self.last_dist.pop()
            self.last_dist.append(dist)
            dist = 0
            for i in self.last_dist:
                dist += i
        return dist
    def showDist(self,RSSI):
        self.show()
        circle = plt.Circle((self.pose[0],self.pose[1]),self.RSSItoMeters(RSSI))
    def getPose(self):
        "Returns the currently pose of the tag"
        return self.pose
    def getRead(self, RSSI):
        "Returns the antenna's pose and the distance to the tag in meters"
        return self.pose,self.RSSItoMeters(RSSI)
