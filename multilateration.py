from scipy.optimize import minimize
import math

# Mean Square Error
def mse(tag,antennas,distances):
        mse = 0.0
        #print antennas, distances
        for i in range(len(distances)):
            #print distances[i],antennas
            distance_calculated = euclidean(antennas[i],tag)
            #print distance_calculated
            mse += math.pow(distance_calculated - distances[i], 2.0)
        return mse / len(distances)
def euclidean( antenna, tag):
        """Calculates the euclideian distance from the tag to a antenna"""
        dx = tag[0]-antenna[0]
        dy = tag[1]-antenna[1]
        dz = tag[2]-antenna[2]
        #print dx, dy, dz
        return (dx**2 + dy**2 + dz**2)**0.5
bnds = ((0,1000),(0,1000),(0,1000))
def position(antennas,distances,tag=[0,0,0]):
        return minimize( mse,  # Error Function
                                    tag,    # Initial Guess
                                    args=(antennas,distances), # Additional parameters for mse
                                    method='L-BFGS-B',           # The optimisation algorithm
                                    #bounds=bnds,
                                     # options={
                                     #         'ftol':1e-5,         # Tolerance
                                     #         'maxiter': 1e+7      # Maximum iterations
                                     #               }
                                    ).x



# initial_location: (lat, long)
# locations: [ (lat1, long1), ... ]
# distances: [ distance1,     ... ]

localizations = [(0,0,0),(0,5,0),(5,0,0)]
distances = [5,3.16,4.47] #Pose = (3,4,0)

print position(antennas=localizations,distances=distances,tag=(0,0,0))

