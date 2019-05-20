import sys
from sympy import *

f12 = Rational(1, 2)

l1 = var("l1", positive=True)
l2 = var("l2", positive=True)
l3 = var("l3", positive=True)

dl1 = var("dl1", negative=False)
dl2 = var("dl2", negative=False)
dl3 = var("dl3", negative=False)

z1 = var("z1", real=True)
z2 = var("z2", real=True)
z3 = var("z3", real=True)

l1_ = l1 + dl1 * z1
l2_ = l2 + dl2 * z2
l3_ = l3 + dl3 * z3

t = var("t", negative=False)

q1 = Function("q1", real=True)(t) #var("q1", real=True)
q2 = Function("q2", real=True)(t) #var("q2", real=True)
q3 = Function("q3", real=True)(t) #var("q3", real=True)

dq1 = var("dq1", negative=False)
dq2 = var("dq2", negative=False)
dq3 = var("dq3", negative=False)

z4 = var("z4", real=True)
z5 = var("z5", real=True)
z6 = var("z6", real=True)

q1_ = q1 + dq1 * z4
q2_ = q2 + dq2 * z5
q3_ = q3 + dq3 * z6

m1 = var("m1", positive=True)
m2 = var("m2", positive=True)
m3 = var("m3", positive=True)
m4 = var("m4", positive=True)

dm1 = var("dm1", negative=False)
dm2 = var("dm2", negative=False)
dm3 = var("dm3", negative=False)
dm4 = var("dm4", negative=False)

z7 = var("z7", real=True)
z8 = var("z8", real=True)
z9 = var("z9", real=True)
z10 = var("z10", real=True)

m1_ = m1 + dm1 * z7
m2_ = m2 + dm2 * z8
m3_ = m3 + dm3 * z9
m4_ = m4 + dm4 * z10

I1 = m1_ * l1_ ** 2 / 12
I2 = m2_ * l2_ ** 2 / 12
I3 = m3_ * l3_ ** 2 / 12

x1 = l1_ * cos(q1_)
x2 = l1_ * cos(q1_) + l2_ * cos(q1_ + q2_)
x3 = l1_ * cos(q1_) + l2_ * cos(q1_ + q2_) + l3_ * cos(q1_ + q2_ + q3_)
y1 = l1_ * sin(q1_)
y2 = l1_ * sin(q1_) + l2_ * sin(q1_ + q2_)
y3 = l1_ * sin(q1_) + l2_ * sin(q1_ + q2_) + l3_ * sin(q1_ + q2_ + q3_)

q1sym = symbols("q1", real=True)
q2sym = symbols("q2", real=True)
q3sym = symbols("q3", real=True)

J = [[x3.diff(q1), x3.diff(q2), x3.diff(q3)],
     [y3.diff(q1), y3.diff(q2), y3.diff(q3)]]
J = [[d.subs(q1, q1sym).subs(q2, q2sym).subs(q3, q3sym) for d in r] for r in J]
print(J)

sys.exit(0)

x1g = f12 * l1_ * cos(q1_)
x2g = l1_ * cos(q1_) + f12 * l2_ * cos(q1_ + q2_)
x3g = l1_ * cos(q1_) + l2_ * cos(q1_ + q2_) + f12 * l3_ * cos(q1_ + q2_ + q3_)
x4g = l1_ * cos(q1_) + l2_ * cos(q1_ + q2_) + l3_ * cos(q1_ + q2_ + q3_)
y1g = f12 * l1_ * sin(q1_)
y2g = l1_ * sin(q1_) + f12 * l2_ * sin(q1_ + q2_)
y3g = l1_ * sin(q1_) + l2_ * sin(q1_ + q2_) + f12 * l3_ * sin(q1_ + q2_ + q3_)
y4g = l1_ * sin(q1_) + l2_ * sin(q1_ + q2_) + l3_ * sin(q1_ + q2_ + q3_)

K1 = (f12 * m1_ * x1g.diff(t) ** 2
        + f12 * m1_ * y1g.diff(t) ** 2
        + f12 * I1 * q1_.diff(t) ** 2)
K2 = (f12 * m2_ * x2g.diff(t) ** 2
        + f12 * m2_ * y2g.diff(t) ** 2
        + f12 * I2 * q2_.diff(t) ** 2)
K3 = (f12 * m3_ * x3g.diff(t) ** 2
        + f12 * m3_ * y3g.diff(t) ** 2
        + f12 * I3 * q3_.diff(t) ** 2)
K4 = (f12 * m4_ * x4g.diff(t) ** 2
        + f12 * m4_ * y4g.diff(t) ** 2)

# diffq# (# = 1, 2, 3) will be replaced with s#.
diffq1 = q1.diff(t)
diffq2 = q2.diff(t)
diffq3 = q3.diff(t)
s1 = var("s1", real=True)
s2 = var("s2", real=True)
s3 = var("s3", real=True)

K = K1 + K2 + K3 + K4
K_ = (K
        .subs(diffq1, s1)
        .subs(diffq2, s2)
        .subs(diffq3, s3))

# ddiffq# (# = 1, 2, 3) will be replaced with a#.
ddiffq1 = diffq1.diff(t)
ddiffq2 = diffq2.diff(t)
ddiffq3 = diffq3.diff(t)
a1 = var("a1", real=True)
a2 = var("a2", real=True)
a3 = var("a3", real=True)

pK1 = K.diff(diffq1).diff(t)
pK1_ = (pK1
        .subs(ddiffq1, a1)
        .subs(ddiffq2, a2)
        .subs(ddiffq3, a3)
        .subs(diffq1, s1)
        .subs(diffq2, s2)
        .subs(diffq3, s3)
        .subs(q1, q1sym)
        .subs(q2, q2sym)
        .subs(q3, q3sym)
        .expand()
        .collect(a1)
        .collect(a2)
        .collect(a3))
pK2 = K.diff(diffq2).diff(t)
pK2_ = (pK2
        .subs(ddiffq1, a1)
        .subs(ddiffq2, a2)
        .subs(ddiffq3, a3)
        .subs(diffq1, s1)
        .subs(diffq2, s2)
        .subs(diffq3, s3)
        .subs(q1, q1sym)
        .subs(q2, q2sym)
        .subs(q3, q3sym)
        .expand()
        .collect(a1)
        .collect(a2)
        .collect(a3))
pK3 = K.diff(diffq3).diff(t)
pK3_ = (pK3
        .subs(ddiffq1, a1)
        .subs(ddiffq2, a2)
        .subs(ddiffq3, a3)
        .subs(diffq1, s1)
        .subs(diffq2, s2)
        .subs(diffq3, s3)
        .subs(q1, q1sym)
        .subs(q2, q2sym)
        .subs(q3, q3sym)
        .expand()
        .collect(a1)
        .collect(a2)
        .collect(a3))

M = [[pK1_.args[0]/a1, pK1_.args[1]/a2, pK1_.args[2]/a3],
     [pK2_.args[0]/a1, pK2_.args[1]/a2, pK2_.args[2]/a3],
     [pK3_.args[0]/a1, pK3_.args[1]/a2, pK3_.args[2]/a3]]

sys.exit(0)
