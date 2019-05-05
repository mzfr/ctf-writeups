import re
import matplotlib.pyplot as plt

lines = open("sensors.log").readlines()

coords = []
x_coords = []
y_coords = []
z_coords = []
cur_X,cur_Y,cur_Z = 0,0,0

for line in lines:
    match = re.findall("\[drone\]\(DEBUG\)> dir: \(x=(-?\d.\d+),y=(-?\d+.\d+),z=(-?\d.\d+)\)", line)
    if match:
        x,y,z = map(float, match[0])
        cur_X += x
        cur_Y += y
        cur_Z += z
        x_coords.append(cur_X)
        y_coords.append(cur_Y)
        z_coords.append(cur_Z)
        #print(x,y,z)



ax = plt.plot(x_coords, y_coords, '-')
plt.axis('equal')
#plt.ylim(-500,500)
plt.savefig("test.png", dpi=1000)