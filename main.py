#coding: utf-8

from tkinter import *

from wand.color import Color
from wand.drawing import Drawing

angle=0
distance=0

root_w =1920
root_h =1080

root =Tk()
root.title("Ultrason radar")
root.geometry('%dx%d'%(root_w,root_h))
root.configure(background='#17202A')

C = Canvas(root, bg="#17202A", height=root_h, width=root_w)
#def serial_event():
def drawRadar():

    arc_40_cm = C.create_arc(100, 100, 1800, 1800, start=0, extent=180,outline="green", width=4)
    arc_30_cm = C.create_arc(300, 300, 1600, 1600, start=0, extent=180,outline="green", width=4)
    arc_20_cm = C.create_arc(500, 500, 1400, 1400, start=0, extent=180,outline="green", width=4)
    arc_10_cm = C.create_arc(700, 700, 1200, 1200, start=0, extent=180,outline="green", width=4)

    #line_180_degree = C.create_line(0, 0, 950, 950, fill='green', width=5)
    line_150_degree = C.create_line(20, 400, 950, 950, fill='green', width=5)
    line_120_bis_degree = C.create_line(400, 20, 950, 950, fill='red', width=5)
    line_120_degree = C.create_line(350, 20, 950, 950, fill='green', width=5)
    line_90_degree  = C.create_line(950, 20, 950, 950, fill='green', width=5)
    #line_60_degree  = C.create_line(0, 0, 1000, 1000, fill='green', width=5)
    #line_30_degree  = C.create_line(0, 0, 950, 950, fill='green', width=5)
    #line_0_degree   = C.create_line(0, 0, 950, 950, fill='green', width=5)
    line_0_degree   = C.create_line(0, 960, 0, 960, fill='orange', width=5)

    """with Drawing() as draw:
        draw.stroke_color = Color('green')
        draw.arc((0, 0),  # Starting point
                 (root_w, root_w),  # Ending point
                 (90, 180))  # From bottom left around to top right"""


def drawLIne():
    for i in range(180):
        arc_40_cm = C.create_arc(100, 100, 1800, 1800, start=0, extent=i, outline="orange", width=4)
        C.update_idletasks()

def drawLIneinv():
    for i in range(180):
        arc_40_cm = C.create_arc(100, 100, 1800, 1800, start=0, extent=180-i, outline="#17202A", width=4)
        C.update_idletasks()
#def drawText():


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run=1
    C.pack()
    while(run==1):
        drawRadar()
        drawLIne()
        drawRadar()
        drawLIneinv()
    root.mainloop()