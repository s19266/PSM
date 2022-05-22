import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = 2
y = 2

original_top_temp=200
original_bottom_temp=50
original_left_temp=150
original_right_temp=100

delta=1

def calculate_temp(x,y):
  color_interpolation=50
  color_map=plt.cm.get_cmap('RdYlGn_r')

  a=np.zeros((x*y,x*y)) 
  b=np.zeros((x*y))

  for j in range(1, y+1, delta):
    for i in range(1, x+1, delta):
      point_to_find = (i,j)

      bottom_point = calculate_bottom_point(point_to_find)
      top_point = calculate_top_point(point_to_find)
      left_point = calculate_left_point(point_to_find)
      right_point = calculate_right_point(point_to_find)

      bottom_temp = export_temp(bottom_point)
      top_temp = export_temp(top_point)
      left_temp = export_temp(left_point)
      right_temp = export_temp(right_point)

      a[export_line_table(point_to_find),export_line_table(point_to_find)] = -4
      if bottom_temp is None:
        a[export_line_table(bottom_point), export_line_table(point_to_find)] = 1
      if top_temp is None:
        a[export_line_table(top_point), export_line_table(point_to_find)] = 1
      if left_temp is None:
        a[export_line_table(left_point), export_line_table(point_to_find)] = 1
      if right_temp is None:
        a[export_line_table(right_point), export_line_table(point_to_find)] = 1

      b[export_line_table(point_to_find)] = -calc_known_temp([bottom_temp,
                                                              top_temp,
                                                              left_temp,
                                                              right_temp
                                                            ])
  final_matrix = np.dot(np.linalg.inv(a), b)
  final_matrix = final_matrix.reshape((y,x))
  plt.title(f"2D temperature - {x} x {y}")
  plt.contourf(final_matrix, color_interpolation, cmap=color_map)
  plt.colorbar()
  plt.show()

  
  final_matrix = np.flipud(final_matrix)

  # Create nice and colourful temp plot


  final_matrix=np.c_[np.full((y,1), original_left_temp, dtype=float), final_matrix, np.full((y,1), original_right_temp, dtype=float)]

  mom_matrix = np.full((1,x+2), original_bottom_temp, dtype=float)
  final_matrix = np.append(final_matrix, mom_matrix, axis=0)
  
  mom_matrix = np.full((1,x+2), original_top_temp, dtype=float)
  final_matrix = np.append(mom_matrix,final_matrix, axis=0)

  final_matrix[0,0]= None
  final_matrix[0,-1]= None
  final_matrix[-1,-1]= None
  final_matrix[-1,0]= None

  # Code below is probably a bug, doesn't allow to paste matrix into another matrix which has same shape but one additional line.
  #mom_matrix = np.full((y+2,x+2),original_top_temp)
  #print (mom_matrix)
  #mom_matrix[1:,:] = final_matrix

  df= pd.DataFrame(data=final_matrix)
  # Export to excel

  df.to_excel(sys.path[0]+"/HEAT_CALC.xlsx", index = False)
  print (f"Done! Check your excel here: {sys.path[0]}/HEAT_CALC.xlsx")

def export_temp(point):
  px,py = point[0],point[1]
  if ((px != 0 and px != x + 1) and (py != 0 and py != y + 1)):
    return None
  if (px == 0):
    return original_left_temp
  if (px == x+1):
    return original_right_temp
  if (py == 0):
    return original_bottom_temp
  if (py == y+1):
    return original_top_temp

def export_line_table(point):
  px,py = point[0],point[1]
  return px - 1 + (( py - 1 ) * x)

def calc_known_temp(temperatures):
  return sum(filter(lambda val: val,temperatures))

def calculate_top_point(point):
  return (point[0], point[1]+1)

def calculate_left_point(point):
  return (point[0]-1, point[1])

def calculate_bottom_point(point):
  return (point[0], point[1]-1)

def calculate_right_point(point):
  return (point[0]+1, point[1])

def main():
  calculate_temp(x,y)

if __name__ == '__main__':
  main()