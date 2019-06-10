import json


# some functions which are used
def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

   

# opening the flie
inpFile = open("giotto.json", "r")
outFile = open("constraints_specification.txt", "w")

# reading giotto.json as dict
inpJson = inpFile.read()
inpDict = json.loads(inpJson)

# constrains specification
cnx = []

# jitter tolerance
jitter = int(inpDict["jitter"])

# time period of the mode
modePeriod = int(inpDict["mode"][0]["period"])

# calculating lcm of all the frequency
frequencyMax=1
for i in inpDict["mode"][0]["definition"]:
    frequencyMax=lcm(frequencyMax,int(i["frequency"]))

# Time at which the giotto micro step must execute
configUpdate = modePeriod/frequencyMax


# finding actuator drivers

# list containing name of all the actuators
actList = []

for i in inpDict["actuator"]:
    actList.append(i["name"])

# list containing name of all the sensors
senList = []

for i in inpDict["sensor"]:
    senList.append(i["name"])

# timing constraints for the actuator
for i in inpDict["mode"][0]["definition"]:
    if i["type"] == "actuator":
        for j in inpDict["driver"]:
            if j["name"] == i["driver"]:
                for k in range(int(i["frequency"])):
                    # lower bound
                    cnx.append( j["name"] + "_"+ str(k) + " >= " + str((modePeriod/int(i["frequency"]))*(k+1) - jitter) + "\n")
                    # upper bound
                    cnx.append( j["name"] + "_"+ str(k) + " <= " + str((modePeriod/int(i["frequency"]))*(k+1) - float(j["wcet"])) + "\n")

cnx.append("\n")


# timing constraints for sensor
for i in inpDict["mode"][0]["definition"]:
    if i["type"] == "sensor":
        for j in inpDict["driver"]:
            if j["name"] == i["driver"]:
                for k in range(int(i["frequency"])):
                    # lower bound
                    cnx.append( j["name"] + "_"+ str(k) + " >= " + str((modePeriod/int(i["frequency"]))*(k+1)) + "\n")
                    # upper bound
                    cnx.append( j["name"] + "_"+ str(k) + " <= " + str((modePeriod/int(i["frequency"]))*(k+1) + jitter - float(j["wcet"])) + "\n")
cnx.append("\n")

# precedence constraints

# task-update dependency
count = 0
for i in inpDict["task"]:
    cnx.append( i["name"] + "_" +  str(count) + " < " + i["name"] + "_update_" + str(count) + "\n")
    count +=1

cnx.append("\n")

# driver dependencies
for i in inpDict["mode"][0]["definition"]:
    if i["type"] == "task" or i["type"] == "sensor":
        for j in range(int(i["frequency"])):
            cnx.append( i["task"] + "_" + str(j) + " < " + i["driver"] + "_" + str(j) + "\n")

cnx.append("\n")

# task instance ordering constraints
for i in inpDict["mode"][0]["definition"]:
    if i["type"] == "task" or i["type"] == "sensor":
        for j in range(int(i["frequency"])-1):
            cnx.append( i["task"] + "_" + str(j) + " < " + i["task"] + "_" + str(j+1) + "\n" )

cnx.append("\n")

# actuator-task dependencies
for i in inpDict["mode"][0]["definition"]:
    if i["type"] == "actuator":
        # print("Actuator "+i["driver"])
        for j in inpDict["driver"]:
            if i["driver"] == j["name"]:
                for k in j["input"]:
                    # print("Input "+k)
                    for l in inpDict["task"]:
                        if k in l["output"]:
                            # print("Task "+ l["name"])
                            for m in inpDict["mode"][0]["definition"]:
                                if m["type"] != "actuator" and m["task"] == l["name"]:
                                    # print(l["name"])
                                    # finding the task's instance
                                    actPeriod = int(modePeriod/int(i["frequency"]))
                                    for n in range(int(modePeriod/int(i["frequency"])),modePeriod+1,actPeriod):
                                        instance = int(n/(modePeriod/int(m["frequency"])))-1
                                        if(n != modePeriod):
                                            cnx.append(m["task"] + "_update_" + str(instance) + " < "+ i["driver"] + "_" + str(int(n/actPeriod)-1)+ "\n" )
                                            cnx.append(m["task"] + "_update_" + str(instance+1) + " > "+ i["driver"] + "_" + str(int(n/actPeriod)-1)+ "\n" )
                                        else:
                                            cnx.append(m["task"] + "_update_" + str(instance) + " < "+ i["driver"] + "_" + str(int(n/actPeriod)-1)+ "\n" )

cnx.append("\n")


# task-task dependency

for i in inpDict["driver"]:
    for j in i["input"]:
        for k in inpDict["task"]:
            if j in k["output"]:
            #    print(i["name"]+ "  "+ k["name"])
               for l in i["output"]:
                   for m in inpDict["task"]:
                       if l in m["input"]:
                           if(k["name"] != m["name"]):
                               print(i["name"])


cnx.append("\n")
# default constraints
jobList = []
# adding drivers with wcet
for i in inpDict["mode"][0]["definition"]:
    for j in inpDict["driver"]:
        if j["name"] == i["driver"]:
            for k in range(int(i["frequency"])):
                x = ( j["name"] + "_" + str(k) , j["wcet"])
                jobList.append(x)
    # adding task with wcet
    if i["type"] == "task" or i["type"] == "sensor":
        for j in inpDict["task"]:
            if j["name"] == i["task"]:
                for k in range(int(i["frequency"])):
                    x = ( j["name"] + "_" + str(k) , j["wcet1"])
                    jobList.append(x)
                    x = ( j["name"] + "_update_" + str(k) , j["wcet2"])
                    jobList.append(x)

for i,j in jobList:
    for p,q in jobList:
        if(p != i):
            cnx.append("Or(" + i + " + " + j + " <= " + p + " , " + p+" + "+ q + " <= "+ i+")\n")

cnx.append("\n")
# print(jobList)
outFile.writelines(cnx)
print("Done!")
