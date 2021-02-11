from tkinter import *
import math

# Defining Commands
def button_click(number):
	val = a.get()
	a.delete(0,END)
	a.insert(0,val + number)
def button_click_1(number):
	val = a.get().split()
	val.insert(len(val)-2 , number)
	str1 = ""     
	for i in val :
		str1 += i
	a.delete(0,END)
	a.insert(0,str(str1))
def clear():
	a.delete(0,END)



# Defining BODMAS
def equal():
	ans = a.get().split()
	for i in range(ans.count("sqrt")):
		ans [ ( ans.index( "sqrt" ) + 1 ) ] = math.sqrt( float( ans[ ( ans.index( "sqrt" ) + 1 ) ] ) )
		ans.pop( ans.index( "sqrt" ) )
	for i in range(ans.count("**")):
		ans [ ( ans.index( "**" ) - 1 ) ] = float(ans[ ( ans.index( "**" ) - 1 ) ]) ** float(ans[ ( ans.index( "**" ) + 1 ) ])
		ans.pop( ans.index( "**" ) + 1  )
		ans.pop( ans.index( "**" ))
	for i in range(ans.count("/")):
		ans [ ( ans.index( "/" ) - 1 ) ] = float(ans[ ( ans.index( "/" ) - 1 ) ]) / float(ans[ ( ans.index( "/" ) + 1 ) ])
		ans.pop( ans.index( "/" ) + 1  )
		ans.pop( ans.index( "/" ))
	for i in range(ans.count("*")):
		ans [ ( ans.index( "*" ) - 1 ) ] = float(ans[ ( ans.index( "*" ) - 1 ) ]) * float(ans[ ( ans.index( "*" ) + 1 ) ])
		ans.pop( ans.index( "*" ) + 1  )
		ans.pop( ans.index( "*" )  )
	for i in range(ans.count("+")):
		ans [ ( ans.index( "+" ) - 1 ) ] = float(ans[ ( ans.index( "+" ) - 1 ) ]) + float(ans[ ( ans.index( "+" ) + 1 ) ])
		ans.pop( ans.index( "+" ) + 1  )
		ans.pop( ans.index( "+" )  )
	for i in range(ans.count("-")):
		ans [ ( ans.index( "-" ) - 1 ) ] = float(ans[ ( ans.index( "-" ) - 1 ) ]) - float(ans[ ( ans.index( "-" ) + 1 ) ])
		ans.pop( ans.index( "-" ) + 1  )
		ans.pop( ans.index( "-" )  )	
	a.delete(0,END)
	a.insert(0,ans)
window = Tk()

a = Entry(window,width = 70 , borderwidth = 5)
a.grid(column = 0,row = 0, columnspan = 4 , padx = 10 , pady = 10)

window.title("Calculator")

#Defining Button

B1  = Button(window , text = "1" , padx = 40 , pady = 20, command = lambda : button_click("1"))
B2  = Button(window , text = "2" , padx = 40 , pady = 20, command = lambda : button_click("2"))
B3  = Button(window , text = "3" , padx = 40 , pady = 20, command = lambda : button_click("3"))
B4  = Button(window , text = "4" , padx = 40 , pady = 20, command = lambda : button_click("4"))
B5  = Button(window , text = "5" , padx = 40 , pady = 20, command = lambda : button_click("5"))
B6  = Button(window , text = "6" , padx = 40 , pady = 20, command = lambda : button_click("6"))
B7  = Button(window , text = "7" , padx = 40 , pady = 20, command = lambda : button_click("7"))
B8  = Button(window , text = "8" , padx = 40 , pady = 20, command = lambda : button_click("8"))
B9  = Button(window , text = "9" , padx = 40 , pady = 20, command = lambda : button_click("9"))
B0  = Button(window , text = "0" , padx = 40 , pady = 20, command = lambda : button_click("0"))
B11 = Button(window , text = "Clear" , padx = 40 , pady = 20 , command = lambda : clear())
B12 = Button(window , text = "+" , padx = 40 , pady = 20, command = lambda : button_click(" + "))
B13 = Button(window , text = "-" , padx = 40 , pady = 20, command = lambda : button_click(" - "))
B14 = Button(window , text = "/" , padx = 40 , pady = 20, command = lambda : button_click(" / "))
B15 = Button(window , text = "*" , padx = 40 , pady = 20, command = lambda : button_click(" * "))
B16 = Button(window , text = "=" , padx = 40 , pady = 20, command = lambda : equal())
B17 = Button(window , text = "sqrt(x)" , padx = 40 , pady = 20, command = lambda : button_click_1(" sqrt "))
B18 = Button(window , text = "x**y" , padx = 40 , pady = 20, command = lambda : button_click(" ** "))
B19 = Button(window , text = "1/x" , padx = 40 , pady = 20, command = lambda : button_click_1(" 1 / "))
B10 = Button(window , text = "." , padx = 40 , pady = 20, command = lambda : button_click("."))	

#Griding

B1.grid(row = 3, column = 0)
B2.grid(row = 3, column = 1)
B3.grid(row = 3, column = 2)

B4.grid(row = 2, column = 0)
B5.grid(row = 2, column = 1)
B6.grid(row = 2, column = 2)

B7.grid(row = 1, column = 0)
B8.grid(row = 1, column = 1)
B9.grid(row = 1, column = 2)

B0.grid(row = 4, column = 1)
B11.grid(row = 4, column = 0)
B12.grid(row = 1, column = 3)

B13.grid(row = 2, column = 3)
B14.grid(row = 3, column = 3)
B15.grid(row = 4, column = 3)
B16.grid(row = 4, column = 2)

B17.grid(row = 5, column = 0)
B18.grid(row = 5, column = 1)
B19.grid(row = 5, column = 2)
B10.grid(row = 5, column = 3)

window.mainloop()		