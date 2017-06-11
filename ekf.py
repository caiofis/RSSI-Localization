import numpy as np
import math

class EKF(object):
    """Implements an EKF to the localization of the RFID tags."""
    def __init__(self,x,P,V,R=0):
        self.x = x      #Set the initial state
        self.P = P      #Set the initial Covariance
        self.V = V      #Set the process noise covariance
        self.R = R      #Set the measurement noise covariance
    def Fx(self,x,u):
        """Linearize the system with the Jacobian of the x"""
        return np.array([[1,0,0],
                         [0,1,0],
                         [0,0,1]])
    def f(self,x,u):
        """Estimate the non-linear state of the system, in this case is
        the actual state."""
        return self.x

    def H(self,dx,dy,dz):
        """Linearize the measurement function with the Jacobian of h related
        to the state."""
        root = self.h(dx,dy,dz)
        #return np.array([dx/root,dy/root,dz/root])
        return np.array([dx/root,dy/root,0])
    def h(self,dx,dy,dz):
        """"Predict the distance from the tag to a point on 3D space using the
        diference in x, y and z"""
        return (dx**2 + dy**2 + dz**2)**0.5

    def Prediction(self):
        #u[1] = ((u[0]/self.L)*math.tan((u[1])))
        #x_ = self.x
        #P_ = self.P
        #self.x = self.f(x_,u)
        self.P += self.V
    def Update(self,antenna, z):
        """Update the Kalman Prediction using the meazurement z.
        Antenna is the pose of the antenna and z is the read dist in meters"""
        self.Prediction()
        dx = self.x[0]-antenna[0]
        dy = self.x[1]-antenna[1]
        dz = self.x[2]-antenna[2]
        H = self.H(dx,dy,dz)

        y = z - self.h(dx, dy,dz)

        S = H.dot(self.P.dot(H.T)) + self.R
        K = self.P.dot(H.T.dot(np.linalg.inv(S)))
        self.x = self.x + K.dot(y)
        #self.x[2] = abs(self.x[2])
        self.x[2] = 0.6
        self.P = (np.eye(3)-K.dot(H)).dot(self.P)
        #self.P = self.P - (K.dot(H.T)).dot(self.P)
