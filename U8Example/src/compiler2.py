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

modePeriod = int(inpDict["mode"][0]["period"])

# calculating lcm of all the frequency
frequencyMax=1
for i in inpDict["mode"][0]["definition"]:
    frequencyMax=lcm(frequencyMax,int(i["frequency"]))

# Time at which the giotto micro step must execute
configUpdate = modePeriod/frequencyMax

print(configUpdate)

# finding actuator drivers

# list containing name of all the actuators
actList = []

for i in inpDict["actuator"]:
    actList.append(i["name"])

# timing constraints for the actuator
for i in inpDict["mode"][0]["definition"]:
    if i["type"] == "actuator":
        for j in inpDict["driver"]:
            if j["name"] == i["driver"]:
                for k in range(int(i["frequency"])):
                    cnx.append("= " + j["name"] + "_"+ str(k) + " "+ str((modePeriod/int(i["frequency"]))*(k+1)) + "\n")


# timing constraints for sensor 


outFile.writelines(cnx)
# print(actList)
# finding sensor drivers