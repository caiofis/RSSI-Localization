import hardware
import matplotlib.pyplot as plt
import numpy as np


def showError():
	error.append(a0.predictDistance([3.7,1.9,a0.getPose()[2]]))
	plt.figure(2)
	plt.plot(i,error)
	i.append(i[-1]+1)
	plt.figure(1)
	print ("Mean error: ", np.mean(error))

data = np.genfromtxt("./data/dataRSSI_Skenario1.txt",delimiter="\t",dtype=int)

a0 = hardware.tag("a0")
ant1 = hardware.antenna(Id=1, pose=[2.5,5,1.8])#,A=-0.08043828,b=9.16771469)
ant2 = hardware.antenna(Id=2, pose=[0,2.5,1.8])#,A=-0.08043828,b=9.16771469)
ant3 = hardware.antenna(Id=3, pose=[2.5,0,1.8])#,A=-0.08043828,b=9.16771469)
ant4 = hardware.antenna(Id=4, pose=[5,2.5,1.8])#,A=-0.08043828,b=9.16771469)
ant5 = hardware.antenna(Id=5, pose=[0,5,1.8])#,A=-0.08043828,b=9.16771469)
ant6 = hardware.antenna(Id=6, pose=[0,0,1.8])#,A=-0.08716238,b=10.10576369)
ant7 = hardware.antenna(Id=7, pose=[5,0,1.8])#,A=-0.10571799,b=10.56375537)
ant8 = hardware.antenna(Id=8, pose=[5,5,1.8])#,A=-0.086835,b=9.32504799)
print a0
print ant1
print ant2
print ant3
print ant4
print ant5  # 3,65m
print ant6
print ant7
print ant8

#plt.ion()
plt.xlim([-1,6])
plt.ylim([-1,6])
ant8.show()
ant7.show()
ant6.show()
ant5.show()
i=[0]
error = []
z = [0]
for read in data:
	if read[1] == 20:
		#Define the distance from tag
		if read[0] == 1:
			pose,dist = ant1.getRead(read[2])
			a0.Update(antenna=pose,distance=dist)
		if read[0] == 2:
			pose,dist = ant2.getRead(read[2])
			a0.Update(antenna=pose,distance=dist)
		if read[0] == 3:
			pose,dist = ant3.getRead(read[2])
			a0.Update(antenna=pose,distance=dist)
		if read[0] == 4:
			pose,dist = ant4.getRead(read[2])
			a0.Update(antenna=pose,distance=dist)
		if read[0] == 5:
			pose,dist = ant5.getRead(read[2])
			a0.Update(antenna=pose,distance=dist)
			#a0.show()
		if read[0] == 6:
			pose,dist = ant6.getRead(read[2])
			a0.Update(antenna=pose,distance=dist)
			#a0.show()
		if read[0] == 7:
			pose,dist = ant7.getRead(read[2])
			a0.Update(antenna=pose,distance=dist)
			#a0.show()
		if read[0] == 8:
			pose,dist = ant8.getRead(read[2])
			a0.Update(antenna=pose,distance=dist)
			print a0
			a0.show()
			error.append(a0.predictDistance([3.7,1.9,a0.getPose()[2]]))
			z.append(a0.getPose()[2])
			i.append(i[-1]+1)
plt.figure(3)
plt.plot(i,z)
plt.figure(1)
showError()
plt.show()
