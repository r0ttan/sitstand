import tkinter as tk
from time import clock
#import matplotlib.pyplot as plt

class Application(tk.Frame):
    def __init__(self, master=None):
        self.pos = 1 #start sitting, increment timerd
        self.onoff = 0 #start off
        self.totalt = 0 #total time app been on
        self.allday = 21600 #6h = 21600s
        self.timeru = 0 #time standing
        self.timerd = 0 #time sitting

        self.timerudig = tk.StringVar() #for dynamic change of tk.labels
        self.timerddig = tk.StringVar()
        self.timerustr = tk.StringVar()
        self.timerdstr = tk.StringVar()

        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        """Make stuff visible on root and canvas"""
        self.start_b = tk.Button(root, text="On/Off", command=self.onofftoggle)
        self.toggle_b = tk.Button(root, text="Sit/Stand", command=self.togglepos)
        self.start_b.pack(expand=1, fill=tk.BOTH, side=tk.BOTTOM)
        self.toggle_b.pack(expand=1,fill=tk.BOTH, side=tk.TOP)
        
        self.dtlbl = tk.Label(root, bg="#000fff000", text="Sit")
        self.utlbl = tk.Label(root, text="Stand")

        self.uframe = tk.Frame(root)
        self.dframe = tk.Frame(root)
        self.dtick = tk.Label(self.dframe, textvariable=self.timerdstr)
        self.utick = tk.Label(self.uframe, textvariable=self.timerustr)
        self.ddig = tk.Label(self.dframe, textvariable=self.timerddig)
        self.udig = tk.Label(self.uframe, textvariable=self.timerudig)

        self.linecanv = tk.Canvas(root, height=60, width=120, bg="#b00b00b00")
        self.linecanv.pack(expand=1, fill=tk.X)
        self.cw = int(self.linecanv.cget("width"))
        self.ch = int(self.linecanv.cget("height"))
        self.uline = self.linecanv.create_line(0, self.ch/2, self.cw/2, self.ch/2, width=24, fill="#100400c00", tags="uline")
        self.dline = self.linecanv.create_line(self.cw/2, self.ch/2, self.cw, self.ch/2, width=24, fill="#100c00400", tags="dline")
        self.ux2 = self.cw/2
        self.utlbl.pack()
        self.uframe.pack()
        self.utick.pack(side=tk.LEFT)
        self.udig.pack(side=tk.RIGHT)
        self.dtlbl.pack()
        self.dframe.pack()
        self.dtick.pack(side=tk.LEFT)
        self.ddig.pack(side=tk.RIGHT)

        self.uline = tk.NONE

        self.ticker()
        
    def onofftoggle(self):
        """Called from on/off button"""
        self.onoff = 1 if self.onoff == 0 else 0
        if self.onoff == 1:
            self.start_b.configure(bg="#000fff000")
        else:
            self.start_b.configure(bg="#f00f00f00")
        
    def togglepos(self):
        """called from Stand/Sit button"""
        self.pos = 1 if self.pos == 0 else 0
        if self.pos == 1:
            self.dtlbl.config(bg="#000fff000")
            self.utlbl.config(bg="#f00f00f00")
        else:
            self.utlbl.config(bg="#000fff000")
            self.dtlbl.config(bg="#f00f00f00")
        #print("Pos: ", self.pos)

    def ticker(self):
        if self.onoff == 1:
            self.totalt += 1
            if self.pos == 1:
                self.timerd += 1
            else:
                self.timeru += 1
            self.dprocent = self.timerd/self.totalt
            self.uprocent = self.timeru/self.totalt
            self.timerdstr.set(int(self.timerd/self.totalt*100))
            self.timerddig.set(round(self.timerd/self.allday*100, 2))
            ux1=0
            uy1=self.ch/2
            ux2=self.cw*self.uprocent
            self.ux2 -=3
            ulinecoord = (int(ux1), int(uy1), int(ux2), int(uy1))
            dx1=self.cw-(self.cw*self.dprocent)
            dy1=self.ch/2
            dx2=self.cw
            dlinecoord = (int(dx1), int(dy1), int(dx2), int(dy1))
            self.linecanv.coords("uline", ulinecoord)
            self.linecanv.coords("dline", dlinecoord)
            self.timerustr.set(int(self.timeru/self.totalt*100))
            self.timerudig.set(round(self.timeru/self.allday*100, 2))
            print(ulinecoord, dlinecoord)
        self._tick = self.after(1000, self.ticker)#call itself every 1s


root = tk.Tk()
app = Application(master=root)
app.mainloop()
