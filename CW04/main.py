from turtle import right
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys

def calculate_heat(x,y):

  max_n_iterations=500

  len_x=x+2
  len_y=y+2
  delta=1

  top_temp=200
  bottom_temp=50
  left_temp=150
  right_temp=100


  init_temp=(top_temp+bottom_temp+left_temp+right_temp)/4

  color_interpolation=50
  color_map=plt.cm.get_cmap('RdYlGn_r')

  # initialization
  x_arr,y_arr = np.meshgrid (np.arange(0,len_x), np.arange(0,len_y))

  temp=np.empty((len_x, len_y))
  temp.fill(init_temp)

  temp[:,(len_x-1):]=right_temp
  temp[:,:1]=left_temp
  temp[(len_y-1):,:]=top_temp
  temp[:1,:]=bottom_temp

  # function to calculate the heat
  for iter in range(0,max_n_iterations):
    for i in range(1,len_x-1,delta):
      for j in range(1,len_x-1,delta):
        temp[i,j]=( 
                    temp[i+1][j] +
                    temp[i-1][j] +
                    temp[i][j+1] +
                    temp[i][j-1] 
                  )/4
  # Create nice and colourful heat plot
  plt.title(f"2D temperature - {x} x {y}")
  plt.contourf(temp, color_interpolation, cmap=color_map)
  plt.colorbar()
  plt.show()

  temp_df= pd.DataFrame(data=temp)
  temp_df=temp_df.reindex(index=temp_df.index[::-1])

  temp_df[0][0]=np.NaN
  temp_df[len_x-1][0]=np.NaN
  temp_df[0][len_y-1]=np.NaN
  temp_df[len_x-1][len_y-1]=np.NaN

  # Export to excel
  temp_df.to_excel(sys.path[0]+"/HEAT_CALC.xlsx", index = False)
  print (f"Done! Check your excel here: {sys.path[0]}/HEAT_CALC.xlsx")

calculate_heat(40,40)