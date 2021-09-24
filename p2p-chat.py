import socket
from tkinter import *

mainWindow = Tk()

# Настройка приема
rIP = '192.168.89.24' # use MacBookPro ip or 0.0.0.0
rPort = 30002
rSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
rSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
rSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
rSock.bind((rIP, rPort))

# Настройка отправки
sIP = '192.168.89.14' # use HOME-PC ip or 255.255.255.255
sPort = 30002
sSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Параметры окна
mainWindow.title('Dobrui Chat')
mainWindow.geometry('400x30')

# Форма ввода
textBox = StringVar()
message = Entry(mainWindow, textvariable=textBox)
message.pack(side='bottom', fill='x', expand='true')

# Получение сообщений
def MsgReciever():
    rSock.setblocking(False)
    try:
        message = rSock.recv(1024)
        message = message.decode('utf-8')
        message.delete(0,END)
        message.insert(END, message)
    except:
        mainWindow.after(1, MsgReciever)
        return
    mainWindow.after(1, MsgReciever)
    return

# Отправка сообщений при вызове события
def MsgSender(event):
    sSock.sendto(textBox.get().encode('utf-8'), (sIP, sPort))

#Бинд выполнения события по нажатию кнопи
message.bind('<Return>', MsgSender)
mainWindow.after(1, MsgReciever)

mainWindow.mainloop()
