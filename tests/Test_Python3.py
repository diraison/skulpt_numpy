import numpy as np

a = [[1, 2], [3, 4]]

b = np.array(a, ndmin=3, dtype=float)
print("np.array(a, ndmin=3a, dtype=float)")

c = np.ones(b.shape)
print("np.ones(b.shape): %s" % (c,))
d = np.zeros(b.shape)
print("np.zeros(b.shape): %s" % (d,))
print("__str__: %s" % b)
print("__repr__: %r" % b)
print("__len__: %s" % len(b))
print("shape %s" % (b.shape,))
print("ndim %s" % b.ndmin)
print("data: %s"  % (b.data,))
print("dtype: %s" % b.dtype)
print("size %s" % b.size)
print("b.tolist %s" % (b.tolist(),))
b.fill(9)
print("b.fill(9): %s" % (b,))
b[0, 0, 0] = 2
print("b[0, 0, 0] = 2: %s" % (b,))

print("")
print("np.full((2,2), 2.0)")
c = np.full((2,2), 2.0, int)

print("====================")
print("     operations")
print("====================")
print("c = %s" % (c,))
print("c + 2 = %s" % (c + 2,))
print("c - 2 = %s" % (c - 2,))
print("c * 2 = %s" % (c * 2,))
print("c / 2 = %s" % (c / 2,))
print("c ** 2 = %s" % (c ** 2,))
print("+c = %s" % (+c,))
print("-c = %s" % (-c,))

print("====================")
print("   trigonometric    ")
print("====================")
c = np.full((2,2), 0, int)
print("c = %s" % (c,))
print("np.sin(c) = %s" % (np.sin(c),))
print("np.cos(c) = %s" % (np.cos(c),))
print("np.tan(c) = %s" % (np.tan(c),))
print("np.arcsin(c) = %s" % (np.arcsin(c),))
print("np.arccos(c) = %s" % (np.arccos(c),))
print("np.arctan(c) = %s" % (np.arctan(c),))
print("np.sinh(c) = %s" % (np.sinh(c),))
print("np.cosh(c) = %s" % (np.cosh(c),))
print("np.tanh(c) = %s" % (np.tanh(c),))
print("np.sin([0,1]) = %s" % (np.sin([0,1]),))
print("np.sin((0,1)) = %s" % (np.sin((0,1)),))

print("====================")
print("      various       ")
print("====================")
ar = np.arange(3.0)
print("np.arange(3.0): %s, dtype: %s" % (ar, ar.dtype))
ar = np.arange(3)
print("np.arange(3): %s, dtype: %s" % (ar, ar.dtype))
ar = np.arange(3,7)
print("np.arange(3,7): %s, dtype: %s" % (ar, ar.dtype))
ar = np.arange(3,7, 2)
print("np.arange(3,7, 2): %s, dtype: %s" % (ar, ar.dtype))
ar = np.linspace(2.0, 3.0, num=5)
print("np.linspace(2.0, 3.0, num=5): %s" % (ar,))
ar = np.linspace(2.0, 3.0, num=5, endpoint=False)
print("np.linspace(2.0, 3.0, num=5, endpoint=False): %s" % (ar,))
ar = np.linspace(2.0, 3.0, num=5, retstep=True)
print("np.linspace(2.0, 3.0, num=5, retstep=True): %s" % (ar,))