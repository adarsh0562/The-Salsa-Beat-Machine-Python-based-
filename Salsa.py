

import sys
from tkhtmlview import HTMLLabel
import pygame
from ttkthemes import themed_tk as tk
import threading
from mutagen.mp3 import MP3
from pygame import mixer
import time
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Salsa_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    Salsa_support.set_Tk_var()
    top = Toplevel1 (root)
    Salsa_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    Salsa_support.set_Tk_var()
    top = Toplevel1 (w)
    Salsa_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Schadow BT} -size 14"
        font12 = "-family {Schadow BT} -size 16"
        font14 = "-family {MV Boli} -size 16 -weight bold"
        font15 = "-family {Arial} -size 14 -underline 1"
        self.font16 = "-family {News706 BT} -size 13 -weight bold"
        font9 = "-family {News706 BT} -size 12 -weight bold"
        self.style = ttk.Style()
        self.style1 = ttk.Style()
        self.style1.configure("TScale", background="white")

        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        #top.geometry("1164x693+107+0")
        top.minsize(1164, 693)
        top.maxsize(1164, 693)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#970097")
        pygame.mixer.init(44100)

        #self.BPM()

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.172, rely=0.058, relheight=0.206
                , relwidth=0.674)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="white")

        self.playphoto = tk.PhotoImage(file='icon/play.png')
        self.stopphoto = tk.PhotoImage(file='icon/dot.png')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.025, rely=0.14, height=44, width=40)
        self.Button1.configure(activebackground="white")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(background="white")
        self.Button1.configure(disabledforeground="grey")
        self.Button1.configure(foreground="white")
        self.Button1.configure(highlightbackground="white")
        self.Button1.configure(highlightcolor="white")
        self.Button1.configure(image=self.playphoto)
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="flat")
        self.Button1.configure(text='''Button''',command=self.start_Salsa)

        self.TScale1 = ttk.Scale(self.Frame1, from_=0, to=100)
        self.TScale1.place(relx=0.102, rely=0.14, relwidth=0.256, relheight=0.0
                , height=38, bordermode='ignore')
        self.TScale1.configure(takefocus="")
        self.style.configure('.', background="white")
        self.TScale1.set(70)

        self.Checkbutton1 = tk.Checkbutton(self.Frame1)
        self.Checkbutton1.place(relx=0.815, rely=0.098, relheight=0.51
                , relwidth=0.153)
        self.Checkbutton1.configure(activebackground="white")
        self.Checkbutton1.configure(activeforeground="black")
        self.Checkbutton1.configure(background="white")
        self.Checkbutton1.configure(disabledforeground="white")
        self.Checkbutton1.configure(font=font9)
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="white")
        self.Checkbutton1.configure(highlightcolor="white")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''Merengue''',command=self.playsalsa)
        self.var = 1
        self.Checkbutton1.configure(variable=self.var)

        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.369, rely=0.112, height=42, width=29)
        self.TLabel1.configure(background="white")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font=font12)
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''80''')

        self.TLabel2 = ttk.Label(self.Frame1)
        self.TLabel2.place(relx=0.408, rely=0.112, height=42, width=40)
        self.TLabel2.configure(background="white")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font=font11)
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''BPM''')

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.172, rely=0.286, relheight=0.496, relwidth=0.674)
        self.Frame2.configure(relief='sunken')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="sunken")
        self.Frame2.configure(background="white")

        self.claveOri = tk.PhotoImage(file="icon/clave (1).png")
        self.claveBlk = tk.PhotoImage(file="icon/clave (2).png")
        self.cowbellOri = tk.PhotoImage(file="icon/cowbell.png")
        self.cowbellBlk = tk.PhotoImage(file="icon/cowbell (1).png")
        self.congasOri = tk.PhotoImage(file="icon/conga.png")
        self.congasBlk = tk.PhotoImage(file="icon/conga (1).png")
        self.drumOri = tk.PhotoImage(file="icon/drum.png")
        self.drumBlk = tk.PhotoImage(file="icon/drum (1).png")
        self.pianoOri = tk.PhotoImage(file="icon/piano.png")
        self.pianoBlk = tk.PhotoImage(file="icon/piano (2).png")
        self.bongosOri = tk.PhotoImage(file="icon/bongos.png")
        self.bongosBlk = tk.PhotoImage(file="icon/bongos (2).png")
        self.guiroOri = tk.PhotoImage(file="icon/guiro.png")
        self.guiroBlk = tk.PhotoImage(file="icon/guiro (3).png")
        self.maracasOri = tk.PhotoImage(file="icon/maracas.png")
        self.maracasBlk = tk.PhotoImage(file="icon/maracas (2).png")

        self.Button2 = tk.Button(self.Frame2)
        self.Button2.place(relx=0.025, rely=0.055, height=94, width=80)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="white")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")

        self.Button2.configure(pady="0")
        self.Button2.configure(relief="flat")
        self.Button2.configure(text='''Button''',command=self.threadmusic1)

        self.Button3 = tk.Button(self.Frame2)
        self.Button3.place(relx=0.245, rely=0.055, height=94, width=77)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="white")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")

        self.Button3.configure(pady="0")
        self.Button3.configure(relief="flat")
        self.Button3.configure(text='''Button''',command=self.threadmusic2)

        self.Button4 = tk.Button(self.Frame2)
        self.Button4.place(relx=0.424, rely=0.087, height=84, width=70)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="white")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")

        self.Button4.configure(pady="0")
        self.Button4.configure(relief="flat")
        self.Button4.configure(text='''Button''',command=self.threadmusic3)

        self.Button5 = tk.Button(self.Frame2)
        self.Button5.place(relx=0.631, rely=0.055, height=94, width=77)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="white")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")

        self.Button5.configure(pady="0")
        self.Button5.configure(relief="flat")
        self.Button5.configure(text='''Button''',command=self.threadmusic4)

        self.Button5_5 = tk.Button(self.Frame2)
        #self.Button5_5.place(relx=0.245, rely=0.573, height=94, width=77)
        self.Button5_5.place(relx=0.823, rely=0.055, height=94, width=77)

        self.Button5_5.configure(activebackground="#ececec")
        self.Button5_5.configure(activeforeground="#000000")
        self.Button5_5.configure(background="white")
        self.Button5_5.configure(disabledforeground="#a3a3a3")
        self.Button5_5.configure(foreground="#000000")
        self.Button5_5.configure(highlightbackground="#d9d9d9")
        self.Button5_5.configure(highlightcolor="black")

        self.Button5_5.configure(pady="0")
        self.Button5_5.configure(relief="flat")
        self.Button5_5.configure(text='''Button''',command=self.threadmusic7)

        self.Button5_7 = tk.Button(self.Frame2)
        self.Button5_7.place(relx=0.180, rely=0.573, height=94, width=77)
        self.Button5_7.configure(activebackground="#ececec")
        self.Button5_7.configure(activeforeground="#000000")
        self.Button5_7.configure(background="white")
        self.Button5_7.configure(disabledforeground="#a3a3a3")
        self.Button5_7.configure(foreground="#000000")
        self.Button5_7.configure(highlightbackground="#d9d9d9")
        self.Button5_7.configure(highlightcolor="black")

        self.Button5_7.configure(pady="0")
        self.Button5_7.configure(relief="flat")
        self.Button5_7.configure(text='''Button''',command=self.threadmusic8)

        self.Button5_8 = tk.Button(self.Frame2)
        self.Button5_8.place(relx=0.400, rely=0.581, height=94, width=77)
        self.Button5_8.configure(activebackground="#ececec")
        self.Button5_8.configure(activeforeground="#000000")
        self.Button5_8.configure(background="white")
        self.Button5_8.configure(disabledforeground="#a3a3a3")
        self.Button5_8.configure(foreground="#000000")
        self.Button5_8.configure(highlightbackground="#d9d9d9")
        self.Button5_8.configure(highlightcolor="black")

        self.Button5_8.configure(pady="0")
        self.Button5_8.configure(relief="flat")
        self.Button5_8.configure(text='''Button''',command=self.threadmusic9)

        self.Button5_9 = tk.Button(self.Frame2)
        self.Button5_9.place(relx=0.623, rely=0.573, height=94, width=77)
        self.Button5_9.configure(activebackground="#ececec")
        self.Button5_9.configure(activeforeground="#000000")
        self.Button5_9.configure(background="white")
        self.Button5_9.configure(disabledforeground="#a3a3a3")
        self.Button5_9.configure(foreground="#000000")
        self.Button5_9.configure(highlightbackground="#d9d9d9")
        self.Button5_9.configure(highlightcolor="black")

        self.Button5_9.configure(pady="0")
        self.Button5_9.configure(relief="flat")
        self.Button5_9.configure(text='''Button''',command=self.threadmusic10)

        self.Button7 = tk.Button(self.Frame2)
        self.Button7.place(relx=0.154, rely=0.192, height=24, width=30)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="white")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"icon/speaker (1).png")
        global _img20
        _img20 = tk.PhotoImage(file=photo_location)
        self.Button7.configure(image=_img20)
        self.Button7.configure(pady="0")
        self.Button7.configure(relief="flat")
        self.Button7.configure(text='''Button''',command=self.clave_Volume)

        self.Button5_19 = tk.Button(self.Frame2)
        self.Button5_19.place(relx=0.346, rely=0.192, height=24, width=30)
        self.Button5_19.configure(activebackground="#ececec")
        self.Button5_19.configure(activeforeground="#000000")
        self.Button5_19.configure(background="white")
        self.Button5_19.configure(disabledforeground="#a3a3a3")
        self.Button5_19.configure(foreground="#000000")
        self.Button5_19.configure(highlightbackground="#d9d9d9")
        self.Button5_19.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"icon/speaker (1).png")
        global _img30
        _img30 = tk.PhotoImage(file=photo_location)
        self.Button5_19.configure(image=_img30)
        self.Button5_19.configure(pady="0")
        self.Button5_19.configure(relief="flat")
        self.Button5_19.configure(text='''Button''',command=self.cowbell_Volume)

        self.Button5_20 = tk.Button(self.Frame2)
        self.Button5_20.place(relx=0.54, rely=0.192, height=24, width=30)
        self.Button5_20.configure(activebackground="#ececec")
        self.Button5_20.configure(activeforeground="#000000")
        self.Button5_20.configure(background="white")
        self.Button5_20.configure(disabledforeground="#a3a3a3")
        self.Button5_20.configure(foreground="#000000")
        self.Button5_20.configure(highlightbackground="#d9d9d9")
        self.Button5_20.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"icon/speaker (1).png")
        global _img31
        _img31 = tk.PhotoImage(file=photo_location)
        self.Button5_20.configure(image=_img31)
        self.Button5_20.configure(pady="0")
        self.Button5_20.configure(relief="flat")
        self.Button5_20.configure(text='''Button''',command=self.congas_Volume)

        self.Button5_21 = tk.Button(self.Frame2)
        self.Button5_21.place(relx=0.746, rely=0.192, height=24, width=30)
        self.Button5_21.configure(activebackground="#ececec")
        self.Button5_21.configure(activeforeground="#000000")
        self.Button5_21.configure(background="white")
        self.Button5_21.configure(disabledforeground="#a3a3a3")
        self.Button5_21.configure(foreground="#000000")
        self.Button5_21.configure(highlightbackground="#d9d9d9")
        self.Button5_21.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"icon/speaker (1).png")
        global _img32
        _img32 = tk.PhotoImage(file=photo_location)
        self.Button5_21.configure(image=_img32)
        self.Button5_21.configure(pady="0")
        self.Button5_21.configure(relief="flat")
        self.Button5_21.configure(text='''Button''',command=self.piano_Volume)

        self.Button5_24 = tk.Button(self.Frame2)
        self.Button5_24.place(relx=0.938, rely=0.192, height=24, width=30)

        self.Button5_24.configure(activebackground="#ececec")
        self.Button5_24.configure(activeforeground="#000000")
        self.Button5_24.configure(background="white")
        self.Button5_24.configure(disabledforeground="#a3a3a3")
        self.Button5_24.configure(foreground="#000000")
        self.Button5_24.configure(highlightbackground="#d9d9d9")
        self.Button5_24.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"icon/speaker (1).png")
        global _img35
        _img35 = tk.PhotoImage(file=photo_location)
        self.Button5_24.configure(image=_img35)
        self.Button5_24.configure(pady="0")
        self.Button5_24.configure(relief="flat")
        self.Button5_24.configure(text='''Button''',command=self.timbales_Volume)

        self.Button5_25 = tk.Button(self.Frame2)
        self.Button5_25.place(relx=0.280, rely=0.709, height=24, width=50)
        self.Button5_25.configure(activebackground="#ececec")
        self.Button5_25.configure(activeforeground="#000000")
        self.Button5_25.configure(background="white")
        self.Button5_25.configure(disabledforeground="#a3a3a3")
        self.Button5_25.configure(foreground="#000000")
        self.Button5_25.configure(highlightbackground="#d9d9d9")
        self.Button5_25.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"icon/speaker (1).png")
        global _img36
        _img36 = tk.PhotoImage(file=photo_location)
        self.Button5_25.configure(image=_img36)
        self.Button5_25.configure(pady="0")
        self.Button5_25.configure(relief="flat")
        self.Button5_25.configure(text='''Button''',command=self.guiro_Volume)

        self.Button5_26 = tk.Button(self.Frame2)
        self.Button5_26.place(relx=0.540, rely=0.709, height=24, width=30)
        self.Button5_26.configure(activebackground="#ececec")
        self.Button5_26.configure(activeforeground="#000000")
        self.Button5_26.configure(background="white")
        self.Button5_26.configure(disabledforeground="#a3a3a3")
        self.Button5_26.configure(foreground="#000000")
        self.Button5_26.configure(highlightbackground="#d9d9d9")
        self.Button5_26.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"icon/speaker (1).png")
        global _img37
        _img37 = tk.PhotoImage(file=photo_location)
        self.Button5_26.configure(image=_img37)
        self.Button5_26.configure(pady="0")
        self.Button5_26.configure(relief="flat")
        self.Button5_26.configure(text='''Button''',command=self.bongos_Volume)

        self.Button5_27 = tk.Button(self.Frame2)
        self.Button5_27.place(relx=0.758, rely=0.709, height=24, width=30)
        self.Button5_27.configure(activebackground="#ececec")
        self.Button5_27.configure(activeforeground="#000000")
        self.Button5_27.configure(background="white")
        self.Button5_27.configure(disabledforeground="#a3a3a3")
        self.Button5_27.configure(foreground="#000000")
        self.Button5_27.configure(highlightbackground="#d9d9d9")
        self.Button5_27.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"icon/speaker (1).png")
        global _img38
        _img38 = tk.PhotoImage(file=photo_location)
        self.Button5_27.configure(image=_img38)
        self.Button5_27.configure(pady="0")
        self.Button5_27.configure(relief="flat")
        self.Button5_27.configure(text='''Button''',command=self.maracas_Volume)


        self.Frame3 = tk.Frame(top)
        self.Frame3.place(relx=0.172, rely=0.81, relheight=0.185, relwidth=0.674)

        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="white")

        self.TLabel6 = ttk.Label(self.Frame3)
        self.TLabel6.place(relx=0.637, rely=0.102, height=111, width=514)
        self.TLabel6.configure(background="white")
        self.TLabel6.configure(foreground="#000000")
        self.TLabel6.configure(font="TkDefaultFont")
        self.TLabel6.configure(relief="flat")
        self.TLabel6.configure(anchor='w')
        self.TLabel6.configure(justify='left')
        self.TLabel6.configure(text='''Tlabel''')
        photo_location = os.path.join(prog_location,"icon/visual-salsa.png")
        global _img39
        _img39 = tk.PhotoImage(file=photo_location)
        self.TLabel6.configure(image=_img39)

        self.TLabel7 = ttk.Label(self.Frame3)
        self.TLabel7.place(relx=0.013, rely=0.102, height=49, width=491)
        self.TLabel7.configure(background="white")
        self.TLabel7.configure(foreground="#000000")
        self.TLabel7.configure(font=font14)
        self.TLabel7.configure(relief="flat")
        self.TLabel7.configure(anchor='w')
        self.TLabel7.configure(justify='left')
        self.TLabel7.configure(text='''Need help finding the beat in salsa music?''')

        self.TLabel8 = HTMLLabel(self.Frame3,html='<a href="https://salsabeatmachine.org/"> <p style="background-color: white;font-size:15px; width: 100%;"> Try our Web Application! </p></a>')
        self.TLabel8.place(relx=0.038, rely=0.492, height=37, width=356)
        self.TLabel8.configure(background="white")
        self.TLabel8.configure(foreground="blue")
        self.TLabel8.configure(font=font15)
        self.TLabel8.configure(relief="flat")
        #self.TLabel8.configure(anchor='w')
        #self.TLabel8.configure(justify='left')
        #self.TLabel8.configure(text='''Try our new app!''')
        self.clave = 1
        self.cowbell = 1
        self.congas = 1
        self.piano = 1
        self.mic = 1
        self.guitar = 1
        self.timbales = 1
        self.guiro = 1
        self.drum = 1
        self.maracas = 1
        self.start = 1
        self.val = 0
        self.val1 = 0
        self.a = 1
        self.b = 1
        self.c = 1
        self.d = 1
        self.e = 1
        self.f = 1
        self.g = 1
        self.h = 1
        self.vol1 = 1
        self.vol2 = 1
        self.vol3 = 1
        self.vol4 = 1
        self.vol5 = 1
        self.vol6 = 1
        self.vol7 = 1
        self.vol8 = 1

        self.pos_list = [0.300, 0.360, 0.420, 0.480, 0.540, 0.600, 0.660, 0.720]
        self.gear_x_positionx = [0.154, 0.343, 0.54, 0.746, 0.938]
        self.gear_x_positionx1 = [0.289, 0.536, 0.758]
        #self.gear_y_positionx = [ 0.602, 0.602, 0.602]
        self.gearphoto = tk.PhotoImage(file="icon/gear.png")

        self.photo_location = tk.PhotoImage(file="icon/dot.png")
        self.reddotphoto = tk.PhotoImage(file="icon/circle.png").subsample(24, 24)

        #self.stateDisabled()
        self.intital_postion()
        self.gearPosition()
        self.defaultphoto()
        self.clave_text()
        self.cowbell_text()
        self.congas_text()
        self.piano_text()
        self.timbales_text()
        self.guiro_text()
        self.bongos_text()
        self.maracas_text()

        #self.box.insert("a", "b")

        self.vol10 = 70
    def start_Salsa(self):
        if self.start == 1:
            self.pauseMusic()
            #self.stateEnabled()
            self.Button1["image"] = self.stopphoto
            self.Button1.configure(image=self.stopphoto)
            self.pos_set2()
            self.start = 0
            #self.playsalsa()
        else:
            #self.stateDisabled()
            self.Button1["image"] = self.playphoto
            self.Button1.configure(image=self.playphoto)
            self.start = 1
            self.val = 1
            self.stopMusic()
            #self.defaultphoto()

    def commanPos(self,x):
        self.TLabel9 = ttk.Label(self.Frame1)
        self.TLabel9.place(relx=x, rely=0.664, height=28, width=37)
        self.TLabel9.configure(background="white")
        self.TLabel9.configure(foreground="#000000")
        self.TLabel9.configure(font="TkDefaultFont")
        self.TLabel9.configure(relief="flat")
        self.TLabel9.configure(anchor='w')
        self.TLabel9.configure(justify='left')
        self.TLabel9.configure(text='''Tlabel''')

    def intital_postion(self):
        for x in self.pos_list:
            self.commanPos(x)

            self.TLabel9.configure(image=self.photo_location)

    def position(self):
        for x in self.pos_list:
            if self.val == 1:
                self.val = 0
                self.val1 = 1
                break
            else:
                time.sleep(0.5)
                self.commanPos(x)
                self.TLabel9.configure(image=self.reddotphoto)
                self.pos_set()
        if self.val1 == 0:
            self.position()

    def blackpos(self):
        for x in self.pos_list:
            time.sleep(0.6)
            self.commanPos(x)
            self.TLabel9.configure(image=self.photo_location)

    def pos_set(self):
        t2 = threading.Thread(target=self.blackpos,daemon=True)
        t2.start()

    def pos_set2(self):
        t1 = threading.Thread(target=self.position,daemon=True)
        t1.start()
    # pos2()
    def gearPosition(self):
        for x in self.gear_x_positionx:
            self.Button5_15 = tk.OptionMenu(self.Frame2,"one", "two", "three")
            self.Button5_15.place(relx=x, rely=0.081, height=24, width=30)
            self.gearPositionCommancode()
        for x in self.gear_x_positionx1:
            self.Button5_15 = tk.OptionMenu(self.Frame2,"one", "two", "three")
            self.Button5_15.place(relx=x, rely=0.602, height=24, width=30)
            self.gearPositionCommancode()


    def gearPositionCommancode(self):
        self.Button5_15.configure(activebackground="white")
        self.Button5_15.configure(activeforeground="white")
        self.Button5_15.configure(background="white")
        self.Button5_15.configure(disabledforeground="white")
        self.Button5_15.configure(foreground="white")
        self.Button5_15.configure(highlightbackground="white")
        self.Button5_15.configure(highlightcolor="white")
        self.Button5_15.configure(compound='right', indicatoron=0)
        self.Button5_15.configure(image=self.gearphoto)
        self.Button5_15.configure(pady="0")
        self.Button5_15.configure(relief="flat")

    def threadmusic1(self):
        t = threading.Thread(target=self.callingthread1)
        t.start()

    def threadmusic2(self):
        t = threading.Thread(target=self.callingthread2)
        t.start()
    
    def threadmusic3(self):
        t = threading.Thread(target=self.callingthread3)
        t.start()
    
    def threadmusic4(self):
        t = threading.Thread(target=self.callingthread4)
        t.start()
    
    """def threadmusic5(self):
        t = threading.Thread(target=self.callingthread5)
        t.start()

    def threadmusic6(self):
        t = threading.Thread(target=self.callingthread6)
        t.start()"""

    def threadmusic7(self):
        t = threading.Thread(target=self.callingthread7,args=())
        t.start()

    def threadmusic8(self):
        t = threading.Thread(target=self.callingthread8)
        t.start()

    def threadmusic9(self):
        t = threading.Thread(target=self.callingthread9)
        t.start()
    
    def threadmusic10(self):
        t = threading.Thread(target=self.callingthread10)
        t.start()

    def callingthread1(self):
        if self.start == 0:
            if self.clave == 1:
                self.playClave()
                self.a = 0
            else:
                print("stop")
                self.Button2.configure(image=self.claveBlk)

                pygame.mixer.Channel(0).stop()
                self.clave = 1
                self.a = 1
        else:
            if self.a == 1:
                self.Button2.configure(image=self.claveOri)
                self.clave = 0
                self.a = 0
            else:
                self.Button2.configure(image=self.claveBlk)
                self.clave = 1
                self.a = 1

    def playClave(self):
        self.cla = pygame.mixer.Channel(0)
        self.cla.play(pygame.mixer.Sound('Songs/clave (1).wav'),-1)
        self.cla.set_volume(0.5)
        self.Button2.configure(image=self.claveOri)
        self.clave = 0


    def callingthread2(self):
        if self.start == 0:
            if self.cowbell == 1:
                self.playCowbell()
                self.b = 0
            else:
                print("stop")
                self.Button3.configure(image=self.cowbellBlk)

                pygame.mixer.Channel(1).stop()
                self.cowbell = 1
                self.b = 1
        else:
            if self.b == 1:
                self.Button3.configure(image=self.cowbellOri)
                self.cowbell = 0
                self.b = 0
            else:
                self.Button3.configure(image=self.cowbellBlk)
                self.cowbell = 1
                self.b = 1

    def playCowbell(self):
        self.cow = pygame.mixer.Channel(1)
        self.cow.play(pygame.mixer.Sound('Songs/Cowbell.wav'),-1)
        self.cow.set_volume(0.5)
        self.cowbell = 0
        self.Button3.configure(image=self.cowbellOri)

    def callingthread3(self):
        if self.start == 0:
            if self.congas == 1:
                self.playCongas()
                self.c = 0
            else:
                print("stop")
                self.Button4.configure(image=self.congasBlk)

                pygame.mixer.Channel(2).stop()
                self.congas = 1
                self.c = 1
        else:
            if self.c == 1:
                self.Button4.configure(image=self.congasOri)
                self.congas = 0
                self.c = 0
            else:
                self.Button4.configure(image=self.congasBlk)
                self.congas = 1
                self.c = 1

    def playCongas(self):
        self.con = pygame.mixer.Channel(2)
        self.con.play(pygame.mixer.Sound('Songs/congas.wav'),-1)
        self.con.set_volume(0.5)
        self.congas = 0
        self.Button4.configure(image=self.congasOri)

    def callingthread4(self):
        if self.start == 0:
            if self.piano == 1:
                self.playPiano()
                self.d = 0
            else:
                print("stop")
                self.Button5.configure(image=self.pianoBlk)

                #pygame.mixer.Channel(0).stop()
                pygame.mixer.Channel(3).stop()
                self.piano = 1
                self.d = 1
        else:
            if self.d == 1:
                self.Button5.configure(image=self.pianoOri)
                self.piano = 0
                self.d = 0
            else:
                self.Button5.configure(image=self.pianoBlk)
                self.piano = 1
                self.d = 1

    def playPiano(self):
        self.pi = pygame.mixer.Channel(3)
        self.pi.play(pygame.mixer.Sound('Songs/piano.wav'),-1)
        self.pi.set_volume(0.5)
        self.piano = 0
        self.Button5.configure(image=self.pianoOri)



    def callingthread7(self):
        if self.start == 0:
            if self.timbales == 1:
                self.playTimbales()
                self.e = 0
            else:
                print("stop")
                self.Button5_5.configure(image=self.bongosBlk)
                #pygame.mixer.Channel(0).stop()
                pygame.mixer.Channel(4).stop()
                self.timbales = 1
                self.e = 1
        else:
            if self.e == 1:
                self.Button5_5.configure(image=self.bongosOri)
                self.timbales = 0
                self.e = 0
            else:
                self.Button5_5.configure(image=self.bongosBlk)
                self.timbales = 1
                self.e = 1

    def playTimbales(self):
        self.tim = pygame.mixer.Channel(4)
        self.tim.play(pygame.mixer.Sound('Songs/timbales.wav'),-1)
        self.tim.set_volume(0.5)
        self.timbales = 0
        self.Button5_5.configure(image=self.bongosOri)



    def callingthread8(self):
        if self.start == 0:
            if self.guiro == 1:
                self.playGuiro()
                self.f = 0
            else:
                print("stop")
                self.Button5_7.configure(image=self.guiroBlk)

                #pygame.mixer.Channel(0).stop()
                pygame.mixer.Channel(5).stop()
                self.guiro = 1
                self.f = 1
        else:
            if self.f == 1:
                self.Button5_7.configure(image=self.guiroOri)
                self.guiro = 0
                self.f = 0
            else:
                self.Button5_7.configure(image=self.guiroBlk)
                self.guiro = 1
                self.f = 1

    def playGuiro(self):
        self.gui = pygame.mixer.Channel(5)
        self.gui.play(pygame.mixer.Sound('Songs/guiro.wav'),-1)
        self.gui.set_volume(0.5)
        self.guiro = 0
        self.Button5_7.configure(image=self.guiroOri)

        #root.update()
    def callingthread9(self):
        if self.start == 0:
            if self.drum == 1:
                self.playDrum()
                self.g = 0
            else:
                print("stop")
                self.Button5_8.configure(image=self.drumBlk)

                pygame.mixer.Channel(6).stop()
                #pygame.mixer.Channel().stop()
                self.drum = 1
                self.g = 1
        else:
            if self.g == 1:
                self.Button5_8.configure(image=self.drumOri)
                self.drum = 0
                self.g = 0
            else:
                self.Button5_8.configure(image=self.drumBlk)
                self.drum = 1
                self.g = 1

    def playDrum(self):
        self.dr = pygame.mixer.Channel(6)
        self.dr.play(pygame.mixer.Sound('Songs/drum.wav'),-1)
        self.dr.set_volume(0.5)
        self.drum = 0
        self.Button5_8.configure(image=self.drumOri)

    def callingthread10(self):
        if self.start == 0:

            if self.maracas == 1:
                self.playMaracas()
                self.h = 0
            else:
                print("stop")
                self.Button5_9.configure(image=self.maracasBlk)
                #pygame.mixer.Channel(7).stop()
                self.mara.stop()
                self.maracas = 1
                self.h = 1

        else:
            if self.h == 1:
                self.Button5_9.configure(image=self.maracasOri)
                self.maracas = 0
                self.h = 0
            else:
                self.Button5_9.configure(image=self.maracasBlk)
                self.maracas = 1
                self.h = 1

    def playMaracas(self):
        self.Button5_9.configure(image=self.maracasOri)
        self.mara = pygame.mixer.Channel(7)
        self.mara.play(pygame.mixer.Sound('Songs/maracas.wav'),-1)
        self.mara.set_volume(0.5)
        #a.set_volume(1.0)
        self.maracas = 0

    def stopMusic(self):
        pygame.mixer.Channel(0).pause()
        pygame.mixer.Channel(1).stop()
        pygame.mixer.Channel(2).stop()
        pygame.mixer.Channel(3).stop()
        pygame.mixer.Channel(4).stop()
        pygame.mixer.Channel(5).stop()
        pygame.mixer.Channel(6).stop()
        pygame.mixer.Channel(7).stop()

    def pauseMusic(self):
        if self.clave == 0:
            self.playClave()
            self.clave = 0

        if self.cowbell == 0:
            self.playCowbell()
            self.cowbell = 0
        if self.congas == 0:
            self.playCongas()
            self.congas = 0
        if self.piano == 0:
            self.playPiano()
            self.piano = 0
        if self.guiro == 0:
            self.playGuiro()
            self.guiro = 0
        if self.drum == 0:
            self.playDrum()
            self.drum = 0
        if self.timbales == 0:
            self.playTimbales()
            self.timbales = 0
        if self.maracas == 0:
            self.playMaracas()
            self.maracas = 0

    def defaultphoto(self):
        self.Button5_9.configure(image=self.maracasBlk)
        self.Button5_8.configure(image=self.drumBlk)
        self.Button2.configure(image=self.claveBlk)
        self.Button3.configure(image=self.cowbellBlk)
        self.Button4.configure(image=self.congasBlk)
        self.Button5.configure(image=self.pianoBlk)
        self.Button5_5.configure(image=self.bongosBlk)
        self.Button5_7.configure(image=self.guiroBlk)

    def playsalsa(self):
        self.threadmusic1()
        self.threadmusic2()
        self.threadmusic3()
        self.threadmusic4()
        self.threadmusic7()
        self.threadmusic8()
        self.threadmusic9()
        self.threadmusic10()

    def clave_text(self):
        self.TLabel3 = ttk.Label(self.Frame2)
        self.TLabel3.place(relx=0.051, rely=0.346, height=27, width=60)
        self.TLabel3.configure(background="white")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font=self.font16)
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''Clave''')

    def cowbell_text(self):
        self.TLabel3_28 = ttk.Label(self.Frame2)
        self.TLabel3_28.place(relx=0.257, rely=0.346, height=27, width=80)
        self.TLabel3_28.configure(background="white")
        self.TLabel3_28.configure(foreground="#000000")
        self.TLabel3_28.configure(font="-family {News706 BT} -size 13 -weight bold")
        self.TLabel3_28.configure(relief="flat")
        self.TLabel3_28.configure(anchor='w')
        self.TLabel3_28.configure(justify='left')
        self.TLabel3_28.configure(text='''Cowbell''')

    def congas_text(self):
        self.TLabel3_29 = ttk.Label(self.Frame2)
        self.TLabel3_29.place(relx=0.424, rely=0.346, height=27, width=70)
        self.TLabel3_29.configure(background="white")
        self.TLabel3_29.configure(foreground="#000000")
        self.TLabel3_29.configure(font="-family {News706 BT} -size 13 -weight bold")
        self.TLabel3_29.configure(relief="flat")
        self.TLabel3_29.configure(anchor='w')
        self.TLabel3_29.configure(justify='left')
        self.TLabel3_29.configure(text='''Congas''')

    def piano_text(self):
        self.TLabel3_30 = ttk.Label(self.Frame2)
        self.TLabel3_30.place(relx=0.643, rely=0.346, height=27, width=59)
        self.TLabel3_30.configure(background="white")
        self.TLabel3_30.configure(foreground="#000000")
        self.TLabel3_30.configure(font="-family {News706 BT} -size 13 -weight bold")
        self.TLabel3_30.configure(relief="flat")
        self.TLabel3_30.configure(anchor='w')
        self.TLabel3_30.configure(justify='left')
        self.TLabel3_30.configure(text='''Piano''')

    def timbales_text(self):
        self.TLabel3_33 = ttk.Label(self.Frame2)
        self.TLabel3_33.place(relx=0.823, rely=0.346, height=27, width=110)

        self.TLabel3_33.configure(background="white")
        self.TLabel3_33.configure(foreground="#000000")
        self.TLabel3_33.configure(font="-family {News706 BT} -size 13 -weight bold")
        self.TLabel3_33.configure(relief="flat")
        self.TLabel3_33.configure(anchor='w')
        self.TLabel3_33.configure(justify='left')
        self.TLabel3_33.configure(text='''Timbales''')

    def guiro_text(self):
        self.TLabel3_34 = ttk.Label(self.Frame2)
        self.TLabel3_34.place(relx=0.180, rely=0.895, height=27, width=60)
        self.TLabel3_34.configure(background="white")
        self.TLabel3_34.configure(foreground="#000000")
        self.TLabel3_34.configure(font="-family {News706 BT} -size 13 -weight bold")
        self.TLabel3_34.configure(relief="flat")
        self.TLabel3_34.configure(anchor='w')
        self.TLabel3_34.configure(justify='left')
        self.TLabel3_34.configure(text='''Güiro''')

    def bongos_text(self):
        self.TLabel3_35 = ttk.Label(self.Frame2)
        self.TLabel3_35.place(relx=0.400, rely=0.895, height=27, width=70)
        self.TLabel3_35.configure(background="white")
        self.TLabel3_35.configure(foreground="#000000")
        self.TLabel3_35.configure(font="-family {News706 BT} -size 13 -weight bold")
        self.TLabel3_35.configure(relief="flat")
        self.TLabel3_35.configure(anchor='w')
        self.TLabel3_35.configure(justify='left')
        self.TLabel3_35.configure(text='''Bongos''')

    def maracas_text(self):
        self.TLabel3_36 = ttk.Label(self.Frame2)
        self.TLabel3_36.place(relx=0.623, rely=0.887, height=27, width=80)
        self.TLabel3_36.configure(background="white")
        self.TLabel3_36.configure(foreground="#000000")
        self.TLabel3_36.configure(font="-family {News706 BT} -size 13 -weight bold")
        self.TLabel3_36.configure(relief="flat")
        self.TLabel3_36.configure(anchor='w')
        self.TLabel3_36.configure(justify='left')
        self.TLabel3_36.configure(text='''Maracas''')

    def clave_Volume(self):
        if self.vol1 == 1:
            self.TLabel3.destroy()
            self.TLabel3 = ttk.Scale(self.Frame2, from_=0, to=100)
            root.update_idletasks()
            self.TLabel3.place(relx=0.051, rely=0.346, relwidth=0.150, relheight=0.0
                               , height=18, bordermode='ignore')
            self.TLabel3.configure(takefocus="",command=self.setvol1)
            self.style.configure('.', background="white")
            self.TLabel3.set(50)
            self.vol1 = 0
        else:
            self.TLabel3.destroy()
            self.clave_text()
            self.vol1 = 1

    def cowbell_Volume(self):
        if self.vol2 == 1:
            self.TLabel3_28.destroy()
            self.TLabel3_28 = ttk.Scale(self.Frame2, from_=0, to=100)
            root.update_idletasks()
            self.TLabel3_28.place(relx=0.257, rely=0.346, relwidth=0.150, relheight=0.0
                               , height=18, bordermode='ignore')
            self.TLabel3_28.configure(takefocus="",command=self.setvol2)
            self.style.configure('.', background="white")
            self.vol2 = 0
            self.TLabel3_28.set(50)
        else:
            self.TLabel3_28.destroy()
            self.cowbell_text()
            self.vol2 = 1

    def congas_Volume(self):
        if self.vol3 == 1:
            self.TLabel3_29.destroy()
            self.TLabel3_29 = ttk.Scale(self.Frame2, from_=0, to=100)
            root.update_idletasks()
            self.TLabel3_29.place(relx=0.424, rely=0.346, relwidth=0.150, relheight=0.0
                               , height=18, bordermode='ignore')
            self.TLabel3_29.configure(takefocus="",command=self.setvol3)
            self.style.configure('.', background="white")
            self.vol3 = 0
            self.TLabel3_29.set(50)
        else:
            self.TLabel3_29.destroy()
            self.congas_text()
            self.vol3 = 1

    def piano_Volume(self):
        if self.vol4 == 1:
            self.TLabel3_30.destroy()
            self.TLabel3_30 = ttk.Scale(self.Frame2, from_=0, to=100)
            root.update_idletasks()
            self.TLabel3_30.place(relx=0.623, rely=0.346, relwidth=0.150, relheight=0.0
                               , height=18, bordermode='ignore')
            self.TLabel3_30.configure(takefocus="",command=self.setvol4)
            self.style.configure('.', background="white")
            self.vol4 = 0
            self.TLabel3_30.set(50)
        else:
            self.TLabel3_30.destroy()
            self.piano_text()
            self.vol4 = 1

    def timbales_Volume(self):
        if self.vol5 == 1:
            self.TLabel3_33.destroy()
            self.TLabel3_33 = ttk.Scale(self.Frame2, from_=0, to=100)
            root.update_idletasks()
            self.TLabel3_33.place(relx=0.823, rely=0.346, relwidth=0.150, relheight=0.0
                               , height=18, bordermode='ignore')
            self.TLabel3_33.configure(takefocus="",command=self.setvol5)
            self.style.configure('.', background="white")
            self.vol5 = 0
            self.TLabel3_33.set(50)
        else:
            self.TLabel3_33.destroy()
            self.timbales_text()
            self.vol5 = 1

    def guiro_Volume(self):
        if self.vol6 == 1:
            self.TLabel3_34.destroy()
            self.TLabel3_34 = ttk.Scale(self.Frame2, from_=0, to=100)
            root.update_idletasks()
            self.TLabel3_34.place(relx=0.180, rely=0.895, relwidth=0.150, relheight=0.0
                               , height=18, bordermode='ignore')
            self.TLabel3_34.configure(takefocus="",command=self.setvol6)
            self.style.configure('.', background="white")
            self.vol6 = 0
            self.TLabel3_34.set(50)
        else:
            self.TLabel3_34.destroy()
            self.guiro_text()
            self.vol6 = 1

    def bongos_Volume(self):
        if self.vol7 == 1:
            self.TLabel3_35.destroy()
            self.TLabel3_35 = ttk.Scale(self.Frame2, from_=0, to=100)
            root.update_idletasks()
            self.TLabel3_35.place(relx=0.400, rely=0.895, relwidth=0.150, relheight=0.0
                               , height=18, bordermode='ignore')
            self.TLabel3_35.configure(takefocus="",command=self.setvol7)
            self.style.configure('.', background="white")
            self.vol7 = 0
            self.TLabel3_35.set(50)
        else:
            self.TLabel3_35.destroy()
            self.bongos_text()
            self.vol7 = 1

    def maracas_Volume(self):
        if self.vol8 == 1:
            self.TLabel3_36.destroy()
            self.TLabel3_36 = ttk.Scale(self.Frame2, from_=0, to=100)
            root.update_idletasks()
            self.TLabel3_36.place(relx=0.623, rely=0.887, relwidth=0.150, relheight=0.0
                               , height=18, bordermode='ignore')
            self.TLabel3_36.configure(takefocus="")
            self.style.configure('.', background="white")
            self.TLabel3_36.configure(command=self.setvol8)
            self.TLabel3_36.set(50)
            self.vol8 = 0

        else:
            self.TLabel3_36.destroy()
            self.maracas_text()
            self.vol8 = 1

    def setvol1(self,*event):
        try:
            volum = self.TLabel3.get()
            self.cla.set_volume(volum * 0.01)

        except AttributeError:
            pass

    def setvol2(self, *event):
        try:
            volum = self.TLabel3_28.get()
            self.cow.set_volume(volum * 0.01)

        except AttributeError:
            pass

    def setvol3(self, *event):
        try:
            volum = self.TLabel3_29.get()
            self.con.set_volume(volum * 0.01)

        except AttributeError:
            pass

    def setvol4(self, *event):
        try:
            volum = self.TLabel3_30.get()
            self.pi.set_volume(volum * 0.01)

        except AttributeError:
            pass

    def setvol5(self, *event):
        try:
            volum = self.TLabel3_33.get()
            self.tim.set_volume(volum * 0.01)

        except AttributeError:
            pass

    def setvol6(self, *event):
        try:
            volum = self.TLabel3_34.get()
            self.gui.set_volume(volum * 0.01)

        except AttributeError:
            pass

    def setvol7(self, *event):
        try:
            volum = self.TLabel3_35.get()
            self.dr.set_volume(volum * 0.01)

        except AttributeError:
            pass

    def setvol8(self, *event):
        try:
            volum = self.TLabel3_36.get()
            self.mara.set_volume(volum * 0.01)
        except AttributeError:
            pass

if __name__ == '__main__':
    vp_start_gui()





