# -*- coding: utf-8 -*-
   
    
from tkinter import *
import random
import math
import time

root = Tk()

btn = [] #Array storing all the buttons
numOfBombs = 400 #Number of bombs
numOfRows = 38 #Number of rows
numOfCols = 56 #Number of columns

initialPause = 2000
waitTime = 100
restartCount = 0

StartRow = 19
StartCol = 28
StartIndex = ((StartRow-1)*numOfCols) + StartCol -1

btnNumber = 0 #Variable to track which button has been clicked

numOfClickedTiles = 0


my_str=StringVar()
l1=Label(root,textvariable=my_str)
l1.grid(row=0,column=0,columnspan=10)

def FlagClick(x,y,index):
	btnBox = btn[index]
	if isClickedList[index]==0:
		if isFlaggedList[index]==0:
			btnBox.config(text="🚩")
			btnBox.config(fg="red")
			isFlaggedList[index] = 1
		else:
			if isFlaggedList[index]==1:
				btnBox.config(text="")
				isFlaggedList[index] = 0
				

def spiral(X, Y):
	updateCount = 0
	x = y = 0
	dx = 0
	dy = -1
	for i in range(max(X, Y)**2):
		if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
			#print (math.ceil(x+X/2),math.ceil(y+Y/2))
			xtemp = math.ceil(x+X/2)-1
			ytemp = math.ceil(y+Y/2)-1
			#plt.scatter(math.ceil(x+X/2),math.ceil(y+Y/2))
			indextemp = ((ytemp)*numOfCols) + xtemp
			btnBox = btn[indextemp]
			
			nearbyClickedCount = 0
			
			numOfNearbyTiles = 0
			
			if isClickedList[indextemp]==1:
				
				ChordClick(xtemp,ytemp,indextemp)
				
				#Check how many surrounding cells have been clicked
				#Check cell to the left
				if xtemp!=0 and isClickedList[indextemp-1]==1:
					nearbyClickedCount = nearbyClickedCount + 1
			    #Check cell to the right
				if xtemp!=numOfCols-1 and isClickedList[indextemp+1]==1:
					nearbyClickedCount = nearbyClickedCount + 1
			    #Check cell above
				if ytemp!=0 and isClickedList[indextemp-numOfCols]==1:
					nearbyClickedCount = nearbyClickedCount + 1
			    #Check cell below
				if ytemp!=numOfRows-1 and isClickedList[indextemp+numOfCols]==1:
					nearbyClickedCount = nearbyClickedCount + 1
			    #Check cell up & left
				if xtemp!=0 and ytemp!=0 and isClickedList[indextemp-1-numOfCols]==1:
					nearbyClickedCount = nearbyClickedCount + 1
			    #Check cell up & right
				if xtemp!=numOfCols-1 and ytemp!=0 and isClickedList[indextemp+1-numOfCols]==1:
					nearbyClickedCount = nearbyClickedCount + 1
			    #Check cell down & left
				if xtemp!=0 and ytemp!=numOfRows-1 and isClickedList[indextemp-1+numOfCols]==1:
					nearbyClickedCount = nearbyClickedCount + 1
			    #Check cell down & right
				if xtemp!=numOfCols-1 and ytemp!=numOfRows-1 and isClickedList[indextemp+1+numOfCols]==1:
					nearbyClickedCount = nearbyClickedCount + 1
				
				if xtemp!=0 and xtemp!=numOfCols-1 and ytemp!=0 and ytemp!=numOfRows-1:
					numOfNearbyTiles = 8
				if xtemp==0 and ytemp!=0 and ytemp!=numOfRows-1:
					numOfNearbyTiles = 5
				if xtemp==0 and ytemp==0:
					numOfNearbyTiles = 3
				if xtemp==0 and ytemp==numOfRows-1:
					numOfNearbyTiles = 3
				if xtemp!=0 and xtemp!=numOfCols-1 and ytemp==0:
					numOfNearbyTiles = 5
				if xtemp!=0 and xtemp!=numOfCols-1 and ytemp==numOfRows-1:
					numOfNearbyTiles = 5
				if xtemp==numOfCols-1 and ytemp!=0 and ytemp!=numOfRows-1:
					numOfNearbyTiles = 5
				if xtemp==numOfCols-1 and ytemp==0:
					numOfNearbyTiles = 3
				if xtemp==numOfCols-1 and ytemp==numOfRows-1:
					numOfNearbyTiles = 3
				if numOfNearbyTiles==0:
					print("Nearby tile count has failed")
				
				if nearbyClickedCount == numOfNearbyTiles-int(btnBox.cget('text')):
					
					#flag all non-clicked cells
					if xtemp!=0 and isClickedList[indextemp-1]==0 and isFlaggedList[indextemp-1]==0:
						updateCount = updateCount + 1
						FlagClick(xtemp-1,ytemp,indextemp-1)
					if xtemp!=numOfCols-1 and isClickedList[indextemp+1]==0 and isFlaggedList[indextemp+1]==0:
						updateCount = updateCount + 1
						FlagClick(xtemp+1,ytemp,indextemp+1)
					if ytemp!=0 and isClickedList[indextemp-numOfCols]==0 and isFlaggedList[indextemp-numOfCols]==0:
						updateCount = updateCount + 1
						FlagClick(xtemp,ytemp-1,indextemp-numOfCols)
					if ytemp!=numOfRows-1 and isClickedList[indextemp+numOfCols]==0 and isFlaggedList[indextemp+numOfCols]==0:
						updateCount = updateCount + 1
						FlagClick(xtemp,ytemp+1,indextemp+numOfCols)
					if xtemp!=0 and ytemp!=0 and isClickedList[indextemp-1-numOfCols]==0 and isFlaggedList[indextemp-1-numOfCols]==0:
						updateCount = updateCount + 1
						FlagClick(xtemp-1,ytemp-1,indextemp-1-numOfCols)
					if xtemp!=numOfCols-1 and ytemp!=0 and isClickedList[indextemp+1-numOfCols]==0 and isFlaggedList[indextemp+1-numOfCols]==0:
						updateCount = updateCount + 1
						FlagClick(xtemp+1,ytemp-1,indextemp+1-numOfCols)
					if xtemp!=0 and ytemp!=numOfRows-1 and isClickedList[indextemp-1+numOfCols]==0 and isFlaggedList[indextemp-1+numOfCols]==0:
						updateCount = updateCount + 1
						FlagClick(xtemp-1,ytemp+1,indextemp-1+numOfCols)
					if xtemp!=numOfCols-1 and ytemp!=numOfRows-1 and isClickedList[indextemp+1+numOfCols]==0 and isFlaggedList[indextemp+1+numOfCols]==0:
						updateCount = updateCount + 1
						FlagClick(xtemp+1,ytemp+1,indextemp+1+numOfCols)
				
		if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
			dx, dy = -dy, dx
		x, y = x+dx, y+dy
	
	global restartCount
	global waitTime
	
	if updateCount == 0:
		restartCount = restartCount + 1
		
	if restartCount < 5:
		root.after(waitTime, spiral, numOfCols, numOfRows)
	else:
		root.after(waitTime, spiralMaybes, numOfCols, numOfRows)
		
def spiralGuess(X, Y):
	#print("guess")
	
	global restartCount
	global waitTime
	
	onlyClickOneCount = 0
	
	x = y = 0
	dx = 0
	dy = -1
	for i in range(max(X, Y)**2):
		if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
			#print (math.ceil(x+X/2),math.ceil(y+Y/2))
			xtemp = math.ceil(x+X/2)-1
			ytemp = math.ceil(y+Y/2)-1
			#plt.scatter(math.ceil(x+X/2),math.ceil(y+Y/2))
			indextemp = ((ytemp)*numOfCols) + xtemp
			btnBox = btn[indextemp]
			
			if isClickedList[indextemp]==0 and isFlaggedList[indextemp]==0 and onlyClickOneCount==0:
				onlyClickOneCount = 1
				#print("guess",xtemp,ytemp,indextemp)
				my_fun(xtemp,ytemp,indextemp)
				if bombCheck(indextemp)==1:
					root.after(2*waitTime, showAllBombs)
				else:
					restartCount = 0
					root.after(waitTime, spiral, numOfCols, numOfRows)
			
				
		if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
			dx, dy = -dy, dx
		x, y = x+dx, y+dy
		
def spiralMaybes(X, Y):
	#print("maybe")
	
	global restartCount
	
	hasBeenSuccess = 99999
	successX = 99999
	successY = 99999
	
	x = y = 0
	dx = 0
	dy = -1
	for i in range(max(X, Y)**2):
		
		if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
			#print (math.ceil(x+X/2),math.ceil(y+Y/2))
			xtemp = math.ceil(x+X/2)-1
			ytemp = math.ceil(y+Y/2)-1
			#plt.scatter(math.ceil(x+X/2),math.ceil(y+Y/2))
			indextemp = ((ytemp)*numOfCols) + xtemp
			btnBox = btn[indextemp]
			
			if hasBeenSuccess == 99999:
				if isClickedList[indextemp]==0 and isFlaggedList[indextemp]==0:
					#Flag it as a maybe
					maybeFlaggedList[indextemp]=1
					checkComplete = 0
					
					#check a 10 by 10 area around the investigated cell 10 times
					for t in range(10): #t for "time" tracks number of times looped
						for a in range(-5,5): #a acts as proxy for x
							for b in range (-5,5): #b acts as proxy for y
								atemp = xtemp+a
								btemp = ytemp+b
								abindextemp = ((btemp)*numOfCols) + atemp
								
								nearbyClickedCount = 0
								
								numOfNearbyTiles = 0
								if atemp>=0 and btemp>=0 and atemp<=numOfCols-1 and btemp<=numOfRows-1:
									#print(atemp,btemp,abindextemp)
									if checkComplete==0 and isClickedList[abindextemp]==1:
										btnBoxTemp = btn[abindextemp]
										
										#First check if nearby flagged or maybeFlagged cells = number of surrounding bombs (maybeChordClick)
										nearbyFlagCount = 0
											
										#Check number of nearby flagged or maybeFlagged cells
										#Check cell to the left
										if atemp!=0 and (isFlaggedList[abindextemp-1]==1 or maybeFlaggedList[abindextemp-1]==1):
											nearbyFlagCount = nearbyFlagCount + 1
									    #Check cell to the right
										if atemp!=numOfCols-1 and (isFlaggedList[abindextemp+1]==1 or maybeFlaggedList[abindextemp+1]==1):
											nearbyFlagCount = nearbyFlagCount + 1
									    #Check cell above
										if btemp!=0 and (isFlaggedList[abindextemp-numOfCols]==1 or maybeFlaggedList[abindextemp-numOfCols]==1):
											nearbyFlagCount = nearbyFlagCount + 1
									    #Check cell below
										if btemp!=numOfRows-1 and (isFlaggedList[abindextemp+numOfCols]==1 or maybeFlaggedList[abindextemp+numOfCols]==1):
											nearbyFlagCount = nearbyFlagCount + 1
									    #Check cell up & left
										if atemp!=0 and btemp!=0 and (isFlaggedList[abindextemp-1-numOfCols]==1 or maybeFlaggedList[abindextemp-1-numOfCols]==1):
											nearbyFlagCount = nearbyFlagCount + 1
									    #Check cell up & right
										if atemp!=numOfCols-1 and btemp!=0 and (isFlaggedList[abindextemp+1-numOfCols]==1 or maybeFlaggedList[abindextemp+1-numOfCols]==1):
											nearbyFlagCount = nearbyFlagCount + 1
									    #Check cell down & left
										if atemp!=0 and btemp!=numOfRows-1 and (isFlaggedList[abindextemp-1+numOfCols]==1 or maybeFlaggedList[abindextemp-1+numOfCols]==1):
											nearbyFlagCount = nearbyFlagCount + 1
									    #Check cell down & right
										if atemp!=numOfCols-1 and btemp!=numOfRows-1 and (isFlaggedList[abindextemp+1+numOfCols]==1 or maybeFlaggedList[abindextemp+1+numOfCols]==1):
											nearbyFlagCount = nearbyFlagCount + 1
																			
										if nearbyFlagCount > int(btnBoxTemp.cget('text')):
											#This means that the initially maybe flagged cell is actually clear
											checkComplete = 1
											hasBeenSuccess = indextemp
											successX = xtemp
											successY = ytemp
										
										
										#Check if all nearby bombs have been flagged or maybeFlagged
										if checkComplete==0 and nearbyFlagCount==int(btnBoxTemp.cget('text')):
											#maybeClick all non-flagged nearby tiles
											if atemp!=0 and (isFlaggedList[abindextemp-1]==0 and maybeFlaggedList[abindextemp-1]==0):
												maybeClickedList[abindextemp-1] = 1
											if atemp!=numOfCols-1 and (isFlaggedList[abindextemp+1]==0 and maybeFlaggedList[abindextemp+1]==0):
												maybeClickedList[abindextemp+1] = 1
											if btemp!=0 and (isFlaggedList[abindextemp-numOfCols]==0 and maybeFlaggedList[abindextemp-numOfCols]==0):
												maybeClickedList[abindextemp-numOfCols] = 1
											if btemp!=numOfRows-1 and (isFlaggedList[abindextemp+numOfCols]==0 and maybeFlaggedList[abindextemp+numOfCols]==0):
												maybeClickedList[abindextemp+numOfCols] = 1
											if atemp!=0 and btemp!=0 and (isFlaggedList[abindextemp-1-numOfCols]==0 and maybeFlaggedList[abindextemp-1-numOfCols]==0):
												maybeClickedList[abindextemp-1-numOfCols] = 1
											if atemp!=numOfCols-1 and btemp!=0 and (isFlaggedList[abindextemp+1-numOfCols]==0 and maybeFlaggedList[abindextemp+1-numOfCols]==0):
												maybeClickedList[abindextemp+1-numOfCols] = 1
											if atemp!=0 and btemp!=numOfRows-1 and (isFlaggedList[abindextemp-1+numOfCols]==0 and maybeFlaggedList[abindextemp-1+numOfCols]==0):
												maybeClickedList[abindextemp-1+numOfCols] = 1
											if atemp!=numOfCols-1 and btemp!=numOfRows-1 and (isFlaggedList[abindextemp+1+numOfCols]==0 and maybeFlaggedList[abindextemp+1+numOfCols]==0):
												maybeClickedList[abindextemp+1+numOfCols] = 1
										
										#Check how many surrounding cells have been clicked or maybe clicked
										#Check cell to the left
										if atemp!=0 and (isClickedList[abindextemp-1]==1 or maybeClickedList[abindextemp-1]==1):
											nearbyClickedCount = nearbyClickedCount + 1
									    #Check cell to the right
										if atemp!=numOfCols-1 and (isClickedList[abindextemp+1]==1 or maybeClickedList[abindextemp+1]==1):
											nearbyClickedCount = nearbyClickedCount + 1
									    #Check cell above
										if btemp!=0 and (isClickedList[abindextemp-numOfCols]==1 or maybeClickedList[abindextemp-numOfCols]==1):
											nearbyClickedCount = nearbyClickedCount + 1
									    #Check cell below
										if btemp!=numOfRows-1 and (isClickedList[abindextemp+numOfCols]==1 or maybeClickedList[abindextemp+numOfCols]==1):
											nearbyClickedCount = nearbyClickedCount + 1
									    #Check cell up & left
										if atemp!=0 and btemp!=0 and (isClickedList[abindextemp-1-numOfCols]==1 or maybeClickedList[abindextemp-1-numOfCols]==1):
											nearbyClickedCount = nearbyClickedCount + 1
									    #Check cell up & right
										if atemp!=numOfCols-1 and btemp!=0 and (isClickedList[abindextemp+1-numOfCols]==1 or maybeClickedList[abindextemp+1-numOfCols]==1):
											nearbyClickedCount = nearbyClickedCount + 1
									    #Check cell down & left
										if atemp!=0 and btemp!=numOfRows-1 and (isClickedList[abindextemp-1+numOfCols]==1 or maybeClickedList[abindextemp-1+numOfCols]==1):
											nearbyClickedCount = nearbyClickedCount + 1
									    #Check cell down & right
										if atemp!=numOfCols-1 and btemp!=numOfRows-1 and (isClickedList[abindextemp+1+numOfCols]==1 or maybeClickedList[abindextemp+1+numOfCols]==1):
											nearbyClickedCount = nearbyClickedCount + 1
										
										#calculate number of nearby tiles
										if atemp!=0 and atemp!=numOfCols-1 and btemp!=0 and btemp!=numOfRows-1:
											numOfNearbyTiles = 8
										if atemp==0 and btemp!=0 and btemp!=numOfRows-1:
											numOfNearbyTiles = 5
										if atemp==0 and btemp==0:
											numOfNearbyTiles = 3
										if atemp==0 and btemp==numOfRows-1:
											numOfNearbyTiles = 3
										if atemp!=0 and atemp!=numOfCols-1 and btemp==0:
											numOfNearbyTiles = 5
										if atemp!=0 and atemp!=numOfCols-1 and btemp==numOfRows-1:
											numOfNearbyTiles = 5
										if atemp==numOfCols-1 and btemp!=0 and btemp!=numOfRows-1:
											numOfNearbyTiles = 5
										if atemp==numOfCols-1 and btemp==0:
											numOfNearbyTiles = 3
										if atemp==numOfCols-1 and btemp==numOfRows-1:
											numOfNearbyTiles = 3
										if numOfNearbyTiles==0:
											print("Nearby tile count has failed")
											
										#print(atemp,btemp,numOfNearbyTiles)
											
										if nearbyFlagCount + nearbyClickedCount == numOfNearbyTiles and nearbyFlagCount < int(btnBoxTemp.cget('text')):
											#This means that the initially maybe flagged cell is actually clear
											checkComplete = 1
											hasBeenSuccess = indextemp
											successX = xtemp
											successY = ytemp
										
										
										if checkComplete==0 and nearbyClickedCount == numOfNearbyTiles-int(btnBoxTemp.cget('text')):
											
											#maybeFlag all non-clicked cells
											if atemp!=0 and isClickedList[abindextemp-1]==0 and isFlaggedList[abindextemp-1]==0 and maybeClickedList[abindextemp-1]==0 and maybeFlaggedList[abindextemp-1]==0:
												maybeFlaggedList[abindextemp-1] = 1
											if atemp!=numOfCols-1 and isClickedList[abindextemp+1]==0 and isFlaggedList[abindextemp+1]==0 and maybeClickedList[abindextemp+1]==0 and maybeFlaggedList[abindextemp+1]==0:
												maybeFlaggedList[abindextemp+1] = 1
											if btemp!=0 and isClickedList[abindextemp-numOfCols]==0 and isFlaggedList[abindextemp-numOfCols]==0 and maybeClickedList[abindextemp-numOfCols]==0 and maybeFlaggedList[abindextemp-numOfCols]==0:
												maybeFlaggedList[abindextemp-numOfCols] = 1
											if btemp!=numOfRows-1 and isClickedList[abindextemp+numOfCols]==0 and isFlaggedList[abindextemp+numOfCols]==0 and maybeClickedList[abindextemp+numOfCols]==0 and maybeFlaggedList[abindextemp+numOfCols]==0:
												maybeFlaggedList[abindextemp+numOfCols] = 1
											if atemp!=0 and btemp!=0 and isClickedList[abindextemp-1-numOfCols]==0 and isFlaggedList[abindextemp-1-numOfCols]==0 and maybeClickedList[abindextemp-1-numOfCols]==0 and maybeFlaggedList[abindextemp-1-numOfCols]==0:
												maybeFlaggedList[abindextemp-1-numOfCols] = 1
											if atemp!=numOfCols-1 and btemp!=0 and isClickedList[abindextemp+1-numOfCols]==0 and isFlaggedList[abindextemp+1-numOfCols]==0 and maybeClickedList[abindextemp+1-numOfCols]==0 and maybeFlaggedList[abindextemp+1-numOfCols]==0:
												maybeFlaggedList[abindextemp+1-numOfCols] = 1
											if atemp!=0 and btemp!=numOfRows-1 and isClickedList[abindextemp-1+numOfCols]==0 and isFlaggedList[abindextemp-1+numOfCols]==0 and maybeClickedList[abindextemp-1+numOfCols]==0 and maybeFlaggedList[abindextemp-1+numOfCols]==0:
												maybeFlaggedList[abindextemp-1+numOfCols] = 1
											if atemp!=numOfCols-1 and btemp!=numOfRows-1 and isClickedList[abindextemp+1+numOfCols]==0 and isFlaggedList[abindextemp+1+numOfCols]==0 and maybeClickedList[abindextemp+1+numOfCols]==0 and maybeFlaggedList[abindextemp+1+numOfCols]==0:
												maybeFlaggedList[abindextemp+1+numOfCols] = 1
										
									
					#reset maybleFlaggedList and maybeClickedList
					for k in range(len(maybeFlaggedList)):
						maybeFlaggedList[k]=0
						maybeClickedList[k]=0
					
		if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
			dx, dy = -dy, dx
		x, y = x+dx, y+dy
		
		global waitTime
	
	if hasBeenSuccess != 99999:
		#print(successX,successY,hasBeenSuccess)
		restartCount = 0
		my_fun(successX,successY,hasBeenSuccess)
		root.after(waitTime, spiral, numOfCols, numOfRows)
	else:
		root.after(waitTime, spiralGuess, numOfCols, numOfRows)

		
def showAllBombs():
	
	global waitTime
	for i in range(len(btn)):
		btnBox = btn[i]
		if bombCheck(i)==1 and isFlaggedList[i]==0:
			btnBox.config(text="💣")
			btnBox.config(fg="black")
	
	root.after(waitTime, restartSweep)
				
def ChordClick(x,y,index):
	
	btnBox = btn[index]
	nearbyFlagCount = 0
	
	if isClickedList[index]==1 and btnBox.cget('text')!="💣":
		
		#Check number of nearby flagged cells
		#Check cell to the left
		if x!=0 and isFlaggedList[index-1]==1:
			nearbyFlagCount = nearbyFlagCount + 1
	    #Check cell to the right
		if x!=numOfCols-1 and isFlaggedList[index+1]==1:
			nearbyFlagCount = nearbyFlagCount + 1
	    #Check cell above
		if y!=0 and isFlaggedList[index-numOfCols]==1:
			nearbyFlagCount = nearbyFlagCount + 1
	    #Check cell below
		if y!=numOfRows-1 and isFlaggedList[index+numOfCols]==1:
			nearbyFlagCount = nearbyFlagCount + 1
	    #Check cell up & left
		if x!=0 and y!=0 and isFlaggedList[index-1-numOfCols]==1:
			nearbyFlagCount = nearbyFlagCount + 1
	    #Check cell up & right
		if x!=numOfCols-1 and y!=0 and isFlaggedList[index+1-numOfCols]==1:
			nearbyFlagCount = nearbyFlagCount + 1
	    #Check cell down & left
		if x!=0 and y!=numOfRows-1 and isFlaggedList[index-1+numOfCols]==1:
			nearbyFlagCount = nearbyFlagCount + 1
	    #Check cell down & right
		if x!=numOfCols-1 and y!=numOfRows-1 and isFlaggedList[index+1+numOfCols]==1:
			nearbyFlagCount = nearbyFlagCount + 1
			
		#print("Nearby flag count is " + str(nearbyFlagCount) + " and nearby bomb count is " + btnBox.cget('text'))
		
		#Check if all nearby bombs have been flagged
		if nearbyFlagCount==int(btnBox.cget('text')):
			#print("match")
			#reveal all non-flagged nearby tiles
			if x!=0 and isFlaggedList[index-1]==0:
				my_fun(x-1,y,index-1)
			if x!=numOfCols-1 and isFlaggedList[index+1]==0:
				my_fun(x+1,y,index+1)
			if y!=0 and isFlaggedList[index-numOfCols]==0:
				my_fun(x,y-1,index-numOfCols)
			if y!=numOfRows-1 and isFlaggedList[index+numOfCols]==0:
				my_fun(x,y+1,index+numOfCols)
			if x!=0 and y!=0 and isFlaggedList[index-1-numOfCols]==0:
				my_fun(x-1,y-1,index-1-numOfCols)
			if x!=numOfCols-1 and y!=0 and isFlaggedList[index+1-numOfCols]==0:
				my_fun(x+1,y-1,index+1-numOfCols)
			if x!=0 and y!=numOfRows-1 and isFlaggedList[index-1+numOfCols]==0:
				my_fun(x-1,y+1,index-1+numOfCols)
			if x!=numOfCols-1 and y!=numOfRows-1 and isFlaggedList[index+1+numOfCols]==0:
				my_fun(x+1,y+1,index+1+numOfCols)
			

def bombCheck(index):
    bombFlag = 0
    exist_count = isBombList.count(index)
    if exist_count > 0:
        bombFlag = 1
    
    return bombFlag

def restartSweep():
	
	#Create a list of all the tiles. Take a random sample from that list to assign bombs to
	list_of_numbers = list(range(0, len(btn)))
	#First remove the start tile and it's surrounding tiles 
	del list_of_numbers[StartIndex+numOfCols+1]
	del list_of_numbers[StartIndex+numOfCols]
	del list_of_numbers[StartIndex+numOfCols-1]
	del list_of_numbers[StartIndex+1]
	del list_of_numbers[StartIndex]
	del list_of_numbers[StartIndex-1]
	del list_of_numbers[StartIndex-numOfCols+1]
	del list_of_numbers[StartIndex-numOfCols]
	del list_of_numbers[StartIndex-numOfCols-1]
	
	global isFlaggedList
	global isClickedList
	global recursiveCheckList
	global numOfClickedTiles
	
	isFlaggedList = [0] * len(btn)
	isClickedList = [0] * len(btn)
	recursiveCheckList = [0] * len(btn)
	numOfClickedTiles = 0
	
	global isBombList
	
	isBombList = random.sample(list_of_numbers,numOfBombs)
	
	#Reset all tile appearances
	for k in range(len(btn)):
		btnBox = btn[k]
		btnBox.config(bg='SystemButtonFace')
		btnBox.config(relief="raised")
		btnBox.config(text="")
		btnBox.config(image="")
		
	global restartCount
	
	restartCount = 0
	
	root.after(10, my_fun, StartCol-1, StartRow-1,StartIndex)
	root.after(waitTime+10, spiral, numOfCols, numOfRows)
	

def my_fun(x,y,index):
    #my_str.set("btn row is " + str(x) + " btn col is " + str(y) + " index is " + str(index))
	global waitTime
	btnBox = btn[index]

	nearbyBombCount = 0
    
	if isClickedList[index]==0:
		
	    #Check for bombs in surounding cells
	    #Check cell to the left
		if x!=0 and bombCheck(index-1)==1:
			nearbyBombCount = nearbyBombCount + 1
	    #Check cell to the right
		if x!=numOfCols-1 and bombCheck(index+1)==1:
			nearbyBombCount = nearbyBombCount + 1
	    #Check cell above
		if y!=0 and bombCheck(index-numOfCols)==1:
			nearbyBombCount = nearbyBombCount + 1
	    #Check cell below
		if y!=numOfRows-1 and bombCheck(index+numOfCols)==1:
			nearbyBombCount = nearbyBombCount + 1
	    #Check cell up & left
		if x!=0 and y!=0 and bombCheck(index-1-numOfCols)==1:
			nearbyBombCount = nearbyBombCount + 1
	    #Check cell up & right
		if x!=numOfCols-1 and y!=0 and bombCheck(index+1-numOfCols)==1:
			nearbyBombCount = nearbyBombCount + 1
	    #Check cell down & left
		if x!=0 and y!=numOfRows-1 and bombCheck(index-1+numOfCols)==1:
			nearbyBombCount = nearbyBombCount + 1
	    #Check cell down & right
		if x!=numOfCols-1 and y!=numOfRows-1 and bombCheck(index+1+numOfCols)==1:
			nearbyBombCount = nearbyBombCount + 1
			
		if nearbyBombCount ==0 and bombCheck(index)!=1:
			recursiveCheckList[index] = 1
			if x!=0 and recursiveCheckList[index-1]==0:
				my_fun(x-1,y,index-1)
			if x!=numOfCols-1 and recursiveCheckList[index+1]==0:
				my_fun(x+1,y,index+1)
			if y!=0 and recursiveCheckList[index-numOfCols]==0:
				my_fun(x,y-1,index-numOfCols)
			if y!=numOfRows-1 and recursiveCheckList[index+numOfCols]==0:
				my_fun(x,y+1,index+numOfCols)
			if x!=0 and y!=0 and recursiveCheckList[index-1-numOfCols]==0:
				my_fun(x-1,y-1,index-1-numOfCols)
			if x!=numOfCols-1 and y!=0 and recursiveCheckList[index+1-numOfCols]==0:
				my_fun(x+1,y-1,index+1-numOfCols)
			if x!=0 and y!=numOfRows-1 and recursiveCheckList[index-1+numOfCols]==0:
				my_fun(x-1,y+1,index-1+numOfCols)
			if x!=numOfCols-1 and y!=numOfRows-1 and recursiveCheckList[index+1+numOfCols]==0:
				my_fun(x+1,y+1,index+1+numOfCols)
	    
	    #Set the font colour based on number of bombs nearby
		if nearbyBombCount == 0:
			btnBox.config(fg="#e9e9e9")
		elif nearbyBombCount == 1:
			btnBox.config(fg="blue")
		elif nearbyBombCount == 2:
			btnBox.config(fg="green")
		elif nearbyBombCount == 3:
			btnBox.config(fg="red")
		elif nearbyBombCount == 4:
			btnBox.config(fg="#9900ff")
		elif nearbyBombCount == 5:
			btnBox.config(fg="#660000")
		elif nearbyBombCount == 6:
			btnBox.config(fg="#4a86e8")
		elif nearbyBombCount == 7:
			btnBox.config(fg="black")
		elif nearbyBombCount == 8:
			btnBox.config(fg="#d9d9d9")
		else: 
			pass
		
		global numOfClickedTiles
		
		numOfClickedTiles = numOfClickedTiles + 1
	    
	    #Update cell number
	    #Check for bomb in current cell
		if bombCheck(index)==1:
			btnBox.config(text="💣")
			btnBox.config(fg="black")
			print("You Lose")
		else:
			btnBox.config(text=str(nearbyBombCount))
			btnBox.config(relief="flat")
			btnBox.config(bg="#e9e9e9")
			#Check to see if you've won
			if numOfClickedTiles == (numOfRows*numOfCols)-numOfBombs:
				print("You Win")
				root.after(3*waitTime, restartSweep)
		
		
	isClickedList[index] = 1

    
    
#Loop which creates all the tiles
for i in range(numOfRows):
	for j in range(numOfCols):
		btn.append(Button(root, width=2, height=1, font='Terminal'))
		btn[btnNumber].grid(row=i,column=j)
		btnNumber = btnNumber + 1

#Create a list of all the tiles. Take a random sample from that list to assign bombs to
list_of_numbers = list(range(0, len(btn)))
#First remove the start tile and it's surrounding tiles 
btn[StartIndex].config(text="S")
del list_of_numbers[StartIndex+numOfCols+1]
del list_of_numbers[StartIndex+numOfCols]
del list_of_numbers[StartIndex+numOfCols-1]
del list_of_numbers[StartIndex+1]
del list_of_numbers[StartIndex]
del list_of_numbers[StartIndex-1]
del list_of_numbers[StartIndex-numOfCols+1]
del list_of_numbers[StartIndex-numOfCols]
del list_of_numbers[StartIndex-numOfCols-1]

isBombList = random.sample(list_of_numbers,numOfBombs)

#Create lists to store whether a button has been flagged or clicked
isFlaggedList = [0] * len(btn)
isClickedList = [0] * len(btn)
recursiveCheckList = [0] * len(btn)

maybeFlaggedList = [0] * len(btn)
maybeClickedList = [0] * len(btn)


#root.geometry("1920x1080")

root.after(initialPause, my_fun, StartCol-1, StartRow-1,StartIndex)
root.after(initialPause+waitTime, spiral, numOfCols, numOfRows)
root.mainloop()