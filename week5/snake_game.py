import pygame
import time
import random

snake_speed = 15


#define the size of the window
window_width = 720
window_height = 480

#dict of colors to be used later
colors = {
  'black': pygame.Color(0, 0, 0), 
  'white': pygame.Color(255, 255, 255), 
  'red': pygame.Color(255, 0, 0),
  'green':pygame.Color(0, 255, 0),
  }

#set the game display settings
pygame.init()
pygame.display.set_caption('Welcome to my first snake game!')
game_window = pygame.display.set_mode((window_width, window_height))
game_fps = pygame.time.Clock()

#starting parameters for snake
snake_position = [100, 50]
snake_body = [
  [100, 50],
  [90, 50],
  [80, 50],
  [70, 50],
  ]
snake_heading = 'right'
new_direction = snake_heading

#food settings
def generate_new_food():
  new_food = [random.randrange(1, window_width//10) * 10, random.randrange(1, window_height//10) * 10]
  return new_food

food_position = generate_new_food()
spawn_food = True

#display score to user
score = 0

def show_score(choice, color, font, size):
  #use system font settings for score
  score_display_text = pygame.font.SysFont(font, size)
  
  #score text to be displayed on screen
  score_display = score_display_text.render('Current Score: ' + str(score), True, color)
  
  #designate area for code to be shown
  score_block = score_display.get_rect()
  game_window.blit(score_display, score_block)
  
  
#ending conditions for game
def end_game():
    
  end_game_font = pygame.font.SysFont('times new roman', 50)
  
  #create area that text will be shown on game surface
  end_game_display = end_game_font.render('Your final score is: ' + str(score), True, colors['red'])
  end_game_rectangle = end_game_display.get_rect()
  end_game_rectangle.midtop = (window_width/2, window_height/4)
  
  #draw end game surface to screen
  game_window.blit(end_game_display, end_game_rectangle)
  pygame.display.flip()
  
  #exit after delay
  time.sleep(2)
  pygame.quit()

  quit()
  
#Run the game
while True:
  
  #listen for key inputs
  for event in pygame.event.get():
    #allow user to quit by clicking red x
    if event.type == pygame.QUIT:
      pygame.quit()
      
    #listen for arrow inputs from keyboard
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        new_direction = 'up'
      if event.key == pygame.K_DOWN:
        new_direction = 'down'
      if event.key == pygame.K_LEFT:
        new_direction = 'left'
      if event.key == pygame.K_RIGHT:
        new_direction = 'right'
        
  #update snake heading with new direction
  #disallow user to fold snake back on itself
  if new_direction == 'up' and snake_heading != 'down':
    snake_heading = 'up'
  if new_direction == 'down' and snake_heading != 'up':
    snake_heading = 'down'
  if new_direction == 'left' and snake_heading != 'right':
    snake_heading = 'left'
  if new_direction == 'right' and snake_heading != 'left':
    snake_heading = 'right'
  
  #move snake in indicated direction
  if snake_heading == 'up':
    snake_position[1] -= 10
  if snake_heading == 'down':
    snake_position[1] += 10
  if snake_heading == 'left':
    snake_position[0] -= 10
  if snake_heading == 'right':
    snake_position[0] += 10
    
  #snake mechanics
  snake_body.insert(0, list(snake_position))
  
  #snake grows if it eats the food
  if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
    score += 1
    spawn_food = False
  
  else:
    snake_body.pop()
    
  #randomize food before showing new one on screen
  if spawn_food == False:
    food_position = generate_new_food()
  spawn_food = True
  game_window.fill(colors['black'])
  
  for piece in snake_body:
    pygame.draw.rect(game_window, colors['green'], pygame.Rect(piece[0], piece[1], 10, 10))
    
  pygame.draw.rect(game_window, colors['white'], pygame.Rect( food_position[0], food_position[1], 10, 10))
  
  #lose conditions
  
  #if snake goes too far left or right end the game
  if snake_position[0] < 0 or snake_position[0] > (window_width - 10):
    end_game()
  
  #if snake goes too far up or down
  if snake_position[1] < 0 or snake_position[1] > (window_height - 10):
    end_game()
  
  # if snake runs over itself
  for section in snake_body[1:]:
    if snake_position[0] == section[0] and snake_position[1] == section[1]:
      end_game()
      
  
  #update score
  show_score(1, colors['white'], 'times new roman', 20)
  
  #continuously update screen
  pygame.display.update()
  game_fps.tick(snake_speed)
