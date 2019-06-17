# opening the flie
inpFile = open("schedule_specification.txt", "r")
outFile = open("main.c", "w")
giotto  = open("giotto.json", "r")

# to store code of the main file
mainx = []

# dictionay to store processed schedule
schedule = {}

satisfy = inpFile.readline()
if(satisfy == "sat\n"):
    print("Satisfied")
    constraints = inpFile.readlines()

    mainx.append("#include \"fblib/firebird.h\" \n")
    mainx.append("volatile unsigned int schedule = 0; \n")
    mainx.append("int main(int argc, char *argv[]) {")
    mainx.append("init_devices(); \n")
    mainx.append("TCCR4A = (1 << WGM42); \n")
    mainx.append("TCCR4B = (1 << CS00) | (1 << CS01); \n")
    mainx.append("TIMSK4 = (1 << OCIE4A); \n")
    # we need to specify first schdule now

    for i in constraints:
        i=i[1:]
        i=i[:-2]

        split1 = i.split("=")
        # print(split1)
        split2 = split1[1].split("/")
        if(len(split2) > 1):
            # print(split2)
            schedule.update({split1[0].strip() : float(split2[0])/float(split2[1])})
        else:
            schedule.update({split1[0].strip() : float(split1[1])})
        
    sortedSchedule = sorted(schedule , key=schedule.get)

    print(sortedSchedule)




    outFile.writelines(mainx)

else:
    print("Unsatisfied")