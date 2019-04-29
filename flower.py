#!/bin/python3
import turtle

def draw_diamond(name,size):
  name.forward(size)
  name.right(60)
  name.forward(size)
  name.right(120)
  name.forward(size)
  name.right(60)
  name.forward(size)
  name.right(120)

def draw_flower():
  window = turtle.Screen()
  window.bgcolor("orange")
  f = turtle.Turtle()
  f.shape("turtle")
  f.color("purple")
  f.speed(20)
  for i in range (0,36):
    draw_diamond(f,50)
    f.right(10)
  f.color("green")
  f.right(90)
  f.forward(150)
  f.left(160)
  draw_diamond(f,25)
  f.left(90)
  draw_diamond(f,25)
    
draw_flower()
