import hardware
import matplotlib.pyplot as plt

a0 = hardware.tag("a0")
ant5 = hardware.antenna(Id=5, pose=[0,5,1.8])
ant6 = hardware.antenna(Id=6, pose=[0,0,1.8])
ant7 = hardware.antenna(Id=7, pose=[5,0,1.8])
ant8 = hardware.antenna(Id=8, pose=[5,5,1.8])
print a0
print ant5  # 3,65m
print ant6
print ant7
print ant8


pose,dist = ant8.getRead(65)
plt.ion()
plt.xlim([-1,6])
plt.ylim([-1,6])
ant8.show()
ant7.show()
ant6.show()
ant5.show()
for i in range(100):
    a0.show()
    print a0.getPose()
    #a0.Update(antenna=ant5.getPose(),distance=3.65)
    a0.Update(antenna=ant6.getPose(),distance=3.65)
    a0.Update(antenna=ant7.getPose(),distance=3.65)
    a0.Update(antenna=pose,distance=dist)
    plt.pause(0.5)
plt.pause(5)
plt.show()
