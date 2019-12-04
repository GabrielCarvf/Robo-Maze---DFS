import numpy as np
import matplotlib.pyplot as plt

agentX = 1
agentY = 6

def createMaze():
    maze = np.array([   [1,1,1,1,1,1,1,1,1,1,1,1,1],
                        [1,0,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,1,0,0,1,1,1,1,0,1],
                        [1,0,0,0,1,0,0,1,1,1,1,0,1],
                        [1,0,0,0,1,1,0,1,1,1,1,2,1],
                        [1,1,1,0,1,1,1,1,1,1,1,1,1],
                        [1,0,0,0,0,0,0,0,0,0,0,0,1],
                        [1,1,1,1,1,1,1,1,1,1,1,1,1],    ])
    return maze

def createMaze2():
    maze = np.array([   [1,1,1,1,1,1,1,1,1,1,1,1,1],
                        [1,0,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,1,1,1,1,1,1,1,1,1,0,1],
                        [1,0,1,0,0,0,0,0,0,0,1,0,1],
                        [1,0,0,0,0,0,0,0,1,0,1,0,1],
                        [1,1,1,1,1,1,1,1,1,1,1,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,2,0,0,0,0,1],    
                        [1,1,1,1,1,1,1,1,1,1,1,1,1],    ])
    return maze

def createMaze3():
    maze = np.array([   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                        [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,1,0,1,0,0,1,0,0,0,1,0,0,1,1,0,1,0,1],
                        [1,0,1,0,1,0,0,1,0,0,0,1,0,0,1,1,0,1,0,1],
                        [1,0,1,0,1,0,0,1,0,0,0,1,2,0,1,1,0,1,0,1],
                        [1,0,1,1,1,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1],
                        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],    ])
    return maze

def searchExit(agentX, agentY, maze):
    plt.imshow(createMaze2())
    plt.scatter(agentX, agentY)
    plt.savefig('figura.png')
    plt.close()
    
    if(maze[agentY][agentX] == 2):
        return True
    else:
        foundExit = False
        maze[agentY][agentX] = 3 #Visitado
        
        if(maze[agentY][agentX+1] == 2):
            foundExit = searchExit(agentX+1, agentY, maze)
        elif(maze[agentY][agentX-1] == 2):
            foundExit = searchExit(agentX-1, agentY, maze)
        elif(maze[agentY-1][agentX] == 2):
            foundExit = searchExit(agentX, agentY-1, maze)
        elif(maze[agentY+1][agentX] == 2):
            foundExit = searchExit(agentX, agentY+1, maze)
        else:   
            # Direita
            if(not foundExit and maze[agentY][agentX+1] != 1 and maze[agentY][agentX+1] != 3):
                foundExit = searchExit(agentX+1, agentY, maze)
            # Esquerda
            if(not foundExit and maze[agentY][agentX-1] != 1 and maze[agentY][agentX-1] != 3):
                foundExit = searchExit(agentX-1, agentY, maze)
            # Cima
            if(not foundExit and maze[agentY-1][agentX] != 1 and maze[agentY-1][agentX] != 3):
                foundExit = searchExit(agentX, agentY-1, maze)
            # Baixo
            if(not foundExit and maze[agentY+1][agentX] != 1 and maze[agentY+1][agentX] != 3):
                foundExit = searchExit(agentX, agentY+1, maze)
        
        return(foundExit)

maze = createMaze2()

print('Found exit? ' + str(searchExit(agentX, agentY, maze)))
