#!/usr/bin/python

class Course:
	def __init__(self, name, teacher):
		self.name = str(name)
		self.teacher = str(teacher)

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = str(name)

	def getTeacher(self):
		return self.teacher

	def setTeacher(self, teacher):
		self.teacher = str(teacher)
