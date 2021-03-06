from vector import Vector
from plane import Plane

#test equal
test_vec		= Vector((1,2,3))
test_vec1		= Vector((1,2,3))
# print('Check if equal : ', test_vec == test_vec1)

# Add operation
a = Vector((8.218, -9.341))
b = Vector((-1.129, 2.111))
# print('Sum of 2 Vec :', a.add_vector(b))

# Subtract
c = Vector((7.119, 8.215))
d = Vector((-8.223, 0.878))
# print('Diff of 2 Vec :', c.sub_vector(d))

# Scalar mul
# print('Scalar mul :', d.mul_vector(2))

# magnitude
e = Vector((-0.221, 7.437))
f = Vector((8.813, -1.331, -6.247))
# print(e,e.magnitude())
# print(f,f.magnitude())

# normalization
g = Vector((5.581, -2.136)) 
h =	Vector((1.996, 3.108, -4.554))
# print(g,g.normalization())
# print(h.normalization())

# Dot product (Inner product)
v1 = Vector((7.887, 4.138))
w1 = Vector((-8.802, 6.776))
# print(v1.dot_product(w1))

v2 = Vector((-5.955, -4.904, -1.874))
w2 = Vector((-4.496, -8.755, 7.103))
# print(v2.dot_product(w2))

# Angle in radians
v = Vector((3.183, -7.627))
w = Vector((-2.668, 5.319))
# print(v.angle_in_rad(w))

# Angle in degree
v = Vector((7.35, 0.221, 5.188))
w = Vector((2.751, 8.259, 3.985))
# print(v.angle_in_degree(w))

# Orthogonality
v = Vector((-7.579,-7.88))
w = Vector((0, 0))
# print(v.is_orthogonal(w))

# Parallel
v = Vector((-7.579,-7.88))
w = Vector((1, 0))
# print(v.is_parallel(w))

# Projection
v = Vector((3.039, 1.879))
b = Vector((0.825, 2.036))
# print(v.projection(b))

# Perpendicular
v = Vector([-9.88, -3.264, -8.159])
b = Vector([-2.155, -9.353, -9.473])
# print(v.perpendicular(b))

# Cross product
v = Vector([8.462, 7.893, -8.187])
w = Vector([6.984, -5.975, 4.778])
# print(v.cross_product_3D(w))
# print(v.area_of_parallelogram(w))

# Planes
p1 = Plane(normal_vector=Vector((-0.412, 3.806, 0.728)), constant_term=-3.46)
p2 = Plane(normal_vector=Vector((1.03, -9.515, -1.82)), constant_term=8.65)
# print(p1 == p2)
# print(p1.is_parallel_to(p2))