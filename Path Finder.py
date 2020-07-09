import turtle
import time
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("MAZE")
wn.setup(700,700)

class Pen(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("square")
    self.color("white")
    self.penup()
    self.speed(0)
class PenPath(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("square")
    self.color("blue")
    self.penup()
    self.speed(0)
class PenFinalPath(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("square")
    self.color("yellow")
    self.penup()
    self.speed(0)

flag = False
final_arr=[]

def createMaze():
    level_1 = [

        "XXXXXXSXXXXXXXXXXXXXXXXX",
        "XXXX                  XX",
        "XXX           XXXXXXXXXX",
        "XXXXX  XXXXX         XXX",
        "XXXXX        XXXX     XX",
        "XXXXX             XXXXXX",
        "X      XXXXXXXX        X",
        "XX         XXXXXXXEXXXXX",
        "XXXXX    XXXXXX   XXXXXX",
        "XXXX         XXXXXXXXXXX",
        "XXXX   XXXXX        XXXX",
        "XX     XXXXX      XXXXXX",
        "XXXX      XXXX    XXXXXX",
        "XX                    XX",
        "XX          XXXXXXXXXXXX",
        "XXX   XX     XX  XX XXXX",
        "XXXXXX          XXXXXXXX",
        "XX                     X",
        "XXXX XXXXXXXX   XXXXXXXX",
        "XXX              XXXXXXX",
        "XX                  XXXX",
        "XX XX                XXX",
        "XX          XXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXX",
    ]

    maze = []

    for i in range(len(level_1)):
        ar = []
        for j in range(len(level_1)):
            ar.append(level_1[i][j])
        maze.append(ar)




    for i in range(len(maze)):
      ss=""
      for j in range(len(maze)):
        ss=ss+maze[i][j]
      final_arr.append(ss)


    final_arr[23].replace(".","E")
    setup_maze(final_arr)
    solveMaze(maze, 0, 5)

def checkAllSides(maze,x,y):
    if(checkL(maze,x,y)!=True and checkR(maze,x,y)!=True and checkU(maze,x,y)!=True and checkD(maze,x,y)!=True ):
        return True
    else:
        return False
def checkL(maze, x, y):
    if (maze[x][y - 1] == "X" or maze[x][y - 1] == "-"):
        return False
    else:
        return True


def checkR(maze, x, y):
    if (maze[x][y + 1] == "X" or maze[x][y + 1] == "-"):
        return False
    else:
        return True


def checkU(maze, x, y):
    if (maze[x - 1][y] == "X" or maze[x - 1][y] == "-"):
        return False
    else:
        return True


def checkD(maze, x, y):
    if (maze[x + 1][y] == "X" or maze[x + 1][y] == "-"):
        return False
    else:
        return True


def solveMaze(maze, x, y):
    global flag

    if(checkAllSides(maze,x,y)):
        screen_x = -288 + (y * 24)
        screen_y = 288 - (x * 24)
        time.sleep(0.1)
        penPath.goto(screen_x, screen_y)

        penPath.stamp()

    if (0 <= x + 1 <= len(maze) and 0 <= y <= len(maze[0]) and checkD(maze, x, y) and flag == False):
        if (maze[x + 1][y] == "E"):
            maze[x][y] = "."
            screen_x = -288 + (y * 24)
            screen_y = 288 - (x * 24)
            time.sleep(0.1)
            penPathFinal.goto(screen_x, screen_y)
            penPathFinal.stamp()
            flag = True
        else:
            maze[x][y] = "-"
            screen_x = -288 + (y * 24)
            screen_y = 288 - (x * 24)
            time.sleep(0.1)
            penPath.goto(screen_x, screen_y)
            penPath.stamp()
            solveMaze(maze, x + 1, y)
            if (flag):
                maze[x][y] = "."
                screen_x = -288 + (y * 24)
                screen_y = 288 - (x * 24)
                time.sleep(0.1)
                penPathFinal.goto(screen_x, screen_y)
                penPathFinal.stamp()

    if (0 <= x - 1 <= len(maze) and 0 <= y <= len(maze[0]) and checkU(maze, x, y) and flag == False):
        if (maze[x - 1][y] == "E"):
            maze[x][y] = "."
            screen_x = -288 + (y * 24)
            screen_y = 288 - (x * 24)
            time.sleep(0.1)
            penPathFinal.goto(screen_x, screen_y)
            penPathFinal.stamp()
            flag = True
        else:
            maze[x][y] = "-"
            screen_x = -288 + (y * 24)
            screen_y = 288 - (x * 24)
            time.sleep(0.1)
            penPath.goto(screen_x, screen_y)
            penPath.stamp()
            solveMaze(maze, x - 1, y)
            if (flag):
                maze[x][y] = "."
                screen_x = -288 + (y * 24)
                screen_y = 288 - (x * 24)
                time.sleep(0.1)
                penPathFinal.goto(screen_x, screen_y)
                penPathFinal.stamp()

    if (0 <= x <= len(maze) and 0 <= y + 1 <= len(maze[0]) and checkR(maze, x, y) and flag == False):
        if (maze[x][y + 1] == "E"):
            maze[x][y] = "."
            screen_x = -288 + (y * 24)
            screen_y = 288 - (x * 24)
            time.sleep(0.1)
            penPathFinal.goto(screen_x, screen_y)
            penPathFinal.stamp()
            flag = True
        else:
            maze[x][y] = "-"
            screen_x = -288 + (y * 24)
            screen_y = 288 - (x * 24)
            time.sleep(0.1)
            penPath.goto(screen_x, screen_y)
            penPath.stamp()
            solveMaze(maze, x, y + 1)
            if (flag):
                maze[x][y] = "."
                screen_x = -288 + (y * 24)
                screen_y = 288 - (x * 24)
                time.sleep(0.1)
                penPathFinal.goto(screen_x, screen_y)
                penPathFinal.stamp()

    if (0 <= x <= len(maze) and 0 <= y - 1 <= len(maze[0]) and checkL(maze, x, y) and flag == False):
        if (maze[x][y - 1] == "E"):
            maze[x][y] = "."
            screen_x = -288 + (y * 24)
            screen_y = 288 - (x * 24)
            time.sleep(0.1)
            penPathFinal.goto(screen_x, screen_y)
            penPathFinal.stamp()
            flag = True
        else:
            maze[x][y] = "-"
            screen_x = -288 + (y * 24)
            screen_y = 288 - (x * 24)
            time.sleep(0.1)
            penPath.goto(screen_x, screen_y)
            penPath.stamp()
            solveMaze(maze, x, y - 1)
            if (flag):
                maze[x][y] = "."
                screen_x = -288 + (y * 24)
                screen_y = 288 - (x * 24)
                time.sleep(0.1)
                penPathFinal.goto(screen_x, screen_y)
                penPathFinal.stamp()



def setup_maze(level):
  for y in range(len(level)):
    for x in range(len(level[0])):
      character=level[y][x]

      screen_x = -288 + (x*24)
      screen_y= 288 - (y*24)

      if character == "X":
        pen.goto(screen_x,screen_y)
        pen.stamp()
      elif character =="E" or character == "S":
        penPathFinal.goto(screen_x, screen_y)
        penPathFinal.stamp()





pen= Pen()
penPath=PenPath()
penPathFinal=PenFinalPath()

createMaze()

turtle.mainloop()