# -*- coding: utf-8 -*-
from Tkinter import *
import sys
import glob
import serial
import time
RightLeftCounter = 1
RightLeftCounter1 = 36
RightLeftCounter2 = 72
 
class App:
  def __init__(self, master, ser):
 	
    self.ser  = ser
    self.label = Label(master, text="Sağ / Sol")
    self.label.grid(row=0, column=9)

    self.button = Button(master, 
                         text="QUIT", fg="red",
                         command=quit)
    self.button.grid(row=0, column=0, padx=0, pady=0, sticky="nw")

    self.slogan = Button(master,
                         text="Reset",
                         command=self.write_reset)
 
    self.slogan.grid(row=0, column=4, padx=0, pady=0, sticky="nw")
 
    self.Left = Button(master,
                         text="←",padx=10,
                         command=self.write_Left)
    self.Left.grid(row=0, column=1, padx=0, pady=0, sticky="nw")
 
    self.Right = Button(master,
                         text="→",padx=10,
                         command=self.write_Right)
    self.Right.grid(row=0, column=6, padx=2, pady=0, sticky="nw")
    self.sweep = Button(master,
                         text="Test",
                         command=self.write_sweep)
    self.sweep.grid(row=0, column=8, padx=0, pady=0, sticky="nw")

    #self.label1 = Scale(master,from_=0,to=180,orient=HORIZONTAL,length = 200,command=self.write_Left1)
    #self.label1.grid(row=0, column=9)
 

    print("---------------------------------------------------------------------")

    self.label11 = Label(master, text="İleri / Geri")
    self.label11.grid(row=1, column=9)

    self.slogan1 = Button(master,
                         text="Reset",
                         command=self.write_reset)
 
    self.slogan1.grid(row=1, column=4, padx=0, pady=0, sticky="nw")
 
    self.Left1 = Button(master,
                         text="↑",padx=10,
                         command=self.write_Left1)
    self.Left1.grid(row=1, column=1, padx=0, pady=0, sticky="nw")
 
    self.Right1 = Button(master,
                         text="↓",padx=10,
                         command=self.write_Right1)
    self.Right1.grid(row=1, column=6, padx=2, pady=0, sticky="nw")
  


    print("---------------------------------------------------------------------")

    self.label111 = Label(master, text="Yukarı / Aşağı")
    self.label111.grid(row=2, column=9)

    self.slogan11 = Button(master,
                         text="Reset",
                         command=self.write_reset)
 
    self.slogan11.grid(row=2, column=4, padx=0, pady=0, sticky="nw")
 
    self.Left11 = Button(master,
                         text="▼",padx=10,
                         command=self.write_Left2)
    self.Left11.grid(row=2, column=1, padx=0, pady=0, sticky="nw")
 
    self.Right11 = Button(master,
                         text="▲",padx=10,
                         command=self.write_Right2)
    self.Right11.grid(row=2, column=6, padx=2, pady=0, sticky="nw")

    print("---------------------------------------------------------------------")

    self.label111 = Label(master, text="Tut / Bırak")
    self.label111.grid(row=3, column=9)

    self.slogan11 = Button(master,
                         text="Reset",
                         command=self.write_reset)
 
    self.slogan11.grid(row=3, column=4, padx=0, pady=0, sticky="nw")
 
    self.Left11 = Button(master,
                         text="↑",padx=10,
                         command=self.write_Left)
    self.Left11.grid(row=3, column=1, padx=0, pady=0, sticky="nw")
 
    self.Right11 = Button(master,
                         text="↓",padx=10,
                         command=self.write_Right)
    self.Right11.grid(row=3, column=6, padx=2, pady=0, sticky="nw")


  def write_Left(self):
    global RightLeftCounter
    if (RightLeftCounter>0):
      RightLeftCounter -=1
    self.ser.write(chr(RightLeftCounter))
    print(RightLeftCounter)
    print self.ser.readline()
 
  def write_Right(self):
    global RightLeftCounter
    if (RightLeftCounter<35):
      RightLeftCounter +=1
    self.ser.write(chr(RightLeftCounter))
    print(RightLeftCounter)
    print self.ser.readline()

  def write_Left1(self):
    global RightLeftCounter1
    if (RightLeftCounter1>36):
      RightLeftCounter1 -=1
    self.ser.write(chr(RightLeftCounter1))
    print(RightLeftCounter1)
    print self.ser.readline()
 
  def write_Right1(self):
    global RightLeftCounter1
    if (RightLeftCounter1<71):
      RightLeftCounter1 +=1
    self.ser.write(chr(RightLeftCounter1))
    print(RightLeftCounter1)
    print self.ser.readline()

  def write_Left2(self):
    global RightLeftCounter2
    if (RightLeftCounter2>72):
      RightLeftCounter2 -=1
    self.ser.write(chr(RightLeftCounter2))
    print(RightLeftCounter2)
    print self.ser.readline()
 
  def write_Right2(self):
    global RightLeftCounter2
    if (RightLeftCounter2<150):
      RightLeftCounter2 +=1
    self.ser.write(chr(RightLeftCounter2))
    print(RightLeftCounter2)
    print self.ser.readline()


  def write_reset(self):
    global RightLeftCounter
    RightLeftCounter = 1
    print(RightLeftCounter)
    self.ser.write(chr(RightLeftCounter))
    print self.ser.readline()
 
  def write_sweep(self):
    global RightLeftCounter
    for RightLeftCounter in range(0,180):
      print(RightLeftCounter)
      self.ser.write(chr(RightLeftCounter))
      print self.ser.readline()
      time.sleep(0.01)
    RightLeftCounter = 90
    self.ser.write(chr(RightLeftCounter))

def main():
  ser = serial.Serial()
  ser.port = '/dev/ttyACM0'
  ser.baudrate = 9600
  ser.timeout = 0
  # open port if not already open
  if ser.isOpen() == False:
    ser.open()
  root = Tk()
  root.title("RobotKol-GUI")
  root.geometry("400x300+500+300")
  app = App(root,ser)
  root.mainloop()
 
if __name__ == '__main__':
  main()