# -*- coding: utf-8 -*-
    
#
    
from tkinter import *
import random

root = Tk()

btn = [] #Array storing all the buttons
numOfBombs = 400 #Number of bombs
numOfRows = 38 #Number of rows
numOfCols = 56 #Number of columns

StartRow = 12
StartCol = 10
StartIndex = ((StartRow-1)*numOfCols) + StartCol -1

btnNumber = 0 #Variable to track which button has been clicked

numOfClickedTiles = [0]*1

my_str=StringVar()
l1=Label(root,textvariable=my_str)
l1.grid(row=0,column=0,columnspan=10)

def FlagClick(event,x,y,index):
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
				
def ChordClick(event,x,y,index):
	
	btnBox = btn[index]
	nearbyFlagCount = 0
	
	if isClickedList[index]==1 and btnBox.cget('text')!="B":
		
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
				my_fun(event,x-1,y,index-1)
			if x!=numOfCols-1 and isFlaggedList[index+1]==0:
				my_fun(event,x+1,y,index+1)
			if y!=0 and isFlaggedList[index-numOfCols]==0:
				my_fun(event,x,y-1,index-numOfCols)
			if y!=numOfRows-1 and isFlaggedList[index+numOfCols]==0:
				my_fun(event,x,y+1,index+numOfCols)
			if x!=0 and y!=0 and isFlaggedList[index-1-numOfCols]==0:
				my_fun(event,x-1,y-1,index-1-numOfCols)
			if x!=numOfCols-1 and y!=0 and isFlaggedList[index+1-numOfCols]==0:
				my_fun(event,x+1,y-1,index+1-numOfCols)
			if x!=0 and y!=numOfRows-1 and isFlaggedList[index-1+numOfCols]==0:
				my_fun(event,x-1,y+1,index-1+numOfCols)
			if x!=numOfCols-1 and y!=numOfRows-1 and isFlaggedList[index+1+numOfCols]==0:
				my_fun(event,x+1,y+1,index+1+numOfCols)
			

def bombCheck(index):
    bombFlag = 0
    exist_count = isBombList.count(index)
    if exist_count > 0:
        bombFlag = 1
    
    return bombFlag

def showAllBombs():
	
	global waitTime
	for i in range(len(btn)):
		btnBox = btn[i]
		if bombCheck(i)==1 and isFlaggedList[i]==0:
			btnBox.config(text="💣")
			btnBox.config(fg="black")
	

def my_fun(event,x,y,index):
    #my_str.set("btn row is " + str(x) + " btn col is " + str(y) + " index is " + str(index))
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
				my_fun(event,x-1,y,index-1)
			if x!=numOfCols-1 and recursiveCheckList[index+1]==0:
				my_fun(event,x+1,y,index+1)
			if y!=0 and recursiveCheckList[index-numOfCols]==0:
				my_fun(event,x,y-1,index-numOfCols)
			if y!=numOfRows-1 and recursiveCheckList[index+numOfCols]==0:
				my_fun(event,x,y+1,index+numOfCols)
			if x!=0 and y!=0 and recursiveCheckList[index-1-numOfCols]==0:
				my_fun(event,x-1,y-1,index-1-numOfCols)
			if x!=numOfCols-1 and y!=0 and recursiveCheckList[index+1-numOfCols]==0:
				my_fun(event,x+1,y-1,index+1-numOfCols)
			if x!=0 and y!=numOfRows-1 and recursiveCheckList[index-1+numOfCols]==0:
				my_fun(event,x-1,y+1,index-1+numOfCols)
			if x!=numOfCols-1 and y!=numOfRows-1 and recursiveCheckList[index+1+numOfCols]==0:
				my_fun(event,x+1,y+1,index+1+numOfCols)
	    
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
	    
	    #Update cell number
	    #Check for bomb in current cell
		if bombCheck(index)==1:
			btnBox.config(text="💣")
			btnBox.config(fg="black")
			print("You Lose")
			showAllBombs()
		else:
			btnBox.config(text=str(nearbyBombCount))
			btnBox.config(relief="flat")
			btnBox.config(bg="#e9e9e9")
			
		numOfClickedTiles[0] = numOfClickedTiles[0] + 1
			
		#Check to see if you've won
		if numOfClickedTiles[0] == (numOfRows*numOfCols)-numOfBombs:
			print("You Win")
		
		
	isClickedList[index] = 1

    
    
#Loop which creates all the tiles
for i in range(numOfRows):
	for j in range(numOfCols):
		btn.append(Button(root, width=2, height=1, font='Terminal'))
		btn[btnNumber].bind('<Double-Button-1>', lambda event, x=j,y=i,index=btnNumber:my_fun(event,x,y,index))
		btn[btnNumber].bind('<Button-1>', lambda event, x=j,y=i,index=btnNumber:ChordClick(event,x,y,index))
		btn[btnNumber].bind('<Button-3>', lambda event, x=j,y=i,index=btnNumber:FlagClick(event,x,y,index))
		btn[btnNumber].grid(row=i+1,column=j)
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



root.mainloop()