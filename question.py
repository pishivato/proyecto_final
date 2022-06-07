import random
from tkinter import *
from tkinter import simpledialog

wind = Tk()
wind.withdraw()
class Pregunta:
    
    def Preguntas(self):
        answer = False
        preguntas = []
        operadores = ["+", "-", "*", "/"]
        
        for i in range(0, 100):
            preguntas.append(random.randint(0, 100))
        
        for i in preguntas:
            y,z = preguntas[random.randint(0, preguntas[-1])], preguntas[random.randint(0, preguntas[-1])]

        x = random.choice(operadores) 
        
        if x == "+":
            sum = y+z    
            respuesta = simpledialog.askinteger(f"Cuanto es {y} + {z}: ", wind)
            if respuesta == sum:             
                answer = True

        elif x == "-":
            res = y-z
            respuesta = simpledialog.askinteger(f"Cuanto es {y} - {z}: ", wind)
            if respuesta == res:
                answer = True

        elif x == "*":
            mul = y*z
            respuesta = simpledialog.askinteger(f"Cuanto es {y} * {z}: ", wind)
            if respuesta == mul:
                answer = True
        
        elif x == "/":
            div = y/z
            respuesta = simpledialog.askinteger(f"Cuanto es {y} / {z}: ", wind)
            if respuesta == round(div):
                answer = True
        
        return answer