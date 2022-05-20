import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

max_n_iterations=500

len_x=10
len_y=10
delta=1

top_temp=200
bottom_temp=50
left_temp=150
right_temp=100


init_temp=100

color_interpolation=50
color_map=plt.cm.get_cmap('RdYlGn_r')

x,y = np.meshgrid (np.arange(0,len_x), np.arange(0,len_y))

temp=np.empty((len_x, len_y))
temp.fill(init_temp)

temp[(len_y-1):,:]=top_temp
temp[:1,:]=bottom_temp
temp[:,(len_x-1):]=right_temp
temp[:,:1]=left_temp

#print(temp[(len_y-1):,:],temp[:1,:],temp[:,(len_x-1):],temp[:,:1])

for iter in range(0,max_n_iterations):
  for i in range(1,len_x-1,delta):
    for j in range(1,len_x-1,delta):
      temp[i,j]=( 
                  temp[i+1][j] +
                  temp[i-1][j] +
                  temp[i][j+1] +
                  temp[i][j-1] 
                )/4

# plt.title("2D temperature")
# plt.contourf(x,y,temp, color_interpolation, cmap=color_map)
# plt.colorbar()
# plt.show()

# print(np.matrix(temp))

print (pd.DataFrame(data=temp))
