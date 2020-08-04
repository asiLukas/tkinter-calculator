from tkinter import *

window = Tk()
window.title('Calculator')
window.configure(background='black')
window.geometry('589x555')

buttons = [
    '7', '8', '9', '*', '**2', '(',
    '4', '5', '6', '/', '//', ')',
    '1', '2', '3', '-', '%', '**(1/2)',
    '0', '.', '=', '+', 'Clear', 'AC']
row = 1
col = 0

for i in buttons:
    action = lambda x=i: when_clicked(x)
    Button(window, text=i, width='11', height='7', foreground='white', background='gray10', font="sans-serif 10 bold",
           command=action).grid(row=row, column=col)

    # These bunch of if statements are just for esthetics, not important(I couldn't think of better way of doing it)
    if i == '**2':
        Button(window, text='x²', width='11', height='7', foreground='white', background='gray10',
               font="sans-serif 10 bold", command=action).grid(
            row=row, column=col)
    elif i == '=':
        Button(window, text=i, width='11', height='7', foreground='white', background='gray30',
               font="sans-serif 10 bold", command=action).grid(
            row=row, column=col)
    elif i == 'AC':
        Button(window, text=i, width='11', height='7', foreground='white', background='darkred',
               font="sans-serif 10 bold", command=action).grid(
            row=row, column=col)
    elif i == 'Clear':
        Button(window, text='Delete last', width='11', height='7', foreground='white', background='grey30',
               font="sans-serif 10 bold", command=action).grid(
            row=row, column=col)
    elif i == '*':
        Button(window, text='×', width='11', height='7', foreground='white', background='gray10',
               font="sans-serif 10 bold", command=action).grid(
            row=row, column=col)
    elif i == '/':
        Button(window, text='÷', width='11', height='7', foreground='white', background='gray10',
               font="sans-serif 10 bold", command=action).grid(
            row=row, column=col)
    elif i == '%':
        Button(window, text='%Modulus', width='11', height='7', foreground='white', background='gray10',
               font="sans-serif 10 bold", command=action).grid(
            row=row, column=col)
    elif i == '//':
        Button(window, text='//Floor Division', width='11', height='7', foreground='white', background='gray10',
               font="sans-serif 10 bold", command=action).grid(
            row=row, column=col)
    elif i == '**(1/2)':
        Button(window, text='√x', width='11', height='7', foreground='white', background='gray10',
               font="sans-serif 10 bold", command=action).grid(
            row=row, column=col)

    col += 1

    if col > 5:
        col = 0
        row += 1

display = Entry(window, width=23, bg='gray10', font="sans-serif 35 bold", fg='white')
display.grid(row=7, column=0, columnspan=60)


def when_clicked(key):
    if key == '=':

        try:
            result = eval(display.get())
            display.insert(END, " = " + str(result))

        except (SyntaxError, NameError):
            display.insert(END, " Err, not valid")

    elif key == 'AC':
        display.delete(0, END)

    elif key == 'Clear':
        display.delete(len(display.get()) - 1, END)

    else:
        if '=' in display.get():
            display.delete(0, END)
        display.insert(END, key)


window.mainloop()
