import turtle

num_sides = int(input('Put how many sides do you need'))

for steps in range(num_sides):
  turtle.color('red')
  turtle.right(360/num_sides) # 90grad (povorot v pravo)
  turtle.forward(100)
  
  for steps in range(num_sides):
    turtle.color('red')
    turtle.right(360/num_sides) # 90grad (povorot v pravo)
    turtle.forward(75)


