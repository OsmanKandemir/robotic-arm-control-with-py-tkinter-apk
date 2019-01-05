# -*- coding: utf-8 -*-
from Tkinter import *
import sys
import glob
import serial
import time
RightLeftCounter = 1
RightLeftCounter1 = 36
RightLeftCounter2 = 72
RightLeftCounter3 = 131
 
class App:

  
  def __init__(self, master, ser):
 	
    self.ser  = ser

    self.button = Button(master, 
                         text="QUIT", fg="red",
                         command=quit)
    self.button.grid(row=4, column=3, padx=0, pady=0, sticky="nw")

    self.slogan = Button(master,
                         text="Reset",
                         command=self.write_reset)
 
    self.slogan.grid(row=5, column=3, padx=0, pady=0, sticky="nw")
   
    self.label1 = Scale(master,from_=0,to=35,orient=HORIZONTAL,command=self.write_Left)
    self.label1.grid(row=0, column=6)

    self.label2 = Scale(master,from_=45,to=71,orient=HORIZONTAL,command=self.write_Left1)
    self.label2.grid(row=1, column=6)

    self.label3 = Scale(master,from_=85,to=130,orient=HORIZONTAL,command=self.write_Left2)
    self.label3.grid(row=2, column=6)

    self.label4 = Scale(master,from_=131,to=160,orient=HORIZONTAL,command=self.write_Left3)
    self.label4.grid(row=3, column=6)


    self.label1111 = Label(master, text="Sağ / Sol")
    self.label1111.grid(row=0, column=3)
    self.label11111 = Label(master, text="Aşağı / Yukarı")
    self.label11111.grid(row=1, column=3)
    self.label11111 = Label(master, text="İleri / Geri")
    self.label11111.grid(row=2, column=3)
    self.label11111 = Label(master, text="Tut / Bırak")
    self.label11111.grid(row=3, column=3)


  def write_Left(self,val):
    global RightLeftCounter
    RightLeftCounter = int(val)
    if (RightLeftCounter>0):
      RightLeftCounter -=1
    self.ser.write(chr(RightLeftCounter))
    print(RightLeftCounter)
    print self.ser.readline()
 

  def write_Left1(self,val):
    global RightLeftCounter1
    RightLeftCounter1 = int(val)
    if (RightLeftCounter1>36):
      RightLeftCounter1 -=1
    self.ser.write(chr(RightLeftCounter1))
    print(RightLeftCounter1)
    print self.ser.readline()
 

  def write_Left2(self,val):
    global RightLeftCounter2
    RightLeftCounter2 = int(val)
    if (RightLeftCounter2>72):
      RightLeftCounter2 -=1
    self.ser.write(chr(RightLeftCounter2))
    print(RightLeftCounter2)
    print self.ser.readline()
 
 


  def write_Left3(self,val):
    global RightLeftCounter3
    RightLeftCounter3 = int(val)
    if (RightLeftCounter3>131):
      RightLeftCounter3 -=1
    self.ser.write(chr(RightLeftCounter3))
    print(RightLeftCounter3)
    print self.ser.readline()

  def write_reset(self):
    global RightLeftCounter
    RightLeftCounter = 1
    print(RightLeftCounter)
    self.ser.write(chr(RightLeftCounter))
    print self.ser.readline()
 



def main():
  ser = serial.Serial()
  ser.port = '/dev/ttyACM1'
  ser.baudrate = 9600
  ser.timeout = 0
  # open port if not already open
  if ser.isOpen() == False:
    ser.open()
  root = Tk()
  root.title("RobotKol-GUI")
  root.geometry("230x400+500+300")

 

  app = App(root,ser)
  root.mainloop()
 
if __name__ == '__main__':
  main()
