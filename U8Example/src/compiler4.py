from z3 import *
d1_0 = Real('d1_0')
d1_1 = Real('d1_1')
t1_0 = Real('t1_0')
t1_update_0 = Real('t1_update_0')
t1_1 = Real('t1_1')
t1_update_1 = Real('t1_update_1')
d2_0 = Real('d2_0')
d2_1 = Real('d2_1')
d2_2 = Real('d2_2')
t2_0 = Real('t2_0')
t2_update_0 = Real('t2_update_0')
t2_1 = Real('t2_1')
t2_update_1 = Real('t2_update_1')
t2_2 = Real('t2_2')
t2_update_2 = Real('t2_update_2')
d4_0 = Real('d4_0')
d4_1 = Real('d4_1')
s = Solver()
s.add(d4_0 >= 5.0)
s.add(d4_0 <= 5.0)
s.add(d4_1 >= 11.0)
s.add(d4_1 <= 11.0)
s.add()
s.add(d2_0 >= 4.0)
s.add(d2_0 <= 4.5)
s.add(d2_1 >= 8.0)
s.add(d2_1 <= 8.5)
s.add(d2_2 >= 12.0)
s.add(d2_2 <= 12.5)
s.add()
s.add(t1_0 < t1_update_0)
s.add(t2_1 < t2_update_1)
s.add()
s.add(t1_0 < d1_0)
s.add(t1_1 < d1_1)
s.add(t2_0 < d2_0)
s.add(t2_1 < d2_1)
s.add(t2_2 < d2_2)
s.add()
s.add(t1_0 < t1_1)
s.add(t2_0 < t2_1)
s.add(t2_1 < t2_2)
s.add()
s.add(t1_update_0 < d4_0)
s.add(t1_update_1 > d4_0)
s.add(t1_update_1 < d4_1)
s.add()
s.add(t2_update_0 < t1_1)
s.add(t2_update_1 > t1_1)
s.add(t2_update_0 > t1_0)
s.add()
s.add(Or(d1_0 + 0.25 <= d1_1 , d1_1 + 0.25 <= d1_0))
s.add(Or(d1_0 + 0.25 <= t1_0 , t1_0 + 0.20 <= d1_0))
s.add(Or(d1_0 + 0.25 <= t1_update_0 , t1_update_0 + 0.05 <= d1_0))
s.add(Or(d1_0 + 0.25 <= t1_1 , t1_1 + 0.20 <= d1_0))
s.add(Or(d1_0 + 0.25 <= t1_update_1 , t1_update_1 + 0.05 <= d1_0))
s.add(Or(d1_0 + 0.25 <= d2_0 , d2_0 + 0.5 <= d1_0))
s.add(Or(d1_0 + 0.25 <= d2_1 , d2_1 + 0.5 <= d1_0))
s.add(Or(d1_0 + 0.25 <= d2_2 , d2_2 + 0.5 <= d1_0))
s.add(Or(d1_0 + 0.25 <= t2_0 , t2_0 + 0.75 <= d1_0))
s.add(Or(d1_0 + 0.25 <= t2_update_0 , t2_update_0 + 0.25 <= d1_0))
s.add(Or(d1_0 + 0.25 <= t2_1 , t2_1 + 0.75 <= d1_0))
s.add(Or(d1_0 + 0.25 <= t2_update_1 , t2_update_1 + 0.25 <= d1_0))
s.add(Or(d1_0 + 0.25 <= t2_2 , t2_2 + 0.75 <= d1_0))
s.add(Or(d1_0 + 0.25 <= t2_update_2 , t2_update_2 + 0.25 <= d1_0))
s.add(Or(d1_0 + 0.25 <= d4_0 , d4_0 + 1 <= d1_0))
s.add(Or(d1_0 + 0.25 <= d4_1 , d4_1 + 1 <= d1_0))
s.add(Or(d1_1 + 0.25 <= d1_0 , d1_0 + 0.25 <= d1_1))
s.add(Or(d1_1 + 0.25 <= t1_0 , t1_0 + 0.20 <= d1_1))
s.add(Or(d1_1 + 0.25 <= t1_update_0 , t1_update_0 + 0.05 <= d1_1))
s.add(Or(d1_1 + 0.25 <= t1_1 , t1_1 + 0.20 <= d1_1))
s.add(Or(d1_1 + 0.25 <= t1_update_1 , t1_update_1 + 0.05 <= d1_1))
s.add(Or(d1_1 + 0.25 <= d2_0 , d2_0 + 0.5 <= d1_1))
s.add(Or(d1_1 + 0.25 <= d2_1 , d2_1 + 0.5 <= d1_1))
s.add(Or(d1_1 + 0.25 <= d2_2 , d2_2 + 0.5 <= d1_1))
s.add(Or(d1_1 + 0.25 <= t2_0 , t2_0 + 0.75 <= d1_1))
s.add(Or(d1_1 + 0.25 <= t2_update_0 , t2_update_0 + 0.25 <= d1_1))
s.add(Or(d1_1 + 0.25 <= t2_1 , t2_1 + 0.75 <= d1_1))
s.add(Or(d1_1 + 0.25 <= t2_update_1 , t2_update_1 + 0.25 <= d1_1))
s.add(Or(d1_1 + 0.25 <= t2_2 , t2_2 + 0.75 <= d1_1))
s.add(Or(d1_1 + 0.25 <= t2_update_2 , t2_update_2 + 0.25 <= d1_1))
s.add(Or(d1_1 + 0.25 <= d4_0 , d4_0 + 1 <= d1_1))
s.add(Or(d1_1 + 0.25 <= d4_1 , d4_1 + 1 <= d1_1))
s.add(Or(t1_0 + 0.20 <= d1_0 , d1_0 + 0.25 <= t1_0))
s.add(Or(t1_0 + 0.20 <= d1_1 , d1_1 + 0.25 <= t1_0))
s.add(Or(t1_0 + 0.20 <= t1_update_0 , t1_update_0 + 0.05 <= t1_0))
s.add(Or(t1_0 + 0.20 <= t1_1 , t1_1 + 0.20 <= t1_0))
s.add(Or(t1_0 + 0.20 <= t1_update_1 , t1_update_1 + 0.05 <= t1_0))
s.add(Or(t1_0 + 0.20 <= d2_0 , d2_0 + 0.5 <= t1_0))
s.add(Or(t1_0 + 0.20 <= d2_1 , d2_1 + 0.5 <= t1_0))
s.add(Or(t1_0 + 0.20 <= d2_2 , d2_2 + 0.5 <= t1_0))
s.add(Or(t1_0 + 0.20 <= t2_0 , t2_0 + 0.75 <= t1_0))
s.add(Or(t1_0 + 0.20 <= t2_update_0 , t2_update_0 + 0.25 <= t1_0))
s.add(Or(t1_0 + 0.20 <= t2_1 , t2_1 + 0.75 <= t1_0))
s.add(Or(t1_0 + 0.20 <= t2_update_1 , t2_update_1 + 0.25 <= t1_0))
s.add(Or(t1_0 + 0.20 <= t2_2 , t2_2 + 0.75 <= t1_0))
s.add(Or(t1_0 + 0.20 <= t2_update_2 , t2_update_2 + 0.25 <= t1_0))
s.add(Or(t1_0 + 0.20 <= d4_0 , d4_0 + 1 <= t1_0))
s.add(Or(t1_0 + 0.20 <= d4_1 , d4_1 + 1 <= t1_0))
s.add(Or(t1_update_0 + 0.05 <= d1_0 , d1_0 + 0.25 <= t1_update_0))
s.add(Or(t1_update_0 + 0.05 <= d1_1 , d1_1 + 0.25 <= t1_update_0))
s.add(Or(t1_update_0 + 0.05 <= t1_0 , t1_0 + 0.20 <= t1_update_0))
s.add(Or(t1_update_0 + 0.05 <= t1_1 , t1_1 + 0.20 <= t1_update_0))
s.add(Or(t1_update_0 + 0.05 <= t1_update_1 , t1_update_1 + 0.05 <= t1_update_0))
s.add(Or(t1_update_0 + 0.05 <= d2_0 , d2_0 + 0.5 <= t1_update_0))
s.add(Or(t1_update_0 + 0.05 <= d2_1 , d2_1 + 0.5 <= t1_update_0))
s.add(Or(t1_update_0 + 0.05 <= d2_2 , d2_2 + 0.5 <= t1_update_0))
s.add(Or(t1_update_0 + 0.05 <= t2_0 , t2_0 + 0.75 <= t1_update_0))
s.add(Or(t1_update_0 + 0.05 <= t2_update_0 , t2_update_0 + 0.25 <= t1_update_0))
s.add(Or(t1_update_0 + 0.05 <= t2_1 , t2_1 + 0.75 <= t1_update_0))
s.add(Or(t1_update_0 + 0.05 <= t2_update_1 , t2_update_1 + 0.25 <= t1_update_0))
s.add(Or(t1_update_0 + 0.05 <= t2_2 , t2_2 + 0.75 <= t1_update_0))
s.add(Or(t1_update_0 + 0.05 <= t2_update_2 , t2_update_2 + 0.25 <= t1_update_0))
s.add(Or(t1_update_0 + 0.05 <= d4_0 , d4_0 + 1 <= t1_update_0))
s.add(Or(t1_update_0 + 0.05 <= d4_1 , d4_1 + 1 <= t1_update_0))
s.add(Or(t1_1 + 0.20 <= d1_0 , d1_0 + 0.25 <= t1_1))
s.add(Or(t1_1 + 0.20 <= d1_1 , d1_1 + 0.25 <= t1_1))
s.add(Or(t1_1 + 0.20 <= t1_0 , t1_0 + 0.20 <= t1_1))
s.add(Or(t1_1 + 0.20 <= t1_update_0 , t1_update_0 + 0.05 <= t1_1))
s.add(Or(t1_1 + 0.20 <= t1_update_1 , t1_update_1 + 0.05 <= t1_1))
s.add(Or(t1_1 + 0.20 <= d2_0 , d2_0 + 0.5 <= t1_1))
s.add(Or(t1_1 + 0.20 <= d2_1 , d2_1 + 0.5 <= t1_1))
s.add(Or(t1_1 + 0.20 <= d2_2 , d2_2 + 0.5 <= t1_1))
s.add(Or(t1_1 + 0.20 <= t2_0 , t2_0 + 0.75 <= t1_1))
s.add(Or(t1_1 + 0.20 <= t2_update_0 , t2_update_0 + 0.25 <= t1_1))
s.add(Or(t1_1 + 0.20 <= t2_1 , t2_1 + 0.75 <= t1_1))
s.add(Or(t1_1 + 0.20 <= t2_update_1 , t2_update_1 + 0.25 <= t1_1))
s.add(Or(t1_1 + 0.20 <= t2_2 , t2_2 + 0.75 <= t1_1))
s.add(Or(t1_1 + 0.20 <= t2_update_2 , t2_update_2 + 0.25 <= t1_1))
s.add(Or(t1_1 + 0.20 <= d4_0 , d4_0 + 1 <= t1_1))
s.add(Or(t1_1 + 0.20 <= d4_1 , d4_1 + 1 <= t1_1))
s.add(Or(t1_update_1 + 0.05 <= d1_0 , d1_0 + 0.25 <= t1_update_1))
s.add(Or(t1_update_1 + 0.05 <= d1_1 , d1_1 + 0.25 <= t1_update_1))
s.add(Or(t1_update_1 + 0.05 <= t1_0 , t1_0 + 0.20 <= t1_update_1))
s.add(Or(t1_update_1 + 0.05 <= t1_update_0 , t1_update_0 + 0.05 <= t1_update_1))
s.add(Or(t1_update_1 + 0.05 <= t1_1 , t1_1 + 0.20 <= t1_update_1))
s.add(Or(t1_update_1 + 0.05 <= d2_0 , d2_0 + 0.5 <= t1_update_1))
s.add(Or(t1_update_1 + 0.05 <= d2_1 , d2_1 + 0.5 <= t1_update_1))
s.add(Or(t1_update_1 + 0.05 <= d2_2 , d2_2 + 0.5 <= t1_update_1))
s.add(Or(t1_update_1 + 0.05 <= t2_0 , t2_0 + 0.75 <= t1_update_1))
s.add(Or(t1_update_1 + 0.05 <= t2_update_0 , t2_update_0 + 0.25 <= t1_update_1))
s.add(Or(t1_update_1 + 0.05 <= t2_1 , t2_1 + 0.75 <= t1_update_1))
s.add(Or(t1_update_1 + 0.05 <= t2_update_1 , t2_update_1 + 0.25 <= t1_update_1))
s.add(Or(t1_update_1 + 0.05 <= t2_2 , t2_2 + 0.75 <= t1_update_1))
s.add(Or(t1_update_1 + 0.05 <= t2_update_2 , t2_update_2 + 0.25 <= t1_update_1))
s.add(Or(t1_update_1 + 0.05 <= d4_0 , d4_0 + 1 <= t1_update_1))
s.add(Or(t1_update_1 + 0.05 <= d4_1 , d4_1 + 1 <= t1_update_1))
s.add(Or(d2_0 + 0.5 <= d1_0 , d1_0 + 0.25 <= d2_0))
s.add(Or(d2_0 + 0.5 <= d1_1 , d1_1 + 0.25 <= d2_0))
s.add(Or(d2_0 + 0.5 <= t1_0 , t1_0 + 0.20 <= d2_0))
s.add(Or(d2_0 + 0.5 <= t1_update_0 , t1_update_0 + 0.05 <= d2_0))
s.add(Or(d2_0 + 0.5 <= t1_1 , t1_1 + 0.20 <= d2_0))
s.add(Or(d2_0 + 0.5 <= t1_update_1 , t1_update_1 + 0.05 <= d2_0))
s.add(Or(d2_0 + 0.5 <= d2_1 , d2_1 + 0.5 <= d2_0))
s.add(Or(d2_0 + 0.5 <= d2_2 , d2_2 + 0.5 <= d2_0))
s.add(Or(d2_0 + 0.5 <= t2_0 , t2_0 + 0.75 <= d2_0))
s.add(Or(d2_0 + 0.5 <= t2_update_0 , t2_update_0 + 0.25 <= d2_0))
s.add(Or(d2_0 + 0.5 <= t2_1 , t2_1 + 0.75 <= d2_0))
s.add(Or(d2_0 + 0.5 <= t2_update_1 , t2_update_1 + 0.25 <= d2_0))
s.add(Or(d2_0 + 0.5 <= t2_2 , t2_2 + 0.75 <= d2_0))
s.add(Or(d2_0 + 0.5 <= t2_update_2 , t2_update_2 + 0.25 <= d2_0))
s.add(Or(d2_0 + 0.5 <= d4_0 , d4_0 + 1 <= d2_0))
s.add(Or(d2_0 + 0.5 <= d4_1 , d4_1 + 1 <= d2_0))
s.add(Or(d2_1 + 0.5 <= d1_0 , d1_0 + 0.25 <= d2_1))
s.add(Or(d2_1 + 0.5 <= d1_1 , d1_1 + 0.25 <= d2_1))
s.add(Or(d2_1 + 0.5 <= t1_0 , t1_0 + 0.20 <= d2_1))
s.add(Or(d2_1 + 0.5 <= t1_update_0 , t1_update_0 + 0.05 <= d2_1))
s.add(Or(d2_1 + 0.5 <= t1_1 , t1_1 + 0.20 <= d2_1))
s.add(Or(d2_1 + 0.5 <= t1_update_1 , t1_update_1 + 0.05 <= d2_1))
s.add(Or(d2_1 + 0.5 <= d2_0 , d2_0 + 0.5 <= d2_1))
s.add(Or(d2_1 + 0.5 <= d2_2 , d2_2 + 0.5 <= d2_1))
s.add(Or(d2_1 + 0.5 <= t2_0 , t2_0 + 0.75 <= d2_1))
s.add(Or(d2_1 + 0.5 <= t2_update_0 , t2_update_0 + 0.25 <= d2_1))
s.add(Or(d2_1 + 0.5 <= t2_1 , t2_1 + 0.75 <= d2_1))
s.add(Or(d2_1 + 0.5 <= t2_update_1 , t2_update_1 + 0.25 <= d2_1))
s.add(Or(d2_1 + 0.5 <= t2_2 , t2_2 + 0.75 <= d2_1))
s.add(Or(d2_1 + 0.5 <= t2_update_2 , t2_update_2 + 0.25 <= d2_1))
s.add(Or(d2_1 + 0.5 <= d4_0 , d4_0 + 1 <= d2_1))
s.add(Or(d2_1 + 0.5 <= d4_1 , d4_1 + 1 <= d2_1))
s.add(Or(d2_2 + 0.5 <= d1_0 , d1_0 + 0.25 <= d2_2))
s.add(Or(d2_2 + 0.5 <= d1_1 , d1_1 + 0.25 <= d2_2))
s.add(Or(d2_2 + 0.5 <= t1_0 , t1_0 + 0.20 <= d2_2))
s.add(Or(d2_2 + 0.5 <= t1_update_0 , t1_update_0 + 0.05 <= d2_2))
s.add(Or(d2_2 + 0.5 <= t1_1 , t1_1 + 0.20 <= d2_2))
s.add(Or(d2_2 + 0.5 <= t1_update_1 , t1_update_1 + 0.05 <= d2_2))
s.add(Or(d2_2 + 0.5 <= d2_0 , d2_0 + 0.5 <= d2_2))
s.add(Or(d2_2 + 0.5 <= d2_1 , d2_1 + 0.5 <= d2_2))
s.add(Or(d2_2 + 0.5 <= t2_0 , t2_0 + 0.75 <= d2_2))
s.add(Or(d2_2 + 0.5 <= t2_update_0 , t2_update_0 + 0.25 <= d2_2))
s.add(Or(d2_2 + 0.5 <= t2_1 , t2_1 + 0.75 <= d2_2))
s.add(Or(d2_2 + 0.5 <= t2_update_1 , t2_update_1 + 0.25 <= d2_2))
s.add(Or(d2_2 + 0.5 <= t2_2 , t2_2 + 0.75 <= d2_2))
s.add(Or(d2_2 + 0.5 <= t2_update_2 , t2_update_2 + 0.25 <= d2_2))
s.add(Or(d2_2 + 0.5 <= d4_0 , d4_0 + 1 <= d2_2))
s.add(Or(d2_2 + 0.5 <= d4_1 , d4_1 + 1 <= d2_2))
s.add(Or(t2_0 + 0.75 <= d1_0 , d1_0 + 0.25 <= t2_0))
s.add(Or(t2_0 + 0.75 <= d1_1 , d1_1 + 0.25 <= t2_0))
s.add(Or(t2_0 + 0.75 <= t1_0 , t1_0 + 0.20 <= t2_0))
s.add(Or(t2_0 + 0.75 <= t1_update_0 , t1_update_0 + 0.05 <= t2_0))
s.add(Or(t2_0 + 0.75 <= t1_1 , t1_1 + 0.20 <= t2_0))
s.add(Or(t2_0 + 0.75 <= t1_update_1 , t1_update_1 + 0.05 <= t2_0))
s.add(Or(t2_0 + 0.75 <= d2_0 , d2_0 + 0.5 <= t2_0))
s.add(Or(t2_0 + 0.75 <= d2_1 , d2_1 + 0.5 <= t2_0))
s.add(Or(t2_0 + 0.75 <= d2_2 , d2_2 + 0.5 <= t2_0))
s.add(Or(t2_0 + 0.75 <= t2_update_0 , t2_update_0 + 0.25 <= t2_0))
s.add(Or(t2_0 + 0.75 <= t2_1 , t2_1 + 0.75 <= t2_0))
s.add(Or(t2_0 + 0.75 <= t2_update_1 , t2_update_1 + 0.25 <= t2_0))
s.add(Or(t2_0 + 0.75 <= t2_2 , t2_2 + 0.75 <= t2_0))
s.add(Or(t2_0 + 0.75 <= t2_update_2 , t2_update_2 + 0.25 <= t2_0))
s.add(Or(t2_0 + 0.75 <= d4_0 , d4_0 + 1 <= t2_0))
s.add(Or(t2_0 + 0.75 <= d4_1 , d4_1 + 1 <= t2_0))
s.add(Or(t2_update_0 + 0.25 <= d1_0 , d1_0 + 0.25 <= t2_update_0))
s.add(Or(t2_update_0 + 0.25 <= d1_1 , d1_1 + 0.25 <= t2_update_0))
s.add(Or(t2_update_0 + 0.25 <= t1_0 , t1_0 + 0.20 <= t2_update_0))
s.add(Or(t2_update_0 + 0.25 <= t1_update_0 , t1_update_0 + 0.05 <= t2_update_0))
s.add(Or(t2_update_0 + 0.25 <= t1_1 , t1_1 + 0.20 <= t2_update_0))
s.add(Or(t2_update_0 + 0.25 <= t1_update_1 , t1_update_1 + 0.05 <= t2_update_0))
s.add(Or(t2_update_0 + 0.25 <= d2_0 , d2_0 + 0.5 <= t2_update_0))
s.add(Or(t2_update_0 + 0.25 <= d2_1 , d2_1 + 0.5 <= t2_update_0))
s.add(Or(t2_update_0 + 0.25 <= d2_2 , d2_2 + 0.5 <= t2_update_0))
s.add(Or(t2_update_0 + 0.25 <= t2_0 , t2_0 + 0.75 <= t2_update_0))
s.add(Or(t2_update_0 + 0.25 <= t2_1 , t2_1 + 0.75 <= t2_update_0))
s.add(Or(t2_update_0 + 0.25 <= t2_update_1 , t2_update_1 + 0.25 <= t2_update_0))
s.add(Or(t2_update_0 + 0.25 <= t2_2 , t2_2 + 0.75 <= t2_update_0))
s.add(Or(t2_update_0 + 0.25 <= t2_update_2 , t2_update_2 + 0.25 <= t2_update_0))
s.add(Or(t2_update_0 + 0.25 <= d4_0 , d4_0 + 1 <= t2_update_0))
s.add(Or(t2_update_0 + 0.25 <= d4_1 , d4_1 + 1 <= t2_update_0))
s.add(Or(t2_1 + 0.75 <= d1_0 , d1_0 + 0.25 <= t2_1))
s.add(Or(t2_1 + 0.75 <= d1_1 , d1_1 + 0.25 <= t2_1))
s.add(Or(t2_1 + 0.75 <= t1_0 , t1_0 + 0.20 <= t2_1))
s.add(Or(t2_1 + 0.75 <= t1_update_0 , t1_update_0 + 0.05 <= t2_1))
s.add(Or(t2_1 + 0.75 <= t1_1 , t1_1 + 0.20 <= t2_1))
s.add(Or(t2_1 + 0.75 <= t1_update_1 , t1_update_1 + 0.05 <= t2_1))
s.add(Or(t2_1 + 0.75 <= d2_0 , d2_0 + 0.5 <= t2_1))
s.add(Or(t2_1 + 0.75 <= d2_1 , d2_1 + 0.5 <= t2_1))
s.add(Or(t2_1 + 0.75 <= d2_2 , d2_2 + 0.5 <= t2_1))
s.add(Or(t2_1 + 0.75 <= t2_0 , t2_0 + 0.75 <= t2_1))
s.add(Or(t2_1 + 0.75 <= t2_update_0 , t2_update_0 + 0.25 <= t2_1))
s.add(Or(t2_1 + 0.75 <= t2_update_1 , t2_update_1 + 0.25 <= t2_1))
s.add(Or(t2_1 + 0.75 <= t2_2 , t2_2 + 0.75 <= t2_1))
s.add(Or(t2_1 + 0.75 <= t2_update_2 , t2_update_2 + 0.25 <= t2_1))
s.add(Or(t2_1 + 0.75 <= d4_0 , d4_0 + 1 <= t2_1))
s.add(Or(t2_1 + 0.75 <= d4_1 , d4_1 + 1 <= t2_1))
s.add(Or(t2_update_1 + 0.25 <= d1_0 , d1_0 + 0.25 <= t2_update_1))
s.add(Or(t2_update_1 + 0.25 <= d1_1 , d1_1 + 0.25 <= t2_update_1))
s.add(Or(t2_update_1 + 0.25 <= t1_0 , t1_0 + 0.20 <= t2_update_1))
s.add(Or(t2_update_1 + 0.25 <= t1_update_0 , t1_update_0 + 0.05 <= t2_update_1))
s.add(Or(t2_update_1 + 0.25 <= t1_1 , t1_1 + 0.20 <= t2_update_1))
s.add(Or(t2_update_1 + 0.25 <= t1_update_1 , t1_update_1 + 0.05 <= t2_update_1))
s.add(Or(t2_update_1 + 0.25 <= d2_0 , d2_0 + 0.5 <= t2_update_1))
s.add(Or(t2_update_1 + 0.25 <= d2_1 , d2_1 + 0.5 <= t2_update_1))
s.add(Or(t2_update_1 + 0.25 <= d2_2 , d2_2 + 0.5 <= t2_update_1))
s.add(Or(t2_update_1 + 0.25 <= t2_0 , t2_0 + 0.75 <= t2_update_1))
s.add(Or(t2_update_1 + 0.25 <= t2_update_0 , t2_update_0 + 0.25 <= t2_update_1))
s.add(Or(t2_update_1 + 0.25 <= t2_1 , t2_1 + 0.75 <= t2_update_1))
s.add(Or(t2_update_1 + 0.25 <= t2_2 , t2_2 + 0.75 <= t2_update_1))
s.add(Or(t2_update_1 + 0.25 <= t2_update_2 , t2_update_2 + 0.25 <= t2_update_1))
s.add(Or(t2_update_1 + 0.25 <= d4_0 , d4_0 + 1 <= t2_update_1))
s.add(Or(t2_update_1 + 0.25 <= d4_1 , d4_1 + 1 <= t2_update_1))
s.add(Or(t2_2 + 0.75 <= d1_0 , d1_0 + 0.25 <= t2_2))
s.add(Or(t2_2 + 0.75 <= d1_1 , d1_1 + 0.25 <= t2_2))
s.add(Or(t2_2 + 0.75 <= t1_0 , t1_0 + 0.20 <= t2_2))
s.add(Or(t2_2 + 0.75 <= t1_update_0 , t1_update_0 + 0.05 <= t2_2))
s.add(Or(t2_2 + 0.75 <= t1_1 , t1_1 + 0.20 <= t2_2))
s.add(Or(t2_2 + 0.75 <= t1_update_1 , t1_update_1 + 0.05 <= t2_2))
s.add(Or(t2_2 + 0.75 <= d2_0 , d2_0 + 0.5 <= t2_2))
s.add(Or(t2_2 + 0.75 <= d2_1 , d2_1 + 0.5 <= t2_2))
s.add(Or(t2_2 + 0.75 <= d2_2 , d2_2 + 0.5 <= t2_2))
s.add(Or(t2_2 + 0.75 <= t2_0 , t2_0 + 0.75 <= t2_2))
s.add(Or(t2_2 + 0.75 <= t2_update_0 , t2_update_0 + 0.25 <= t2_2))
s.add(Or(t2_2 + 0.75 <= t2_1 , t2_1 + 0.75 <= t2_2))
s.add(Or(t2_2 + 0.75 <= t2_update_1 , t2_update_1 + 0.25 <= t2_2))
s.add(Or(t2_2 + 0.75 <= t2_update_2 , t2_update_2 + 0.25 <= t2_2))
s.add(Or(t2_2 + 0.75 <= d4_0 , d4_0 + 1 <= t2_2))
s.add(Or(t2_2 + 0.75 <= d4_1 , d4_1 + 1 <= t2_2))
s.add(Or(t2_update_2 + 0.25 <= d1_0 , d1_0 + 0.25 <= t2_update_2))
s.add(Or(t2_update_2 + 0.25 <= d1_1 , d1_1 + 0.25 <= t2_update_2))
s.add(Or(t2_update_2 + 0.25 <= t1_0 , t1_0 + 0.20 <= t2_update_2))
s.add(Or(t2_update_2 + 0.25 <= t1_update_0 , t1_update_0 + 0.05 <= t2_update_2))
s.add(Or(t2_update_2 + 0.25 <= t1_1 , t1_1 + 0.20 <= t2_update_2))
s.add(Or(t2_update_2 + 0.25 <= t1_update_1 , t1_update_1 + 0.05 <= t2_update_2))
s.add(Or(t2_update_2 + 0.25 <= d2_0 , d2_0 + 0.5 <= t2_update_2))
s.add(Or(t2_update_2 + 0.25 <= d2_1 , d2_1 + 0.5 <= t2_update_2))
s.add(Or(t2_update_2 + 0.25 <= d2_2 , d2_2 + 0.5 <= t2_update_2))
s.add(Or(t2_update_2 + 0.25 <= t2_0 , t2_0 + 0.75 <= t2_update_2))
s.add(Or(t2_update_2 + 0.25 <= t2_update_0 , t2_update_0 + 0.25 <= t2_update_2))
s.add(Or(t2_update_2 + 0.25 <= t2_1 , t2_1 + 0.75 <= t2_update_2))
s.add(Or(t2_update_2 + 0.25 <= t2_update_1 , t2_update_1 + 0.25 <= t2_update_2))
s.add(Or(t2_update_2 + 0.25 <= t2_2 , t2_2 + 0.75 <= t2_update_2))
s.add(Or(t2_update_2 + 0.25 <= d4_0 , d4_0 + 1 <= t2_update_2))
s.add(Or(t2_update_2 + 0.25 <= d4_1 , d4_1 + 1 <= t2_update_2))
s.add(Or(d4_0 + 1 <= d1_0 , d1_0 + 0.25 <= d4_0))
s.add(Or(d4_0 + 1 <= d1_1 , d1_1 + 0.25 <= d4_0))
s.add(Or(d4_0 + 1 <= t1_0 , t1_0 + 0.20 <= d4_0))
s.add(Or(d4_0 + 1 <= t1_update_0 , t1_update_0 + 0.05 <= d4_0))
s.add(Or(d4_0 + 1 <= t1_1 , t1_1 + 0.20 <= d4_0))
s.add(Or(d4_0 + 1 <= t1_update_1 , t1_update_1 + 0.05 <= d4_0))
s.add(Or(d4_0 + 1 <= d2_0 , d2_0 + 0.5 <= d4_0))
s.add(Or(d4_0 + 1 <= d2_1 , d2_1 + 0.5 <= d4_0))
s.add(Or(d4_0 + 1 <= d2_2 , d2_2 + 0.5 <= d4_0))
s.add(Or(d4_0 + 1 <= t2_0 , t2_0 + 0.75 <= d4_0))
s.add(Or(d4_0 + 1 <= t2_update_0 , t2_update_0 + 0.25 <= d4_0))
s.add(Or(d4_0 + 1 <= t2_1 , t2_1 + 0.75 <= d4_0))
s.add(Or(d4_0 + 1 <= t2_update_1 , t2_update_1 + 0.25 <= d4_0))
s.add(Or(d4_0 + 1 <= t2_2 , t2_2 + 0.75 <= d4_0))
s.add(Or(d4_0 + 1 <= t2_update_2 , t2_update_2 + 0.25 <= d4_0))
s.add(Or(d4_0 + 1 <= d4_1 , d4_1 + 1 <= d4_0))
s.add(Or(d4_1 + 1 <= d1_0 , d1_0 + 0.25 <= d4_1))
s.add(Or(d4_1 + 1 <= d1_1 , d1_1 + 0.25 <= d4_1))
s.add(Or(d4_1 + 1 <= t1_0 , t1_0 + 0.20 <= d4_1))
s.add(Or(d4_1 + 1 <= t1_update_0 , t1_update_0 + 0.05 <= d4_1))
s.add(Or(d4_1 + 1 <= t1_1 , t1_1 + 0.20 <= d4_1))
s.add(Or(d4_1 + 1 <= t1_update_1 , t1_update_1 + 0.05 <= d4_1))
s.add(Or(d4_1 + 1 <= d2_0 , d2_0 + 0.5 <= d4_1))
s.add(Or(d4_1 + 1 <= d2_1 , d2_1 + 0.5 <= d4_1))
s.add(Or(d4_1 + 1 <= d2_2 , d2_2 + 0.5 <= d4_1))
s.add(Or(d4_1 + 1 <= t2_0 , t2_0 + 0.75 <= d4_1))
s.add(Or(d4_1 + 1 <= t2_update_0 , t2_update_0 + 0.25 <= d4_1))
s.add(Or(d4_1 + 1 <= t2_1 , t2_1 + 0.75 <= d4_1))
s.add(Or(d4_1 + 1 <= t2_update_1 , t2_update_1 + 0.25 <= d4_1))
s.add(Or(d4_1 + 1 <= t2_2 , t2_2 + 0.75 <= d4_1))
s.add(Or(d4_1 + 1 <= t2_update_2 , t2_update_2 + 0.25 <= d4_1))
s.add(Or(d4_1 + 1 <= d4_0 , d4_0 + 1 <= d4_1))
print(s.check())
print(s.model())
outFile = open("scehule_specification.txt", "w")
outFile.writelines(str(s.model()))
