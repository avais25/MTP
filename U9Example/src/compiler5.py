# opening the flie
inpFile = open("schedule_specification.txt", "r")


satisfy = inpFile.readline()
if(satisfy == "sat\n"):
    print("Satisfied")
    constraints = inpFile.readlines()
    
    for i in constraints:
        i=i[1:]
        i=i[:-2]
        print(i)

else:
    print("Unsatisfied")