#!/usr/bin/python

#Regle 1 : Ajouter un vecteur centre
#Regle 2 : Moyenne des vitesses
#Regle 3 : Air d'espace entre les tortues pour eviter la superposition
#Regle 4 : Eviter que les tortues sortent du cadre de l'ecran

import turtle
import math
import random

#Nombre de tortues
n=20
#Instance de tortues
boids=[]
#vitesse
s=1
#Zone de repulsion
zdr=20
regle1=[]
regle2=[0,0]
regle3=[]
regle4=[]
#Coef des regles
r1=.1
r2=.1
r3=.4
r4=1.0

turtle.tracer(50,1)
turtle.color("white")
for i in range(n):
	boids.append(turtle.Turtle())
	boids[i].penup()
	boids[i].setposition(random.randint(-100,100), random.randint(-100,100))
	boids[i].setheading(random.randint(0,359))
	boids[i].color(random.random(),random.random(),random.random())
	boids[i].pendown()
	
	regle1.append([0,0])
	regle3.append([0,0])
	regle4.append([0,0])

while True:
	#Regle 1
	pmX=0
	pmY=0
	for i in range(n):
		pmX+=boids[i].xcor()
		pmY+=boids[i].ycor()
	pmX/=n
	pmY/=n
	
	for i in range(n):
		regle1[i][0]=pmX-boids[i].xcor()
		regle1[i][1]=pmY-boids[i].ycor()
	
	#Regle 2
	angle=0
	for i in range(n):
		angle+=boids[i].heading()
	angle/=n
	regle2[0] = s * math.cos(angle/57.17)
	regle2[1] = s * math.sin(angle/57.17)
	
	#Regle 3
	for i in range(n):
		nbs=0
		pox, poy = 0, 0
		for boid in boids :
			if boid != boids[i]:
				if math.sqrt(math.pow(boid.xcor()-boids[i].xcor(),2)+math.pow(boid.ycor()-boids[i].ycor(),2)) < zdr:
					pox+=boid.xcor()
					poy+=boid.ycor()
					nbs+=1
		if nbs > 0 :
			pox/=nbs
			poy/=nbs
			regle3[i][0] = boids[i].xcor() - pox
			regle3[i][1] = boids[i].ycor() - poy
	
	#Regle 4	
	hauteur, largeur = turtle.screensize()
	for i in range(n):
		regle4[i][0]=0
		regle4[i][1]=0
		if boids[i].xcor() > largeur/2:
			regle4[i][0]=-10
		elif boids[i].xcor() < -largeur/2:
			regle4[i][0]=10
		
		if boids[i].ycor() > hauteur/2:
			regle4[i][1]=-10
		elif boids[i].ycor() < -hauteur/2:
			regle4[i][1]=10
			
	
	#Application des regles
	for i in range(n):
		v=[0,0]
		v[0] = r1 * regle1[i][0] + r2 * regle2[0] + r3 * regle3[i][0] + r4 * regle4[i][0]
		v[1] = r1 * regle1[i][1] + r2 * regle2[1] + r3 * regle3[i][1] + r4 * regle4[i][1]
		boids[i].setheading(math.atan2(v[1], v[0])*57.17)
		boids[i].forward(s)
					
raw_input("Appuyer sur ENTRER")


