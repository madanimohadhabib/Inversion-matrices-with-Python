# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 13:43:47 2021

@author: pc
"""

from tkinter import Tk, Label, StringVar, Button, Entry
import numpy as np

  
def inverse_and_show():
    inv_mat = np.linalg.inv([[float(entry.get()) for entry in row] for row in text_var])
    det_mat = np.linalg.det([[float(entry.get()) for entry in row] for row in text_var])
    cofactor = inv_mat.T * det_mat  
    Label(window, text="The determinant |A|= "+str(det_mat), font=('arial', 10, 'bold'), bg="bisque2").place(x=390, y=90) 
    Label(window, text="Adj(A)= "+str(cofactor)+" t", font=('arial', 10, 'bold'), bg="bisque2").place(x=390, y=120)    
    for i, j in [[_i, _j] for _i in range(3) for _j in range(3)]:
        output[i][j].config(text=np.round(inv_mat[i][j], decimals=2))
window = Tk()
window.title("Matrix Inverse")
window.configure(bg='bisque2', height=300, width=740)
text_var = [[StringVar() for i in range(3)] for j in range(3)]
entries = [[Entry(window, width=5, textvariable=text_var[i][j]) for j in range(3)] for i in range(3)]
output = [[Label(window, width=5, text="", bg='white') for i in range(3)] for j in range(3)]
Label(window, text="\tThis program is a mini calculator of the inverse of 3x3 Matrices :\n", font=('arial', 10, 'bold'), bg="bisque2").place(x=20, y=10)
Label(window, text="Created this code by:\tMadani Mohamed El-Habib \tHerrouel Nor El-yacine  \tBenkahla Mohamed", font=('arial', 10, 'bold'), bg="bisque2").place(x=20, y=30)
Label(window, text="Enter matrix :", font=('arial', 10, 'bold'), bg="bisque2").place(x=20, y=50)
for i, j in [[_i, _j] for _i in range(3) for _j in range(3)]:
    output[i][j].place(x=200 + j * 70, y=80 + i * 50)
    entries[i][j].place(x=50 + j * 30, y=80 + i * 50)
Button(window, text="Inverse", bg='bisque3', width=15, command=inverse_and_show).place(x=100, y=250)
window.mainloop()
