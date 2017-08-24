import hardware
import matplotlib.pyplot as plt
import numpy as np


def showError():
    error.append(a0.predictDistance(truePose))
    #error1.append(a1.predictDistance(truePose))
    #error2.append(mean.predictDistance(truePose))
    plt.figure(2)
    plt.plot(i, error)
    #plt.plot(j, error1)
    #plt.plot(k, error2, 'r')
    i.append(i[-1] + 1)
    j.append(j[-1] + 1)
    k.append(k[-1] + 1)
    plt.figure(1)
    print ("Mean error: ", np.mean(error))
    #print ("Mean error: ", np.mean(error1))
    #print ("Mean error: ", np.mean(error2))


def meanPose():
    pose1 = a0.getPose()
    pose2 = a1.getPose()
    mean_pose = (pose1 + pose2) * 0.5
    mean.newPose(mean_pose)


data = np.genfromtxt("./data/dataRSSI_Skenario1.txt", delimiter="\t", dtype=int)

truePose = [2.5, 2.5, 0.9]
a0 = hardware.tag("a0")
a1 = hardware.tag("a1")
mean = hardware.tag("a2")
ant1 = hardware.antenna(Id=1, pose=[2.5, 5, 1.8])  # ,A=-0.08043828,b=9.16771469)
ant2 = hardware.antenna(Id=2, pose=[0, 2.5, 1.8])  # ,A=-0.08043828,b=9.16771469)
ant3 = hardware.antenna(Id=3, pose=[2.5, 0, 1.8])  # ,A=-0.08043828,b=9.16771469)
ant4 = hardware.antenna(Id=4, pose=[5, 2.5, 1.8])  # ,A=-0.08043828,b=9.16771469)
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

# plt.ion()
plt.xlim([-1, 6])
plt.ylim([-1, 6])
ant1.show()
ant2.show()
ant3.show()
ant4.show()
ant5.show()
ant6.show()
ant7.show()
ant8.show()
i = [0]
j = [0]
k = [0]
error = []
#error1 = []
#error2 = []
z = [0]
for read in data:
    if read[1] == 13:
        # Define the distance from tag
        if read[0] == 1:
            pose, dist = ant1.getRead(read[2])
            a0.Update(antenna=pose, distance=dist)
        if read[0] == 2:
            pose, dist = ant2.getRead(read[2])
            a0.Update(antenna=pose, distance=dist)
        if read[0] == 3:
            pose, dist = ant3.getRead(read[2])
            a0.Update(antenna=pose, distance=dist)
        if read[0] == 4:
            pose, dist = ant4.getRead(read[2])
            a0.Update(antenna=pose, distance=dist)
        if read[0] == 5:
            pose, dist = ant5.getRead(read[2])
            a0.Update(antenna=pose, distance=dist)
        if read[0] == 6:
            pose, dist = ant6.getRead(read[2])
            a0.Update(antenna=pose, distance=dist)
        if read[0] == 7:
            pose, dist = ant7.getRead(read[2])
            a0.Update(antenna=pose, distance=dist)
        if read[0] == 8:
            pose, dist = ant8.getRead(read[2])
            a0.Update(antenna=pose, distance=dist)
            print a0
            a0.show("r")
            error.append(a0.predictDistance(truePose))
            z.append(a0.getPose()[2])
            i.append(i[-1] + 1)
    # if read[1] == 8:
    #     # Define the distance from tag
    #     if read[0] == 1:
    #         pose, dist = ant1.getRead(read[2])
    #         a1.Update(antenna=pose, distance=dist)
    #     if read[0] == 2:
    #         pose, dist = ant2.getRead(read[2])
    #         a1.Update(antenna=pose, distance=dist)
    #     if read[0] == 3:
    #         pose, dist = ant3.getRead(read[2])
    #         a1.Update(antenna=pose, distance=dist)
    #     if read[0] == 4:
    #         pose, dist = ant4.getRead(read[2])
    #         a1.Update(antenna=pose, distance=dist)
    #         print a1
    #         a1.show("b")
    #         error1.append(a1.predictDistance(truePose))
    #         # z.append(a0.getPose()[2])
    #         j.append(j[-1] + 1)
    #         meanPose()
    #         mean.show("g")
    #         error2.append(mean.predictDistance(truePose))
    #         k.append(k[-1] + 1)

# plt.figure(3)
# plt.plot(i,z)
plt.figure(1)
showError()
plt.show()
