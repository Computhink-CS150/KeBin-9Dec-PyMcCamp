# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER

def Teleport():
    agent.teleport_to_player()

player.on_chat("come", Teleport)

def Forward(steps):
    agent.move(FORWARD, steps)

player.on_chat("fw", Forward)
def Back(steps):
    agent.move(BACK, steps)

player.on_chat("bk", Back)
def Up(steps):
    agent.move(UP, steps)

player.on_chat("up", Up)
def Down(steps):
    agent.move(DOWN, steps)

player.on_chat("dw", Down)
def TurnLeft(steps):
    agent.turn(LEFT)

player.on_chat("tl",TurnLeft)
def TurnRight(steps):
    agent.turn(RIGHT)

player.on_chat("tr", TurnRight)
def ObstacleCourse():
    agent.move(FORWARD, 4)
    agent.move(LEFT, 4)
    agent.move(FORWARD, 3)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)

    player.on_chat("move", ObstacleCourse)
def Chop(height):
    for i in range(height):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    agent.move(DOWN, height)
    agent.collect_all()
player.on_chat("chop", Chop)    
def mine(length):
    for i in range(length):
        agent.destroy(FORWARD)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.destroy(UP)
        agent.collect_all()
        agent.move(FORWARD, 1)

player.on_chat("mine", mine)
def buildwall(height,width):
    for j in range(width):
        for i in range(height):
            agent.place(FORWARD)
            agent.move(UP, 1)
        agent.move(RIGHT, 1)
        agent.move(DOWN, height)        

player.on_chat("roof", buildwall)
def Buildroof(height,width):
    for j in range(width):
        for i in range(height):
            agent.place(DOWN)
            agent.move(FORWARD, 1)
        agent.move(RIGHT, 1)
        agent.move(BACK, height)
player.on_chat("roof", Buildroof)
def DigDown():
    while agent.detect(AgentDetection.BLOCK, DOWN):
        agent.destroy(DOWN)
        agent.move(DOWN, 1)
        agent.collect_all()
player.on_chat("dig", DigDown)
def BuildBridge(height,width):
    for j in range(width):
        for i in range(height):
            agent.place(DOWN)
            agent.move(FORWARD, 1)
        agent.move(RIGHT, 1)
        agent.move(BACK, height)
player.on_chat("roof", Buildroof)