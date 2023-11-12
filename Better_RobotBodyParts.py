"""
Given a list of robots with their parts and a seperate list of List of parts. Return the robots that can be completed.
"""

def solve(param1, param2):
    hm={}
    for p in param1:
        roboInfo=p.split("_")
        robotName=roboInfo[0]
        robotPart=roboInfo[1]
        if robotName not in hm and robotPart not in hm.values():
            hm[robotName]={robotPart}
        elif robotName in hm and robotPart not in hm.values():
            hm[robotName].add(robotPart)
    result=[]
    for robotName, robotSet in hm.items():
        flag = True
        for i in range(len(param2)):
            if param2[i] not in robotSet:
                flag=False
                break
        if flag==True:
            result.append(robotName)
    return result
param1 = ['robot1_arm', 'robot1_leg','robot1_head','robot2_arm','robot2_torso','robot1_leg']
param2 = ['arm','leg','head']
print(solve(param1, param2))
# output: 'robot1'