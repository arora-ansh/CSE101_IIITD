import os
import time
import random

class Grid:

	def __init__(self,N,start,goal,myObstacles,myRewards):
		self.N=N
		self.start=start
		self.goal=goal
		self.myObstacles=myObstacles
		self.myRewards=myRewards

	def rotateClockwise(self):
		pass

	def rotateAnticlockwise(self):
		pass

	def showGrid(self):
		pass

class Obstacle:

	def __init__(self,x,y):
		self.x=x
		self.y=y

class Reward:

	def __init__(self,x,y,value ):
		self.x=x
		self.y=y
		self.value=value

	assert (value>=1 and value<=9)

class Player:

	def __init__(self,x,y,energy):
		self.x=x
		self.y=y
		self.energy=energy

	def makeMove(self,s):
		pass