""" Preprocess the data to apply multilateration"""
import hardware
import matplotlib.pyplot as plt
import numpy as np
import datetime
from multilateration import position

def showError():
    error.append(a0.predictDistance([2.5,2.5,0.9]))
    plt.figure(2)
    plt.plot(i,error)
    i.append(i[-1]+1)
    plt.figure(1)

data = np.recfromtxt("./data/dataRSSI_Skenario3_Target_E_tags_move.txt",delimiter="\t")#,dtype=int)

initial_time = datetime.datetime.strptime(data[0][3],"%H:%M:%S")
current_time = initial_time+datetime.timedelta(seconds=1)
#final_time = initial_time+datetime.timedelta(seconds=10)
final_time = datetime.datetime.strptime(data[-1][3],"%H:%M:%S")
print initial_time
print final_time


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
while initial_time<final_time:
    antennas = []
    distances = []
    for read in data:
        if read[1] ==13:
            if read[3] == initial_time.strftime("%-H:%M:%S") or read[3] == current_time.strftime("%-H:%M:%S"):
                if read[0] == 1:
                    pose,dist = ant1.getRead(read[2])
                    antennas.append(pose)
                    distances.append(dist)
                if read[0] == 2:
                    pose,dist = ant2.getRead(read[2])
                    antennas.append(pose)
                    distances.append(dist)
                if read[0] == 3:
                    pose,dist = ant3.getRead(read[2])
                    antennas.append(pose)
                    distances.append(dist)
                if read[0] == 4:
                    pose,dist = ant4.getRead(read[2])
                    antennas.append(pose)
                    distances.append(dist)
                if read[0] == 5:
                    pose,dist = ant5.getRead(read[2])
                    antennas.append(pose)
                    distances.append(dist)
                if read[0] == 6:
                    pose,dist = ant6.getRead(read[2])
                    antennas.append(pose)
                    distances.append(dist)
                if read[0] == 7:
                    pose,dist = ant7.getRead(read[2])
                    antennas.append(pose)
                    distances.append(dist)
                if read[0] == 8:
                    pose,dist = ant8.getRead(read[2])
                    antennas.append(pose)
                    distances.append(dist)
    if len(distances)!=0:
        new_pose = position(antennas, distances,a0.getPose())
        new_pose = (new_pose+a0.getPose())/2
    a0.newPose(new_pose)
    print a0
    a0.show()
    error.append(a0.predictDistance([2.5,2.5,0.9]))
    i.append(i[-1]+1)
    z.append(a0.getPose()[2])
    initial_time = initial_time+datetime.timedelta(seconds=1)
    current_time = initial_time+datetime.timedelta(seconds=1)

plt.figure(3)
plt.plot(i,z)
plt.figure(1)
showError()
plt.show()
