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

# actuato-task dependencies




outFile.writelines(cnx)
print("Done!")
