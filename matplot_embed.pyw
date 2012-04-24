#! /usr/bin/env python3

import matplotlib
matplotlib.use('TkAgg')

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import sys
from tkinter import *

#application class
class runapp(Frame):
	''' gui for cts chamber (uses oven.exe as backend) '''
	
	def __init__(self,master=None):
		self.root = Tk()
		self.root.title('Embedding MATPLOTLIB in TK')
		Frame.__init__(self,master)
		self.createWidgets()
	
	def createWidgets(self):

		self.f = Figure(figsize=(5,4), dpi=100)
		self.a = self.f.add_subplot(111)
		self.t = arange(0.0,3.0,0.01)
		self.n = 1
		self.s = sin(pi*self.t*self.n)

		self.a.plot(self.t,self.s)
		self.a.set(xlabel='x')
		self.a.set(ylabel='y')

		# a tk.DrawingArea
		self.canvas = FigureCanvasTkAgg(self.f, master=self.root)
		self.canvas.show()
		self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

		'''self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.root)
		self.toolbar.update()
		self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)'''

		self.frmButtons = Frame(master=self.root)
		self.frmButtons.pack()
		self.buttonAdd = Button(master=self.frmButtons,text='Inc',command=self.fIncClick)
		self.buttonAdd.pack(side=LEFT)
		self.buttonSub = Button(master=self.frmButtons,text='Dec',command=self.fDecClick)
		self.buttonSub.pack(side=LEFT)

	def fIncClick(self):
		self.n += 1
		self.fRedraw()

	def fDecClick(self):
		if self.n>1:
			self.n -= 1
			self.fRedraw()

	def fRedraw(self):
		self.s = sin(pi*self.t*self.n)
		self.a.clear()
		self.a.plot(self.t,self.s)
		self.a.set(xlabel='x')
		self.a.set(ylabel='y')
		self.canvas.show()
			
	def _quit(self):
		print('kooonec')
		self.root.quit()     # stops mainloop
		self.root.destroy()  # this is necessary on Windows to prevent
					# Fatal Python Error: PyEval_RestoreThread: NULL tstate

app = runapp()
app.mainloop()
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.
