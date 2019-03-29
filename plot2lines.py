import matplotlib.pyplot as plt 

# line 1 points 
x1 = [1,2,3] 
y1 = [2,4,1] 
# plotting the line 1 points 
plt.plot(x1, y1) 

# line 2 points 
x2 = [1,2,3] 
y2 = [4,1,3] 
# plotting the line 2 points 
plt.plot(x2, y2) 

# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis')

# show a legend on the plot 
plt.legend() 

# function to show the plot 
plt.show() 
