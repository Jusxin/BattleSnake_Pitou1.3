import random
import numpy as n
def get_food(my_head_x, food):
    food_data = [list(i.values()) for i in list(food)]
    if len(food_data) > 0:
      near = (n.abs([i[0]-my_head_x for i in food_data])).argmin()
      return food_data[near]

def hunt_food(my_head_x, my_head_y, moves, food):
  if get_food(my_head_x, food) != None:
    if (my_head_x < get_food(my_head_x, food)[0]) and ('left' in moves):
      moves.remove('left')
    if (my_head_x > get_food(my_head_x, food)[0]) and ('right' in moves):
      moves.remove('right')
    if (my_head_y < get_food(my_head_x, food)[1]) and ('down' in moves):
      moves.remove('down')
    if (my_head_y > get_food(my_head_x, food)[1]) and ('up' in moves):
      moves.remove('up')

def avoid_my_neck(my_head_x, my_head_y, my_body, moves):
    my_neck = my_body[1]  # The segment of body right after the head is the 'neck'
    if my_neck["x"] < my_head_x and ('left' in moves):  # my neck is left of my head
        moves.remove("left")
    elif my_neck["x"] > my_head_x and ('right' in moves):  # my neck is right of my head
        moves.remove("right")
    elif my_neck["y"] < my_head_y and ('down' in moves):  # my neck is below my head
        moves.remove("down")
    elif my_neck["y"] > my_head_y and ('up' in moves):  # my neck is above my head
        moves.remove("up")
 
def avoid_walls(lengthX, my_head_x, my_head_y, lengthY, moves):
  if (my_head_x == 0) and ('left' in moves): 
    moves.remove('left')
  if (my_head_x == lengthX-1) and ('right' in moves): 
    moves.remove('right') 
  if (my_head_y == 0) and ('down' in moves):
    moves.remove('down') 
  if (my_head_y == lengthY-1) and ('up' in moves): 
    moves.remove('up')

def snake_position(moves, my_head_x, my_head_y, lengthX, lengthY, snakes, snakesX):
  for i in snakes:
    for j in i['body']:
      snakesX.append((j.get('x'), j.get('y')))
  if (my_head_x-1, my_head_y) in snakesX and ('left' in moves):
    moves.remove('left')
  if(my_head_x, my_head_y-1) in snakesX and ('down' in moves):
    moves.remove('down')
  if (my_head_x+1, my_head_y) in snakesX and ('right' in moves):
    moves.remove('right')
  if(my_head_x, my_head_y+1) in snakesX and ('up' in moves):
    moves.remove('up')


def call_function(lengthX, lengthY,  my_head_x, my_head_y, my_body, snakes, snakesX, moves, food):
  avoid_walls(lengthX, my_head_x, my_head_y, lengthY, moves)
  snake_position(moves, my_head_x, my_head_y, lengthX, lengthY, snakes, snakesX)
  avoid_my_neck(my_head_x, my_head_y, my_body, moves)
  #hunt_food(my_head_x, my_head_y, moves, food)
  return moves    

def choose_move(data):
    snakesX = []
    food = data['board']['food']
    my_head_x = data["you"]["head"]['x']
    my_head_y = data['you']['head']['y']
    my_body = data["you"]["body"] 
    lengthX = data['board']['width']
    lengthY = data['board']['height']
    snakes = data['board']['snakes']
    # TODO: uncomment the lines below so you can see what this data looks like in your output!
    print(f"~~~ Turn: {data['turn']}  Game Mode: {data['game']['ruleset']['name']} ~~~")
    print(f"All board data this turn: {data}")
    print(f"My Battlesnakes head this turn is: {my_head_x}")
    print(f"My Battlesnakes body this turn is: {my_body}")

    moves = ["up", "down", "left", "right"]

    moves = call_function(lengthX,lengthY, my_head_x, my_head_y, my_body, snakes, snakesX, moves, food)
    move = random.choice(moves)

    print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {moves} \n ({my_head_x}, {my_head_y}), {my_body[1]['x']}, {my_body[1]['y']}, {snakesX}, {get_food(my_head_x, food)}, {snakes}")

    return move
