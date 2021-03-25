from tkinter import *
from tkinter import messagebox
from pyzbar.pyzbar import decode
import pyqrcode
import time
root=Tk()
root.geometry('600x400')
root.title('My QR code')
root.wm_iconbitmap('E:\QR_Generator\myqr.ico')
root.configure(bg="cyan")
################################################################### functions
def Generate_QR():
    QR_Name=QR_Name_Entry.get()
    QR_ID=QR_ID_Entry.get()
    QR_Message=QR_Message_Entry.get()
    Message_QR='Name : '+QR_Name+'\n'+'ID : '+QR_ID+'\n'+'Message : '+QR_Message
    url=pyqrcode.create(Message_QR)
    url.png('{}.png'.format(time.time()),scale=8)
def Clear_ID_Name():
    QR_ID_Entry.delete(0,'end')
    QR_Message_Entry.delete(0,'end')
    QR_Name_Entry.delete(0,'end') 
    QR_Notification_message_label.configure(text="")
def Quit_root():
    res=messagebox.askokcancel('Exit','Are you sure you want to exit?')
    if res==True:
        root.destroy()
    else:
        pass
def read_web_cam():
    import cv2.cv2
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        data = 'Nothing Found'
        try:
            obj = decode(frame)
            data = str(obj[0].data)[2:-1]
        except Exception as e: 
            print(e)

        cv2.putText(frame, data, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2)
        cv2.imshow('Show QR', frame)

        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()

def read_img():
    from PIL import Image
    fileName = input('Enter file path: ')

    obj = decode(Image.open(fileName))
    data = str(obj[0].data)[2:-1]

    print(data)
    input('\nPress any key to exit...')

################################################################### labels
QR_ID_label=Label(master=root,text="Enter Email ID",bg="blue",fg='floral white',width=20,height=2,font=('arial',12,'italic bold'))
QR_ID_label.place(x=10,y=80)
QR_Name_label=Label(master=root,text="Enter Name",bg="blue",fg='floral white',width=20,height=2,font=('arial',12,'italic bold'))
QR_Name_label.place(x=10,y=130)
QR_Message_label=Label(master=root,text="Enter Message",bg="blue",fg='floral white',width=20,height=2,font=('arial',12,'italic bold'))
QR_Message_label.place(x=10,y=180)
QR_Notification_label=Label(master=root,text="Notification:",bg="blue",fg='floral white',width=20,height=2,font=('arial',12,'italic bold'))
QR_Notification_label.place(x=10,y=350)
QR_Notification_message_label=Label(master=root,text="",bg="floral white",width=30,height=2,font=('arial',12,'italic bold'))
QR_Notification_message_label.place(x=250,y=350)

#################################################################### Entry boxes
QR_ID_Entry=Entry(master=root,width=25,bd=5,bg='floral white',font=('arial',17,'italic bold'))
QR_ID_Entry.place(x=250,y=80)

QR_Name_Entry=Entry(master=root,width=25,bd=5,bg='floral white',font=('arial',17,'italic bold'))
QR_Name_Entry.place(x=250,y=130)

QR_Message_Entry=Entry(master=root,width=25,bd=5,bg='floral white',font=('arial',17,'italic bold'))
QR_Message_Entry.place(x=250,y=180)
#########################################################################################
QR_image=PhotoImage(file='E:\QR_Generator\qr-code.png')
QR_image=QR_image.subsample(2,2)
Clear_id_image=PhotoImage(file='E:\QR_Generator\clean.png')
Clear_id_image=Clear_id_image.subsample(2,2)
Cancel_image=PhotoImage(file='E:\QR_Generator\close.png')
Cancel_image=Cancel_image.subsample(2,2)
Scan_image=PhotoImage(file='E:\QR_Generator\qr-code.png')
Scan_image=Scan_image.subsample(2,2)
######################################################################################### generate
Generate_QR=Button(master=root,text='Generate QR',width=120,font=('arial',10,'bold'),bd=10,activebackground='blue',image=QR_image,compound=RIGHT,command=Generate_QR)
Generate_QR.place(x=10,y=250)
Clear_ID=Button(master=root,text='Clear',width=80,font=('arial',10,'bold'),bd=10,activebackground='blue',image=Clear_id_image,compound=RIGHT,command=Clear_ID_Name)
Clear_ID.place(x=170,y=250)
Quit=Button(master=root,text='Quit',width=60,font=('arial',10,'bold'),bd=10,activebackground='blue',image=Cancel_image,compound=RIGHT,command=Quit_root)
Quit.place(x=280,y=250)
ScanIMG=Button(master=root,text='Scan Image',width=100,font=('arial',10,'bold'),bd=10,activebackground='blue',image=Scan_image,compound=RIGHT,command=read_web_cam)
ScanIMG.place(x=380,y=250)
LoadIMG=Button(master=root,text='Load QR',width=100,font=('arial',10,'bold'),bd=10,activebackground='blue',image=Scan_image,compound=RIGHT,command=read_img)
LoadIMG.place(x=520,y=250)

########################################################################################### hover effect
def Generate_QR_ButtonEnter(e):
    Generate_QR['bg']='purple2'
def Generate_QR_ButtonLeave(e):
    Generate_QR['bg']='powder blue'
def Clear_ID_ButtonEnter(e):
    Clear_ID['bg']='purple2'
def Clear_ID_ButtonLeave(e):
    Clear_ID['bg']='powder blue'
def Quit_ButtonEnter(e):
    Quit['bg']='purple2'
def Quit_ButtonLeave(e):
    Quit['bg']='powder blue'


Generate_QR.bind('<Enter>',Generate_QR_ButtonEnter)
Generate_QR.bind('<Leave>',Generate_QR_ButtonLeave)

Clear_ID.bind('<Enter>',Clear_ID_ButtonEnter)
Clear_ID.bind('<Leave>',Clear_ID_ButtonLeave)

Quit.bind('<Enter>',Quit_ButtonEnter)
Quit.bind('<Leave>',Quit_ButtonLeave)
