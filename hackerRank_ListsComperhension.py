
x = int(input())
y = int(input())
z = int(input())
n = int(input()) 

coord = [(x_val, y_val, z_val) for x_val in x for y_val in y for z_val in z if (x_val + y_val + z_val) != n]
print(coord)