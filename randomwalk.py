import turtle
import numpy as np

def rand():
  return np.random.rand()

"""TODO: outputs either 0, 90, 180, 270
with equal 25% probability"""
def randomDirection():
  return()

"""Already written function """
def randomMove(bob):
  angle = randomDirection()
  bob.setheading(angle)
  bob.forward(3)

def main():
  #setting up the turtle
  bob = turtle.Turtle()
  bob.speed(0)
  bob._delay(0)

  #randomly moving the turtle a given number of steps
  n_steps = 100
  for _ in range(n_steps):
    randomMove(bob)

  turtle.done()

main()
