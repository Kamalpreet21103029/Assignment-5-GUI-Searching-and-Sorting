# Made by Kamalpreet Singh Bachhal
# SID 21103029 Branch CSE
#Done for Practise

# -----------------------Q1------------------------
print(">>>>>>>>>>>>>>>>>>>Q1<<<<<<<<<<<<<<<<<<<<<")


import tkinter
from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("GST Tax Calculator")
win.geometry("600x300")
def fun():
     p = int(en1.get())
     q = int(en2.get())
     r = (((int(q) - int(p)) * 100) / int(p))
     messagebox.showinfo("GST Tax", "The GST Tax calculated is equal to "+str(r))
lbl = Label(win, text="Enter Original Cost",fg="black",font=("Arial", 30))
lbl.place(x=10,y=10)
lbl1= Label(win, text="Enter Net Price",fg="black",font=("Arial", 30))
lbl1.place(x=10,y=60)
en1=Entry(win)
en1.place(x=400,y=30)
en2=Entry(win)
en2.place(x=400,y=80)
b1 =Button(win,text = "Calculate GST",command = fun,activeforeground = "red",activebackground ="pink",pady=10)
b1.place(x=10,y=200)
b2 =Button(win,text = "Close" ,activeforeground = "red",activebackground ="pink",pady=10,command=exit)
b2.place(x=100,y=200)
win.mainloop()


print("---------------------+++++++++++++++------------------------")

# -----------------------Q2------------------------
print(">>>>>>>>>>>>>>>>>>>Q2<<<<<<<<<<<<<<<<<<<<<")

from tkinter import *
import calendar
win=Tk()
win.geometry("100x135")
win.title("Calendar")
def showcal():
    a = int(year_field.get())
    print(calendar.calendar(a))
lbl1 = Label(win, text="Calendar")
year = Label(win, text="Enter Year")
year_field = Entry(win)
Show = Button(win, text="Show Calendar", fg="Black",bg="Red", command=showcal)
Exit = Button(win, text="Exit", fg="Black", bg="Red", command=exit)
lbl1.grid(row=1, column=1)
year.grid(row=2, column=1)
year_field.grid(row=3, column=1)
Show.grid(row=4, column=1)
Exit.grid(row=6, column=1)
win.mainloop()

print("---------------------+++++++++++++++------------------------")

# -----------------------Q3------------------------
print(">>>>>>>>>>>>>>>>>>>Q3<<<<<<<<<<<<<<<<<<<<<")

import tkinter
from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Calculator")
win.geometry("400x300")
def fun1():
    p = float(en1.get())
    q = float(en2.get())
    r=p+q
    messagebox.showinfo("Calculation is performed", "The Result obtained is equal to " + str(r))
def fun2():
    p = float(en1.get())
    q = float(en2.get())
    r=p-q
    messagebox.showinfo("Calculation is performed", "The Result obtained is equal to " + str(r))
def fun3():
    p = float(en1.get())
    q = float(en2.get())
    r=p*q
    messagebox.showinfo("Calculation is performed", "The Result obtained is equal to " + str(r))
def fun4():
    p = float(en1.get())
    q = float(en2.get())
    r=p/q
    messagebox.showinfo("Calculation is performed", "The Result obtained is equal to " + str(r))
lbl = Label(win, text="Enter Operand",fg="black",font=("Arial", 20))
lbl.place(x=10,y=10)
lbl1= Label(win, text="Enter Operator",fg="black",font=("Arial", 20))
lbl1.place(x=10,y=60)
lbl2= Label(win, text="Select the Operation-",fg="black",font=("Arial", 20))
lbl2.place(x=10,y=100)
en1=Entry(win)
en1.place(x=250,y=30)
en2=Entry(win)
en2.place(x=250,y=80)
b_add =Button(win,text = "+",command = fun1,activeforeground = "red",activebackground ="pink",pady=10)
b_add.place(x=10,y=200)
b_subtract =Button(win,text = "-",command = fun2,activeforeground = "red",activebackground ="pink",pady=10)
b_subtract .place(x=30,y=200)
b_multiply =Button(win,text = "*",command = fun3,activeforeground = "red",activebackground ="pink",pady=10)
b_multiply .place(x=50,y=200)
b_divide =Button(win,text = "/",command = fun4,activeforeground = "red",activebackground ="pink",pady=10)
b_divide.place(x=70,y=200)
b2 =Button(win,text = "Close" ,activeforeground = "red",activebackground ="pink",pady=10,command=exit)
b2.place(x=100,y=200)
win.mainloop()

print("---------------------+++++++++++++++------------------------")

# -----------------------Q4------------------------
print(">>>>>>>>>>>>>>>>>>>Q4<<<<<<<<<<<<<<<<<<<<<")

def qsort(marks):
    if len(marks) <= 1:
      return marks
    else:
      return qsort([x for x in marks[1:] if x < marks[0]]) + [marks[0]] + qsort([x for x in marks[1:] if x >= marks[0]])

if __name__ == "main_":

    marks = []

    # given is question that n is number of students
    n = int(input("Enter the number of students:"))

    for i in range(0, n):
        user_input = int(input("Enter the marks:"))
        marks.append(user_input)
    print(qsort(marks))


def b():
    c=int(input("Enter the Student Marks="))
    return c
def a():
    lst=[]
    count = 0
    while count<n:
        count=count+1
        p=b()
        lst.append(p)
    print(lst)
    return lst


e=[]
n=int(input("Enter the Number of Students="))
e=e+a()
print("Unsorted list=",e)
print("Sorted List=",qsort(e))

print("---------------------+++++++++++++++------------------------")

# -----------------------Q5------------------------
print(">>>>>>>>>>>>>>>>>>>Q5<<<<<<<<<<<<<<<<<<<<<")

n=int(input("Enter the Number of Elements User wants in Array="))
def b():
    c=int(input("Enter the Elements of the array="))
    return c
def a():
    lst=[]
    count = 0
    while count<n:
        count=count+1
        p=b()
        lst.append(p)
    print(lst)
    return lst
lst=a()
lst.sort()
print(lst)

x=int(input("Enter the Element you want to Search="))
low=0
high=len(lst)-1
mid=0

def binary_search(lst,low,high,y):
     if low<=high :
        mid=(high+low)//2
        if lst[mid]==y:
            return mid
        elif lst[mid]>y:
            return binary_search(lst,low,mid-1,y)
        else:
            return binary_search(lst,mid+1,high,y)
     else:
         print("Error:The Element we are searching for is not in the List")

def search(lst):
      count=0
      Occurence=0
      global x
      for count in range(n):
          if lst[count]==x:
              Occurence=Occurence+1
      return Occurence
r=search(lst)
str="The number of Occurences of %d in the list is=%d"%(x,r)
print(str)


