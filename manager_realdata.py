import hardware
import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt("./data/dataRSSI_Skenario2A_Obstacles_block_randomly.txt",delimiter="\t",dtype=int)

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

plt.ion()
plt.xlim([-1,6])
plt.ylim([-1,6])
ant8.show()
ant7.show()
ant6.show()
ant5.show()
i=[0]
error = []
for read in data:
	if read[1] == 17:
		#Define the distance from tag
		plt.pause(0.5)
		print a0
		# plot error
		error.append(a0.predictDistance([1.9,1.9,0.6]))
		plt.figure(2)
		plt.plot(i,error)
		i.append(i[-1]+1)
		plt.figure(1)

		if read[0] == 5:
			pose,dist = ant5.getRead(read[2])
			a0.Update(antenna=pose,distance=dist)
			a0.show()
		if read[0] == 6:
			pose,dist = ant6.getRead(read[2])
			a0.Update(antenna=pose,distance=dist)
			a0.show()
		if read[0] == 7:
			pose,dist = ant7.getRead(read[2])
			a0.Update(antenna=pose,distance=dist)
			a0.show()
		if read[0] == 8:
			pose,dist = ant8.getRead(read[2])
			a0.Update(antenna=pose,distance=dist)
			a0.show()
plt.pause(5)
plt.show()
