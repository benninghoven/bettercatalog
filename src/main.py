import json

data = {
    "bob" : "course"
        }

with open("courses.json", "w") as write_file:
    json.dump(data, write_file)

file = open("../data/manualentery.txt")

def GetCode(string):
    if len(string) != 3 and len(string) != 4:
        return ""
    count = 0
    for x in string:
        count += 1
        if count > 3:
            break
        if not x.isdigit():
            return ""
    return string

def GetName(string):
    counter = 0
    for char in string:
        counter += 1
        if not char.isupper():
            return ""
    if counter != 4:
        return ""
    return string

# deptcode coursenum courseletter coursename credits
# course description

for line in file.readlines():
    isName = False
    lines = line.split()
    name = GetName(lines[0])
    code = GetCode(lines[1])
    desc = ""
    if name and code:
        isName = True
    if isName:
        desc = line.split("-")[1]
        desc = desc.split("(")[0]
        desc = desc[1:]
        print(f"{name} - {code} - {desc}")


print("ran")
