from z3 import *
input_t1_0 = Real('input_t1_0')
t1_0 = Real('t1_0')
actuation_0 = Real('actuation_0')
input_t2_0 = Real('input_t2_0')
input_t2_1 = Real('input_t2_1')
t2_0 = Real('t2_0')
t2_1 = Real('t2_1')
actuation2_0 = Real('actuation2_0')
actuation2_1 = Real('actuation2_1')
s = Solver()
s.add(actuation_0 >= 14.0)
s.add(actuation_0 + 1.0 <= 16.0)
s.add(actuation2_0 >= 6.0)
s.add(actuation2_0 + 0.5 <= 8.0)
s.add(actuation2_1 >= 14.0)
s.add(actuation2_1 + 0.5 <= 16.0)
s.add()
s.add(input_t1_0 >= 0.0)
s.add(input_t1_0 + 1.0 <= 2.0)
s.add(input_t2_0 >= 0.0)
s.add(input_t2_0 + 0.5 <= 2.0)
s.add(input_t2_1 >= 8.0)
s.add(input_t2_1 + 0.5 <= 10.0)
s.add()
s.add(input_t1_0 + 1.0 <= t1_0)
s.add(input_t2_0 + 0.5 <= t2_0)
s.add(t2_0 + 1.0 <= input_t2_1)
s.add(input_t2_1 + 0.5 <= t2_1)
s.add()
s.add(t2_0 < t2_1)
s.add(input_t2_0 < input_t2_1)
s.add(actuation2_0 < actuation2_1)
s.add()
s.add(t1_0 + 2.0 <= actuation_0)
s.add(t1_0 + 2.0 <= actuation_0)
s.add(t2_0 + 1.0 <= actuation2_0)
s.add(t2_1 >= actuation2_0 + 0.5)
s.add(t2_1 + 1.0 <= actuation2_1)
s.add()
s.add()
s.add(Or(input_t1_0 + 1 <= t1_0 , t1_0 + 2 <= input_t1_0))
s.add(Or(input_t1_0 + 1 <= actuation_0 , actuation_0 + 1 <= input_t1_0))
s.add(Or(input_t1_0 + 1 <= input_t2_0 , input_t2_0 + 0.5 <= input_t1_0))
s.add(Or(input_t1_0 + 1 <= input_t2_1 , input_t2_1 + 0.5 <= input_t1_0))
s.add(Or(input_t1_0 + 1 <= t2_0 , t2_0 + 1 <= input_t1_0))
s.add(Or(input_t1_0 + 1 <= t2_1 , t2_1 + 1 <= input_t1_0))
s.add(Or(input_t1_0 + 1 <= actuation2_0 , actuation2_0 + 0.5 <= input_t1_0))
s.add(Or(input_t1_0 + 1 <= actuation2_1 , actuation2_1 + 0.5 <= input_t1_0))
s.add(Or(t1_0 + 2 <= input_t1_0 , input_t1_0 + 1 <= t1_0))
s.add(Or(t1_0 + 2 <= actuation_0 , actuation_0 + 1 <= t1_0))
s.add(Or(t1_0 + 2 <= input_t2_0 , input_t2_0 + 0.5 <= t1_0))
s.add(Or(t1_0 + 2 <= input_t2_1 , input_t2_1 + 0.5 <= t1_0))
s.add(Or(t1_0 + 2 <= t2_0 , t2_0 + 1 <= t1_0))
s.add(Or(t1_0 + 2 <= t2_1 , t2_1 + 1 <= t1_0))
s.add(Or(t1_0 + 2 <= actuation2_0 , actuation2_0 + 0.5 <= t1_0))
s.add(Or(t1_0 + 2 <= actuation2_1 , actuation2_1 + 0.5 <= t1_0))
s.add(Or(actuation_0 + 1 <= input_t1_0 , input_t1_0 + 1 <= actuation_0))
s.add(Or(actuation_0 + 1 <= t1_0 , t1_0 + 2 <= actuation_0))
s.add(Or(actuation_0 + 1 <= input_t2_0 , input_t2_0 + 0.5 <= actuation_0))
s.add(Or(actuation_0 + 1 <= input_t2_1 , input_t2_1 + 0.5 <= actuation_0))
s.add(Or(actuation_0 + 1 <= t2_0 , t2_0 + 1 <= actuation_0))
s.add(Or(actuation_0 + 1 <= t2_1 , t2_1 + 1 <= actuation_0))
s.add(Or(actuation_0 + 1 <= actuation2_0 , actuation2_0 + 0.5 <= actuation_0))
s.add(Or(actuation_0 + 1 <= actuation2_1 , actuation2_1 + 0.5 <= actuation_0))
s.add(Or(input_t2_0 + 0.5 <= input_t1_0 , input_t1_0 + 1 <= input_t2_0))
s.add(Or(input_t2_0 + 0.5 <= t1_0 , t1_0 + 2 <= input_t2_0))
s.add(Or(input_t2_0 + 0.5 <= actuation_0 , actuation_0 + 1 <= input_t2_0))
s.add(Or(input_t2_0 + 0.5 <= input_t2_1 , input_t2_1 + 0.5 <= input_t2_0))
s.add(Or(input_t2_0 + 0.5 <= t2_0 , t2_0 + 1 <= input_t2_0))
s.add(Or(input_t2_0 + 0.5 <= t2_1 , t2_1 + 1 <= input_t2_0))
s.add(Or(input_t2_0 + 0.5 <= actuation2_0 , actuation2_0 + 0.5 <= input_t2_0))
s.add(Or(input_t2_0 + 0.5 <= actuation2_1 , actuation2_1 + 0.5 <= input_t2_0))
s.add(Or(input_t2_1 + 0.5 <= input_t1_0 , input_t1_0 + 1 <= input_t2_1))
s.add(Or(input_t2_1 + 0.5 <= t1_0 , t1_0 + 2 <= input_t2_1))
s.add(Or(input_t2_1 + 0.5 <= actuation_0 , actuation_0 + 1 <= input_t2_1))
s.add(Or(input_t2_1 + 0.5 <= input_t2_0 , input_t2_0 + 0.5 <= input_t2_1))
s.add(Or(input_t2_1 + 0.5 <= t2_0 , t2_0 + 1 <= input_t2_1))
s.add(Or(input_t2_1 + 0.5 <= t2_1 , t2_1 + 1 <= input_t2_1))
s.add(Or(input_t2_1 + 0.5 <= actuation2_0 , actuation2_0 + 0.5 <= input_t2_1))
s.add(Or(input_t2_1 + 0.5 <= actuation2_1 , actuation2_1 + 0.5 <= input_t2_1))
s.add(Or(t2_0 + 1 <= input_t1_0 , input_t1_0 + 1 <= t2_0))
s.add(Or(t2_0 + 1 <= t1_0 , t1_0 + 2 <= t2_0))
s.add(Or(t2_0 + 1 <= actuation_0 , actuation_0 + 1 <= t2_0))
s.add(Or(t2_0 + 1 <= input_t2_0 , input_t2_0 + 0.5 <= t2_0))
s.add(Or(t2_0 + 1 <= input_t2_1 , input_t2_1 + 0.5 <= t2_0))
s.add(Or(t2_0 + 1 <= t2_1 , t2_1 + 1 <= t2_0))
s.add(Or(t2_0 + 1 <= actuation2_0 , actuation2_0 + 0.5 <= t2_0))
s.add(Or(t2_0 + 1 <= actuation2_1 , actuation2_1 + 0.5 <= t2_0))
s.add(Or(t2_1 + 1 <= input_t1_0 , input_t1_0 + 1 <= t2_1))
s.add(Or(t2_1 + 1 <= t1_0 , t1_0 + 2 <= t2_1))
s.add(Or(t2_1 + 1 <= actuation_0 , actuation_0 + 1 <= t2_1))
s.add(Or(t2_1 + 1 <= input_t2_0 , input_t2_0 + 0.5 <= t2_1))
s.add(Or(t2_1 + 1 <= input_t2_1 , input_t2_1 + 0.5 <= t2_1))
s.add(Or(t2_1 + 1 <= t2_0 , t2_0 + 1 <= t2_1))
s.add(Or(t2_1 + 1 <= actuation2_0 , actuation2_0 + 0.5 <= t2_1))
s.add(Or(t2_1 + 1 <= actuation2_1 , actuation2_1 + 0.5 <= t2_1))
s.add(Or(actuation2_0 + 0.5 <= input_t1_0 , input_t1_0 + 1 <= actuation2_0))
s.add(Or(actuation2_0 + 0.5 <= t1_0 , t1_0 + 2 <= actuation2_0))
s.add(Or(actuation2_0 + 0.5 <= actuation_0 , actuation_0 + 1 <= actuation2_0))
s.add(Or(actuation2_0 + 0.5 <= input_t2_0 , input_t2_0 + 0.5 <= actuation2_0))
s.add(Or(actuation2_0 + 0.5 <= input_t2_1 , input_t2_1 + 0.5 <= actuation2_0))
s.add(Or(actuation2_0 + 0.5 <= t2_0 , t2_0 + 1 <= actuation2_0))
s.add(Or(actuation2_0 + 0.5 <= t2_1 , t2_1 + 1 <= actuation2_0))
s.add(Or(actuation2_0 + 0.5 <= actuation2_1 , actuation2_1 + 0.5 <= actuation2_0))
s.add(Or(actuation2_1 + 0.5 <= input_t1_0 , input_t1_0 + 1 <= actuation2_1))
s.add(Or(actuation2_1 + 0.5 <= t1_0 , t1_0 + 2 <= actuation2_1))
s.add(Or(actuation2_1 + 0.5 <= actuation_0 , actuation_0 + 1 <= actuation2_1))
s.add(Or(actuation2_1 + 0.5 <= input_t2_0 , input_t2_0 + 0.5 <= actuation2_1))
s.add(Or(actuation2_1 + 0.5 <= input_t2_1 , input_t2_1 + 0.5 <= actuation2_1))
s.add(Or(actuation2_1 + 0.5 <= t2_0 , t2_0 + 1 <= actuation2_1))
s.add(Or(actuation2_1 + 0.5 <= t2_1 , t2_1 + 1 <= actuation2_1))
s.add(Or(actuation2_1 + 0.5 <= actuation2_0 , actuation2_0 + 0.5 <= actuation2_1))
s.add()
s.add(input_t1_0 >= 0)
s.add(input_t1_0 <= 16)
s.add(t1_0 >= 0)
s.add(t1_0 <= 16)
s.add(actuation_0 >= 0)
s.add(actuation_0 <= 16)
s.add(input_t2_0 >= 0)
s.add(input_t2_0 <= 16)
s.add(input_t2_1 >= 0)
s.add(input_t2_1 <= 16)
s.add(t2_0 >= 0)
s.add(t2_0 <= 16)
s.add(t2_1 >= 0)
s.add(t2_1 <= 16)
s.add(actuation2_0 >= 0)
s.add(actuation2_0 <= 16)
s.add(actuation2_1 >= 0)
s.add(actuation2_1 <= 16)
print(s.check())
print(s.model())
outFile = open("schedule_specification.txt", "w")
outFile.writelines(str(s.check()) + "\n")
outFile.writelines(str(s.model()))
