#TO DO:
#
#Bug Fix: Pinky is making 180 degree turns. She shouldn't.
#Status: Done
#
#Feature: Add scheduled search modes for ghosts.
#Status: Started
#
#Feature: Add Power Pellet functionality
#Status: Unstarted
#
#Feature: Ghosts should slow down when moving through the tunnel.
#Status: Unstarted
#
#Feature: Ghosts should not be able to turn on certain tiles.
#Status: Unstarted

#map gives the layout and the uneaten pellets and pills.

def new_level(board, pacman, ghost_order, level_number):
	board.reset()
	pacman.reset()
	for ghost in ghost_order:
		ghost.reset(pacman, board, ghost.name, level_number)

def dist_square(a, b):
	return (a[0] - b[0])**2 + (a[1] - b[1])**2

class Map():

	def __init__(self):
		self.reset()

	def reset(self):
		self.pellets_eaten = 0
		self.counter = 0
	#   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28
		self.game_board=[['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'] \
		,['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'] #2 \
		,['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'] #3 \
		,['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'] #4 \
		,['w','p','p','p','p','p','p','p','p','p','p','p','p','w','w','p','p','p','p','p','p','p','p','p','p','p','p','w'] #5 \
		,['w','p','w','w','w','w','p','w','w','w','w','w','p','w','w','p','w','w','w','w','w','p','w','w','w','w','p','w'] #6 \
		,['w','e','w','w','w','w','p','w','w','w','w','w','p','w','w','p','w','w','w','w','w','p','w','w','w','w','e','w'] #7 \
		,['w','p','w','w','w','w','p','w','w','w','w','w','p','w','w','p','w','w','w','w','w','p','w','w','w','w','p','w'] #8 \
		,['w','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','w'] #9 \
		,['w','p','w','w','w','w','p','w','w','p','w','w','w','w','w','w','w','w','p','w','w','p','w','w','w','w','p','w'] #10 \
		,['w','p','w','w','w','w','p','w','w','p','w','w','w','w','w','w','w','w','p','w','w','p','w','w','w','w','p','w'] #11 \
		,['w','p','p','p','p','p','p','w','w','p','p','p','p','w','w','p','p','p','p','w','w','p','p','p','p','p','p','w'] #12 \
		,['w','w','w','w','w','w','p','w','w','w','w','w','h','w','w','h','w','w','w','w','w','p','w','w','w','w','w','w'] #13 \
		,['w','w','w','w','w','w','p','w','w','w','w','w','h','w','w','h','w','w','w','w','w','p','w','w','w','w','w','w'] #14 \
		,['w','w','w','w','w','w','p','w','w','h','h','h','h','h','h','h','h','h','h','w','w','p','w','w','w','w','w','w'] #15 \
		,['w','w','w','w','w','w','p','w','w','h','w','w','w','w','w','w','w','w','h','w','w','p','w','w','w','w','w','w'] #16 \
		,['w','w','w','w','w','w','p','w','w','h','w','h','h','h','h','h','h','w','h','w','w','p','w','w','w','w','w','w'] #17 \
		,['s','s','s','s','s','s','p','h','h','h','w','h','h','h','h','h','h','w','h','h','h','p','s','s','s','s','s','s'] #18 \
		,['w','w','w','w','w','w','p','w','w','h','w','h','h','h','h','h','h','w','h','w','w','p','w','w','w','w','w','w'] #19 \
		,['w','w','w','w','w','w','p','w','w','h','w','w','w','w','w','w','w','w','h','w','w','p','w','w','w','w','w','w'] #20 \
		,['w','w','w','w','w','w','p','w','w','h','h','h','h','h','h','h','h','h','h','w','w','p','w','w','w','w','w','w'] #21 \
		,['w','w','w','w','w','w','p','w','w','h','w','w','w','w','w','w','w','w','h','w','w','p','w','w','w','w','w','w'] #22 \
		,['w','w','w','w','w','w','p','w','w','h','w','w','w','w','w','w','w','w','h','w','w','p','w','w','w','w','w','w'] #23 \
		,['w','p','p','p','p','p','p','p','p','p','p','p','p','w','w','p','p','p','p','p','p','p','p','p','p','p','p','w'] #24 \
		,['w','p','w','w','w','w','p','w','w','w','w','w','p','w','w','p','w','w','w','w','w','p','w','w','w','w','p','w'] #25 \
		,['w','p','w','w','w','w','p','w','w','w','w','w','p','w','w','p','w','w','w','w','w','p','w','w','w','w','p','w'] #26 \
		,['w','e','p','p','w','w','p','p','p','p','p','p','p','h','h','p','p','p','p','p','p','p','w','w','p','p','e','w'] #27 \
		,['w','w','w','p','w','w','p','w','w','p','w','w','w','w','w','w','w','w','p','w','w','p','w','w','p','w','w','w'] #28 \
		,['w','w','w','p','w','w','p','w','w','p','w','w','w','w','w','w','w','w','p','w','w','p','w','w','p','w','w','w'] #29 \
		,['w','p','p','p','p','p','p','w','w','p','p','p','p','w','w','p','p','p','p','w','w','p','p','p','p','p','p','w'] #30 \
		,['w','p','w','w','w','w','w','w','w','w','w','w','p','w','w','p','w','w','w','w','w','w','w','w','w','w','p','w'] #31 \
		,['w','p','w','w','w','w','w','w','w','w','w','w','p','w','w','p','w','w','w','w','w','w','w','w','w','w','p','w'] #32 \
		,['w','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','w'] #33 \
		,['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'] #34 \
		,['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'] #35 \
		,['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w']]#36 \
		self.pellets_to_start = self.pellets_left()

	def pellets_left(self):
		result = 0
		for row in self.game_board:
			for tile in row:
				if tile == 'p':
					result += 1
		return result

	def pass_through_tile(self, coord): #coord should be a 2-pl
		if self.game_board[coord[0]][coord[1]] == 'p':
			self.pellets_eaten += 1
			self.counter += 1
			self.game_board[coord[0]][coord[1]] = 'h'
			print('pellets_eaten: ' + str(self.pellets_eaten))
			print('counter: ' + str(self.counter))

	def udlr(self, coord):
		result = []
		if self.game_board[coord[0] - 1][coord[1]] == 'w':
			result.append(0)
		else:
			result.append(1)
		if self.game_board[coord[0] + 1][coord[1]] == 'w':
			result.append(0)
		else:
			result.append(1)
		if self.game_board[coord[0]][(coord[1] - 1)%28] == 'w':
			result.append(0)
		else:
			result.append(1)
		if self.game_board[coord[0]][(coord[1] + 1)%28] == 'w':
			result.append(0)
		else:
			result.append(1)
		return result

class Ghost():
	def __init__(self, pacman, board, name, level):
		self.reset(pacman, board, name, level)

	def reset(self, pacman, board, name, level):
		self.pixel_position = [4, 0]
		self.pacman_state = pacman.state
		self.map = board
		self.name = name
		self.direction = 'L'
		self.mode = 'C'
		self.in_house = True
		self.started = False
		self.move_score = 0.0

		if level == 1:
			self.move_speed = 0.75
			self.fright_speed = 0.50
			self.tunnel_speed = 0.40
		if level >= 2 and level <= 4:
			self.move_speed = 0.85
			self.fright_speed = 0.55
			self.tunnel_speed = 0.45
		elif level >= 5 and level <= 20:
			self.move_speed = .95
			self.fright_speed = .60
			self.tunnel_speed = .50
		else:
			pacman_move_speed = .90

		if self.name == 'Blinky':
			self.tile_position = [14, 14]
			self.default_tile = [-1, 25]
			self.in_house = False
			self.started = True
			self.counter_limit = 0;
		elif self.name == 'Pinky': #pink
			self.tile_position = [17, 14]
			self.default_tile = [-1, 2]
			self.counter_limit = 0
		elif self.name == 'Inky': #blue
			self.tile_position = [17, 12]
			self.default_tile = [34, 27]
			if level == 1:
				self.counter_limit = 30
			else:
				self.counter_limit = 0
		elif self.name == 'Clyde': #orange
			self.tile_position = [17, 16]
			self.default_tile = [34, 0]
			if level == 1:
				self.counter_limit = 60
			elif level == 2:
				self.counter_limit = 50
			else:
				self.counter_limit = 0
		else:
			pass

# target_tile returns the tile coordinates of the tile which a ghost will navigate towards.
	def target_tile(self):
		#scatter mode
		if self.mode == 'S':
			return self.default_tile
		else:
			pass
		#chase mode
		result = self.pacman_state[:2]
		if self.name == 'Pinky':
			if self.pacman_state[2] == 'L':
				result[1] -= 4
			if self.pacman_state[2] == 'R':
				result[1] += 4
			if self.pacman_state[2] == 'U':
				result[0] -= 4
				result[1] -= 4 #this bug is intentional and is in the original game.
			if self.pacman_state[2] == 'D':
				result[0] += 4
		elif self.name == 'Inky':
			result = [2*self.pacman_state[0] - blinky.tile_position[0], 2*self.pacman_state[1] - blinky.tile_position[1]]
		elif self.name == 'Clyde' and dist_square(self.tile_position, self.pacman_state[:2]) < 64:
			result = self.default_tile
		return list(result)

	def get_display_pixel(self):
		return [8*self.tile_position[0] + self.pixel_position[0], 8*self.tile_position[1] + self.pixel_position[1]]

	def move(self):
		if(self.name == 'Blinky'):
			print('move_speed: ' + str(self.move_speed))
			print('move_score: ' + str(self.move_score))
			print('started: ' + str(self.started))
			print('in_house: ' + str(self.in_house))
			print('pixel_position: ' + str(self.pixel_position))
			print('tile_position: ' + str(self.tile_position))
			print('direction: ' + str(self.direction))
			print()
		if not self.started:
			return
		else:
			pass
		if self.map.game_board[self.tile_position[0]][self.tile_position[1]] == 's':
			self.move_score += self.tunnel_speed
		else:
			self.move_score += self.move_speed
		if self.move_score >= 1.0:
			self.move_score -= 1.0
		else:
			return
		if self.pixel_position == [4,3] or self.in_house:
			if self.in_house and self.tile_position == [14, 14] and self.pixel_position == [4,0]:
				self.in_house = False
		#and (self.tile_position[0] not in {14,26} or self.tile_position[1] not in {12, 15}):
			self.direction = self.choose_direction()
		if self.direction == 'L':
			self.pixel_position[1] -= 1
		elif self.direction == 'R':
			self.pixel_position[1] += 1
		elif self.direction == 'U':
			self.pixel_position[0] -= 1
		elif self.direction == 'D':
			self.pixel_position[0] += 1

#		if self.pixel_position[0] < 0:
#			self.pixel_position[0] += 8
#			self.tile_position[0] -= 1
#		elif self.pixel_position[0] > 7:
#			self.pixel_position[0] -= 8
#			self.tile_position[0] += 1
#		elif self.pixel_position[1] < 0:
#			self.pixel_position[1] += 8
#			self.tile_position[1] = (tile_position[1] - 1)%28
#		elif self.pixel_position[1] > 7:
#			self.pixel_position[1] -= 8
#			self.tile_position[1] = (tile_position[1] + 1)%28
#		else:
#			pass

		self.tile_position[0] = self.tile_position[0] + self.pixel_position[0]//8
		self.tile_position[1] = (self.tile_position[1] + self.pixel_position[1]//8)%28
		self.pixel_position = list(map(lambda n: n%8, self.pixel_position))

		if self.tile_position == list(pacman.get_state()[:2]):
			pass #end game

	def choose_direction(self):

		if self.in_house:
			displacement = (self.tile_position[1] * 8) + self.pixel_position[1] - (14 * 8)
			if displacement < 0:
				#print('displacement < 0')
				return 'R'
			elif displacement > 0:
				#print('displacement > 0')
				return 'L'
			elif self.tile_position == [14, 14] and self.pixel_position == [4,0]:
				#print('at house exit')
				target_tile = self.target_tile()
				if dist_square([14, 13], target_tile) < dist_square([14, 14], target_tile):
					return 'L'
				else:
					return 'R'
			else:
				return 'U'
				#print('go up!')
		else:
			pass

		udlr = board.udlr(self.tile_position)
		distances = [10000,10000,10000,10000]
		target_tile = self.target_tile()
		for i in range(4):
			if udlr[i] == 1 and 'DURL'[i] != self.direction:
				candidate_tile_position = self.tile_position.copy()
				candidate_tile_position[0] += (1 - (i // 2)) * ((-1) ** (i + 1))
				candidate_tile_position[1] += (i // 2) * ((-1) ** (i + 1))
				distances[i] = dist_square(candidate_tile_position, target_tile)
		result = 'U'
		min_dist = distances[0]
		if distances[2] < min_dist:
			result = 'L'
			min_dist = distances[2]
		if distances[1] < min_dist:
			result = 'D'
			min_dist = distances[1]
		if distances[3] < min_dist:
			result = 'R'
		return result

class Pacman():
	def __init__(self, level):
		self.reset(level)

	def reset(self, level):
		self.pixel_position = [4,0]
		self.state = [26,14,'L','L']
		self.move_score = 0.0
		# state has 4 values which are, in order, vertical tile position, horizontal tile position, direction (UDLR), planned direction (UDLR).
		if level == 1:
			self.move_speed = 0.80
			self.fright_speed = 0.90
		elif level >= 2 and level <= 4:
			self.move_speed = .90
			self.fright_speed = .95
		elif level >= 5 and level <= 20:
			self.move_speed = 1.0
			self.fright_speed = 1.0
		else:
			self.move_speed = .90

	def get_display_pixel(self):
		return [8*self.state[0] + self.pixel_position[0], 8*self.state[1] + self.pixel_position[1]]

	def get_state(self):
		return list(self.state)

	#def set_direction(self, new_direction):
	#	self.state[3] = new_direction
	#	print('self.state[3]: ' + self.state[3])

# this function is for pacman's movement. 
	def move(self):
		self.move_score += self.move_speed
		if self.move_score >= 1.0:
			self.move_score -= 1.0
			#check if direction can/should be changed
			udlr = board.udlr(self.state[:2])
			for i in range(4):
				if self.state[3] == 'UDLR'[i] and udlr[i] == 1:
					self.state[2] = self.state[3]
			#check to see if movement in current direction is possible
			can_move = False
			if self.state[2] == 'U':
				can_move = udlr[0] == 1 or self.pixel_position[0] < 4
			elif self.state[2] == 'D':
				can_move = udlr[1] == 1 or self.pixel_position[0] > 4
			elif self.state[2] == 'L':
				can_move = udlr[2] == 1 or self.pixel_position[1] > 3
			elif self.state[2] == 'R':
				can_move = udlr[3] == 1 or self.pixel_position[1] < 3
			else:
				pass
			#check to see if there's a pellet to eat
			if can_move and board.game_board[self.state[0]][self.state[1]] == 'p':
				board.pass_through_tile(self.state[:2])
				can_move = False
			#if pacman can move then move in that direction
			if can_move:
				if self.state[2] == 'L':
					self.pixel_position[1] -= 1
					if self.pixel_position[0] < 4:
						self.pixel_position[0] += 1
					elif self.pixel_position[0] > 4:
						self.pixel_position[0] -= 1
				elif self.state[2] == 'R':
					self.pixel_position[1] += 1
					if self.pixel_position[0] < 4:
						self.pixel_position[0] += 1
					elif self.pixel_position[0] > 4:
						self.pixel_position[0] -= 1
				elif self.state[2] == 'U':
					self.pixel_position[0] -= 1
					if self.pixel_position[1] < 3:
						self.pixel_position[1] += 1
					elif self.pixel_position[1] > 3:
						self.pixel_position[1] -= 1
				elif self.state[2] == 'D':
					self.pixel_position[0] += 1
					if self.pixel_position[1] < 3:
						self.pixel_position[1] += 1
					elif self.pixel_position[1] > 3:
						self.pixel_position[1] -= 1
				#spill over into next tile
				if self.pixel_position[0] < 0:
					self.pixel_position[0] += 8
					self.state[0] -= 1
				if self.pixel_position[0] > 7:
					self.pixel_position[0] -= 8
					self.state[0] += 1
				if self.pixel_position[1] < 0:
					self.pixel_position[1] += 8
					self.state[1] = (self.state[1] - 1)%28
				if self.pixel_position[1] > 7:
					self.pixel_position[1] -= 8
					self.state[1] = (self.state[1] + 1)%28
		else:
			pass

board = Map()
level = 1
pacman = Pacman(level)
blinky = Ghost(pacman, board, 'Blinky', level)
pinky = Ghost(pacman, board, 'Pinky', level)
inky = Ghost(pacman, board, 'Inky', level)
clyde = Ghost(pacman, board, 'Clyde', level)

ghost_order = [blinky, pinky, inky, clyde]
next_to_start_ghost_index = 0
next_to_start_ghost = ghost_order[next_to_start_ghost_index]
next_out_ghost_index = 0

# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
pacman_radius = 6
tile_dimension = 8
tick = 0



    #counter_limits = [[0  , 0  , 0  , 0  ]
    #,                 [17 , 30 , 0  , 0  ]
    #,                 [32 , 60 , 50 , 0  ]
    #,                 [999, 999, 999, 999]]
    #if level > 2:
    #	counter = 3
    #else:
    #	counter = level
    #public, level 1, level 2, level 3+
    #counters = [0, 0, 0, 0]

while running:
  # poll for events
  # pygame.QUIT event means the user clicked X to close your window
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # fill the screen with a color to wipe away anything from last frame
  screen.fill("black")

  row, column = pacman.get_display_pixel()
  pygame.draw.circle(screen, "yellow", pygame.Vector2(column, row), pacman_radius)
  for row_num, row in enumerate(board.game_board):
  	for column_num, tile in enumerate(row):
  		if tile == 'w':
  			rect = pygame.Rect(column_num * tile_dimension, row_num * tile_dimension, tile_dimension, tile_dimension)
  			pygame.draw.rect(screen, "white", rect)
  		elif tile == 'p':
  			pygame.draw.circle(screen, "white", pygame.Vector2(column_num * tile_dimension + 4, row_num * tile_dimension + 4), 2)
  		elif tile == 'p':
  			pygame.draw.circle(screen, "white", pygame.Vector2(column_num * tile_dimension + 4, row_num * tile_dimension + 4), 3)
  		else:
  			pass

  row, column = blinky.get_display_pixel()
  blinky_rect = pygame.Rect(column - 6, row - 6, 12, 12)
  pygame.draw.rect(screen, "red", blinky_rect)

  row, column = inky.get_display_pixel()
  inky_rect = pygame.Rect(column - 6, row - 6, 12, 12)
  pygame.draw.rect(screen, "blue", inky_rect)

  row, column = pinky.get_display_pixel()
  pinky_rect = pygame.Rect(column - 6, row - 6, 12, 12)
  pygame.draw.rect(screen, "pink", pinky_rect)

  row, column = clyde.get_display_pixel()
  clyde_rect = pygame.Rect(column - 6, row - 6, 12, 12)
  pygame.draw.rect(screen, "orange", clyde_rect)

  row, column = blinky.target_tile()
  row = row * 8
  column = column * 8
  blinky_target_rect = pygame.Rect(column - 2, row - 2, 4, 12)
  pygame.draw.rect(screen, "green", blinky_target_rect)

  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    pacman.state[3] = 'U'
  if keys[pygame.K_s]:
    pacman.state[3] = 'D'
  if keys[pygame.K_a]:
    pacman.state[3] = 'L'
  if keys[pygame.K_d]:
    pacman.state[3] = 'R'
  if keys[pygame.K_q]:
  	running = False
  
  if board.counter == next_to_start_ghost.counter_limit and next_to_start_ghost_index < 4:
  	next_to_start_ghost.started = True
  	if next_to_start_ghost_index < 3:
  		board.counter = 0
  		next_to_start_ghost_index += 1
  		next_to_start_ghost = ghost_order[next_to_start_ghost_index]
  	else:
  		pass

  #print(clock.get_fps())

  pacman.move()

  for ghost in ghost_order:
  	if ghost.started:
  		ghost.move()
  		if ghost.in_house:
  			break
  		else:
  			pass
  	else:
  		break

  tick += 1

  # flip() the display to put your work on screen
  pygame.display.flip()

  # limits FPS to 60
  # dt is delta time in seconds since last frame, used for framerate-
  # independent physics.
  dt = clock.tick(60) / 1000

  if board.pellets_to_start == board.pellets_eaten:
  	level += 1
  	next_to_start_ghost_index = 0
  	next_to_start_ghost = ghost_order[next_to_start_ghost_index]
  	next_out_ghost_index = 0
  	new_level(board, pacman, ghost_order, level)
  	print('level: ' + str(level))
  	print('pellets_to_start: ' + str(board.pellets_to_start))
  	print('board.pellets_eaten:' + str(board.pellets_eaten))

pygame.quit()
