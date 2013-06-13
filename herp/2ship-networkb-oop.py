import pygame, sys, math, socket, pickle

class Shot(object):
	def __init__(self, x, y, angle):
		self.x = x
		self.y = y
		self.angle = angle
		
class Ship(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.speed = 0
		self.angle = 0
		self.angleSpeed = 0
		self.shots = []
		self.alive = True
		self.enemy = None

	def process_event(self, event):
		if self.alive:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					self.angleSpeed = -5
				if event.key == pygame.K_LEFT:
					self.angleSpeed = 5
				if event.key == pygame.K_UP:
					self.speed = -5
				if event.key == pygame.K_DOWN:
					self.speed = 5
				if event.key == pygame.K_SPACE:
					self.shots.append(Shot(self.x, self.y, self.angle))

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
					self.angleSpeed = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					self.speed = 0
			
	def send_state(self):
		try:
			s.sendto(pickle.dumps(self),addr)
		except:
			pass
	
	def get_state(self):
		try:
			data,addr = s.recvfrom(1024)
			self=pickle.loads(data)
		except: 
			pass

		
				
	def update(self, img):
		if self.alive:
			self.angle += self.angleSpeed			
			self.y += self.speed * math.cos(math.radians(self.angle))
			self.x += self.speed * math.sin(math.radians(self.angle))
			self.x = self.x % xsize
			self.y = self.y % ysize
			ufo2 = pygame.transform.rotate(img, self.angle)
			newRect = ufo2.get_rect()
			newRect.center = (self.x,self.y)
			ufos.append((ufo2,newRect))
			self.update_bullets()

	def update_bullets(self):
		VisShots = []
		for shot in self.shots:
			if abs(self.enemy.x-shot.x) <= 40 and abs(self.enemy.y-shot.y) <= 40 and self.enemy.alive:
				print 'HIT'
				screen.fill(red)
				self.enemy.alive = False
				continue
			shot.y -= int(5 * math.cos(math.radians(shot.angle)))
			shot.x -= int(5 * math.sin(math.radians(shot.angle)))

			bullets.append(shot)
			if shot.y <= ysize and shot.y >= 0 and shot.x >= 0 and shot.x <= xsize:
				VisShots.append(shot)
		self.shots = VisShots
		
		
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

xsize = 700
ysize = 500

pygame.init()

size = [xsize, ysize]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Game server')

ufo = pygame.image.load('ufo.png')
ship_img=pygame.transform.scale(ufo, (80,80))
ufo = pygame.image.load('ufo2.png')
eship_img=pygame.transform.scale(ufo, (80,80))

ship1 = Ship(100, 100)
ship2 = Ship(200, 200)

ship1.enemy=ship2

ships=[ship1,ship2]

clock = pygame.time.Clock()

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',4444))
s.setblocking(False)
while True:
	if ship2.alive:
		try:
			data,addr = s.recvfrom(1024)
			ship2=pickle.loads(data)
		except: 
			pass
		
	#ship1.enemy=ship2

	bullets=[]
	ufos=[]
	
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			sys.exit(0)
		ship1.process_event(event)
	if ship1.alive:
		ship1.send_state()
		ship1.update(ship_img)
	ship2.update(eship_img)
	screen.fill(white)
	
		
	#all drawing in loops below
	for ufo in ufos:
		screen.blit(ufo[0], ufo[1]) #ufos is a list of tuples (surface, Rect)
	for bullet in bullets:
		pygame.draw.circle(screen, green, (int(bullet.x),int(bullet.y)), 5)

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
