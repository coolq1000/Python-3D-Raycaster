import pygame,sys,math,random,time

layout = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,3,2,2,2,3,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

# Setup,
pygame.init()
w,h = 400,400
screen = pygame.display.set_mode((w,h))

# Variables,

DEBUG = False

mapWidth = len(layout[0])
mapHeight = len(layout)
mapScale = 8

rayCount = 0
count = 0

dt = 0

# Renderer Variables,
numRays = w//15
fov = 0.6

rayLength = 0.2
rayStep = 100


def clamp(n, smallest, largest): return max(smallest, min(n, largest))

def sign(n):
    if n > 0:
        return 1
    if n < 0:
        return -1
    if n == 0:
        return 0

class Cam:
    def __init__(self,pos=(2,2),direction=0,rot=0,sSpeed=0,speed=0,moveSpeed=0.3/8,rotSpeed=math.pi*6/180/6):
        self.x = pos[0]
        self.y = pos[1]
        self.direction = direction
        self.rot = rot
        self.sSpeed = sSpeed
        self.speed =  speed
        self.moveSpeed = moveSpeed
        self.rotSpeed = rotSpeed
    def move(self):
        moveStep = self.speed * self.moveSpeed*dt
        if event.type == pygame.MOUSEMOTION:
            x,y = event.rel
            self.rot += float(x)*math.pi/1000
            self.rot += self.direction*self.rotSpeed*math.pi/8*dt
        newX = self.x + math.cos(self.rot)*moveStep
        newY = self.y + math.sin(self.rot)*moveStep
        if isBlocking(newX+mapScale/10/2,newY+mapScale/10/2):
            return
        if isBlocking(newX,newY):
            return
        if isBlocking(newX+mapScale/10,newY+mapScale/10):
            return
        self.x = newX
        self.y = newY
    def moveSide(self):
        moveStep = self.sSpeed * self.moveSpeed*dt
        newX = self.x + math.cos(self.rot+(self.sSpeed*1.5))*moveStep*sign(self.sSpeed)
        newY = self.y + math.sin(self.rot+(self.sSpeed*1.5))*moveStep*sign(self.sSpeed)
        if isBlocking(newX+mapScale/10/2,newY+mapScale/10/2):
            return
        if isBlocking(newX,newY):
            return
        if isBlocking(newX+mapScale/10,newY+mapScale/10):
            return
        self.x = newX
        self.y = newY
    def getKeys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]: self.speed = 1
        elif key[pygame.K_s]: self.speed = -1
        else:
            self.speed = 0
        if key[pygame.K_q]: self.direction = -1
        elif key[pygame.K_e]: self.direction = 1
        else:
            self.direction = 0
        if key[pygame.K_a]: self.sSpeed = -1
        elif key[pygame.K_d]: self.sSpeed = 1
        else:
            self.sSpeed = 0
        if key[pygame.K_ESCAPE]: pygame.quit(); sys.exit()
def drawMiniMap():
    for x in range(mapWidth):
        for y in range(mapHeight):
            wall = layout[y][x]
            if wall > 0:
                pygame.draw.rect(screen,(50,50,150),pygame.Rect(x*mapScale,y*mapScale,mapScale,mapScale))

def isBlocking(x,y):
    if y < 0 or y >= mapHeight or x < 0 or x >= mapWidth:
        return True
    return layout[math.floor(y)][math.floor(x)] != 0

def isBlockingExtra(x,y):
    try:
        isThere = layout[math.floor(y)][math.floor(x)] != 0
        wall = layout[math.floor(y)][math.floor(x)]
    except:
        isThere = False
        wall = 0
    if y < 0 or y >= mapHeight or x < 0 or x >= mapWidth:
        return True,wall
    return isThere, wall

def drawPlayer():
    pygame.draw.rect(screen,(100,100,200),pygame.Rect(cam.x*mapScale,cam.y*mapScale,mapScale,mapScale))
    pygame.draw.line(screen,(100,100,200),(cam.x*mapScale+(mapScale//2),cam.y*mapScale+(mapScale//2)),((cam.x+math.cos(cam.rot)*4)*mapScale+(mapScale//2),(cam.y+math.sin(cam.rot)*4)*mapScale+(mapScale//2)))

def castRays():
    global count,rayCount
    for i in range(int(numRays)):
        if rayCount % 1 == 0:
            screen.fill((0,0,0),(i*(w/numRays),0,w/numRays,h))
            castSingleRay(i,i/numRays/2*fov-(0.25*fov)+cam.rot,rayLength,rayStep)
        rayCount += 1

def castSingleRay(num,angle,length,step):
    for i in range(step):
        xs = cam.x*mapScale+(mapScale//2)
        ys = cam.y*mapScale+(mapScale//2)
        xe = (cam.x+math.cos(angle)*(i*length))*mapScale+(mapScale//2)
        ye = (cam.y+math.sin(angle)*(i*length))*mapScale+(mapScale//2)
        mxe = (cam.x+math.cos(angle)*(i*length))
        mye = (cam.y+math.sin(angle)*(i*length))
        isThere, wall = isBlockingExtra(mxe,mye)
        if isThere:
            drawRaycast(i,num,wall)
            break
        if DEBUG:
            pygame.draw.line(screen,(100,100,200),(xs,ys),(xe,ye))

def drawRaycast(depth,count,wall):
    temp = depth*10
    shade = 0
    shade = depth*10*rayLength
    if wall == 1:
        screen.fill((clamp(200-shade,0,255),clamp(200-shade,0,255),clamp(200-shade,0,255)),(count*(w/numRays),temp*rayLength,w/numRays+1,h-(temp*2*rayLength)))
    if wall == 2:
        screen.fill((clamp(200-shade,0,255),clamp(20-shade,0,255),clamp(20-shade,0,255)),(count*(w/numRays),temp*rayLength,w/numRays+1,h-(temp*2*rayLength)))
    if wall == 3:
        screen.fill((clamp(20-shade,0,255),clamp(20-shade,0,255),clamp(200-shade,0,255)),(count*(w/numRays),temp*rayLength,w/numRays+1,h-(temp*2*rayLength)))
    #screen.fill((clamp(200-shade,0,255),clamp(200-shade,0,255),clamp(200-shade,0,255)),(count*(w/numRays),w//2-2,w/numRays,4))
cam = Cam()

pygame.event.get(); pygame.mouse.get_rel()
pygame.mouse.set_visible(0); pygame.event.set_grab(1);
clock = pygame.time.Clock()
count = 0
while True:
    rayCount += 1
    dt = clock.tick(60)/5
    
    fps = clock.get_fps()
    screen.fill((0,0,0))
    pygame.display.set_caption("FPS: "+str(int(fps)))
    event = pygame.event.poll()
    if event.type == pygame.QUIT: pygame.quit(); sys.exit();
    # Draw,
    castRays()
    cam.getKeys()
    cam.move()
    cam.moveSide()
    if DEBUG:
        drawMiniMap()
        drawPlayer()
    pygame.display.flip()
    count += 1
