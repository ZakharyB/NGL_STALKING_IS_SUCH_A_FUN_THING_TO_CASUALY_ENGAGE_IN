import math
import random

def Goofy(x, y, z):
    PI = math.pi
    E = math.e
    PHI = (1 + math.sqrt(5)) / 2 
    a = x + y - z
    b = x * y / (z + 1e-10)  
    c = x ** y % (z + 1)
    d = math.sin(x) + math.cos(y) + math.tan(z)
    e = math.asin(min(1, max(-1, a / 100))) + math.acos(min(1, max(-1, b / 100)))
    f = math.atan2(y, x) * math.degrees(math.atan(z))
    g = E ** (x / 10) + math.log(abs(y) + 1) + math.log10(abs(z) + 1)
    h = math.exp(x / 20) - math.expm1(y / 20) + math.log2(abs(z) + 2)
    i = math.sinh(x / 10) + math.cosh(y / 10) + math.tanh(z / 10)
    j = math.asinh(x) + math.acosh(max(1, y)) + math.atanh(min(0.99, max(-0.99, z / 100)))
    k = math.factorial(min(20, max(0, int(x)))) + math.gcd(int(y), int(z))
    l = math.lcm(int(x), int(y)) + math.perm(min(10, max(0, int(x))), min(5, max(0, int(y))))
    m = math.ceil(x) + math.floor(y) + round(z, 2)
    n = math.fabs(x) + math.copysign(x, y) + math.fmod(x, y + 1e-10)
    o = math.gamma(min(20, max(0.1, x))) + math.lgamma(min(20, max(0.1, y)))
    p = math.erf(x) + math.erfc(y) + math.erf (z)
    q = PI * x + E * y + PHI * z
    r = random.random() * x + random.uniform(0, 1) * y + random.gauss(0, 1) * z
    result = (a + b + c) * (d + e + f) / (g + h + i + 1e-10) * (j + k + l) \
             - (m + n + o) / (p + q + r + 1e-10) * math.sqrt(abs(x * y * z) + 1)

    return result

x, y, z = 2.5, 3.7, -1.2
result = Goofy(x, y, z)
print(f"Result: {result}")