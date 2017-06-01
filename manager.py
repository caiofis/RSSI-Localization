import hardware
import matplotlib.pyplot as plt

a0 = hardware.tag("a0")
ant8 = hardware.antenna(Id=8, pose=[5,5,1.8])
print a0
print a0.getPose()
print ant8


pose,dist = ant8.getRead(65)

a0.show()
a0.newPose(new_pose=[0.6,5-1.3,0.6])
a0.show()
print ant8.RSSItoMeters(50)
print a0.predictDistance(pose)
ant8.show()
plt.show()
