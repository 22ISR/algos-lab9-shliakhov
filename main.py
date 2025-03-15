import tkinter as tk
okno = tk.Tk()
# root.mainloop()
okno.geometry("700x400")
okno.title("Калькулятор")
label = tk.Label(okno, text="Hello world!", font=("Arial", 18))
buttonFrame = tk.Frame(okno)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)

btn1 = tk.Button(buttonFrame, text="1", font=("Arial", 18))
btn1.grid(row=0, column=0, sticky="we")

btn2 = tk.Button(buttonFrame, text="2", font=("Arial", 18))
btn2.grid(row=0, column=1, sticky="we")

btn3 = tk.Button(buttonFrame, text="3", font=("Arial", 18))
btn3.grid(row=0, column=2, sticky="we")

btnminus = tk.Button(buttonFrame, text="-", font=("Arial", 18))
btnminus.grid(row=0, column=3, sticky="we")



btn4 = tk.Button(buttonFrame, text="4", font=("Arial", 18))
btn4.grid(row=1, column=0, sticky="we")

btn5 = tk.Button(buttonFrame, text="5", font=("Arial", 18))
btn5.grid(row=1, column=1, sticky="we")

btn6 = tk.Button(buttonFrame, text="6", font=("Arial", 18))
btn3.grid(row=1, column=2, sticky="we")

btnplus = tk.Button(buttonFrame, text="+", font=("Arial", 18))
btnplus.grid(row=1, column=3, sticky="we")


btn7 = tk.Button(buttonFrame, text="7", font=("Arial", 18))
btn7.grid(row=2, column=0, sticky="we")

btn8 = tk.Button(buttonFrame, text="8", font=("Arial", 18))
btn8.grid(row=2, column=1, sticky="we")

btn9 = tk.Button(buttonFrame, text="9", font=("Arial", 18))
btn9.grid(row=2, column=2, sticky="we")

btnymn = tk.Button(buttonFrame, text="*", font=("Arial", 18))
btnymn.grid(row=2, column=3, sticky="we")


btnclear = tk.Button(buttonFrame, text="Clear", font=("Arial", 18))
btnclear.grid(row=3, column=0, sticky="we")

btn0 = tk.Button(buttonFrame, text="0", font=("Arial", 18))
btn0.grid(row=3, column=1, sticky="we")

btnrovn = tk.Button(buttonFrame, text="=", font=("Arial", 18))
btnrovn.grid(row=3, column=2, sticky="we")

btndel = tk.Button(buttonFrame, text="/", font=("Arial", 18))
btndel.grid(row=3, column=3, sticky="we")