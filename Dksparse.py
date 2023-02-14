import numpy as np
from matplotlib import pyplot as plt

def Dksparse(Kmax: int) ->np.ndarray:
    
    sparse = np.zeros([Kmax,Kmax])
    
    for k in range(2,int(0.24479167*Kmax)):
        
        sparse[k,k-2] = 1
        sparse[k,k+2] = 1  

    for k in range(int(0.24479167*Kmax),int(0.49479167*Kmax)):
        for j in range(2,14):
            sparse[k,k-j] = 1
            sparse[k,k+j] = 1
    
    for k in range(int(0.49479167*Kmax),Kmax):
        for j in range(2,28):
            sparse[k,k-j] = 1
            if k+j < Kmax:
                sparse[k,k+j] = 1
    
    return sparse            


trial=Dksparse(1151)
fig=plt.figure()
ax=plt.axes(projection='3d')
# for k in range (1151):
#    Indexes=np.argwhere(trial[k,:]==1).flatten()
#    ax.scatter(np.ones(Indexes.shape[0])*k,Indexes)
 
print(trial.shape) 
   
x = range(trial.shape[0])
y = range(trial.shape[1])  

X, Y = np.meshgrid(x,y) 
   
ax.scatter3D(X , Y, trial, c=trial, cmap='viridis' )   
ax.view_init(elev=90, azim=0)   
plt.show()
 
 
 
# logical = np.array([0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,]) 
# print(logical)    
# data = np.argwhere(logical==1).flatten()
# print(data)    
