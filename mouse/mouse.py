maze = [[2, 2, 2, 2, 2, 2],
        [2, 0, 0, 0, 2, 2],
        [2, 0, 2, 0, 0, 2],
        [2, 0, 0, 2, 0, 2],
        [2, 0, 2, 2, 0, 2],
        [2, 2, 2, 2, 2, 2]]


def goUp(location):
    if(location[1] == 0):
        return False
    else:
        newLocation = [location[0], location[1]-1]
        if newLocation in routeHistory:
            return False
        elif maze[newLocation[0]][newLocation[1]] == 2:
            return False
        else:
            rightRoute.append(newLocation)
            routeHistory.append(newLocation)
            return True

def goDown(location):
    if(location[1]==5):
        return False
    else:
        newLocation = [location[0], location[1]+1]
        if newLocation in routeHistory:
            return False       
        elif maze[newLocation[0]][newLocation[1]] == 2:
            return False
        else:
            rightRoute.append(newLocation)
            routeHistory.append(newLocation)
            return True

def goLeft(location):
    if(location[0]==0):
        return False
    else:
        newLocation = [location[0]-1, location[1]]
        if newLocation in routeHistory:
            return False       
        elif maze[newLocation[0]][newLocation[1]] == 2:
            return False
        else:
            rightRoute.append(newLocation)
            routeHistory.append(newLocation)
            return True
        
def goRight(location):
    if(location[0]==5):
        return False
    else:
        newLocation = [location[0]+1, location[1]]
        if newLocation in routeHistory:
            return False       
        elif maze[newLocation[0]][newLocation[1]] == 2:
            return False
        else:
            rightRoute.append(newLocation)
            routeHistory.append(newLocation)
            return True

rightRoute = [[1,1]]
routeHistory = [[1,1]]
location = [1,1]

while rightRoute[-1] != [4,4]:
    if goUp(location):
        location = rightRoute[-1]
        continue
    if goDown(location):
        location = rightRoute[-1]
        continue
        
    if goLeft(location):
        location = rightRoute[-1]
        continue
        
    if goRight(location):
        location = rightRoute[-1]
        continue
    rightRoute.pop()
    location = rightRoute[-1]

print(rightRoute)