from tkinter import *
from tkinter.font import BOLD
import tkinter.messagebox as msg
from tkinter import ttk
import datetime as dt

class Loginregisteruser:
    def main_screen(self):
        Button(text='Login',bg= "White",fg='Black',height= '2',width= '30',command = self.login).place(x=140, y=160)
    
    def __init__(self,gui,header):
        self.gui = gui
        self.gui.geometry('480x318')
        self.gui.title(header)
        self.gui.resizable(0,0)
        self.main_screen()

    def login(self):
        screen1 = Toplevel(app)
        screen1.title("Login CGV CINEMA")
        screen1.geometry('350x160')
        screen1.resizable(0,0)
        Label(screen1, text= "Email").pack()
        self.entryUser = Entry(screen1, width=30)
        self.entryUser.pack()
        Label(screen1, text = "Password").pack()
        self.entryPass = Entry(screen1,show='#',width=30)
        self.entryPass.pack()
        self.check = IntVar()
        self.showPass = Checkbutton(screen1, text = "Show Password", variable=self.check,command=self.open_password).pack(expand=False,fill=BOTH,padx=10,pady=5)
        self.showPass
        self.btnlogin = Button(screen1, text="Login", bg= 'white',fg='black',command=self.do_login).pack(side=LEFT,expand=True,fill= BOTH, padx= 10,pady=5)
        
    def do_login(self):
        get_username = self.entryUser.get()
        get_password = self.entryPass.get()
        sukses = False
        file = open('database.txt','r')
        
        for i in file :
            name,email,password = i.split(",")
            password = password.strip()
            if get_username == email and get_password == password:
                sukses = True
                break
        if (sukses):
            msg.showinfo("Login Success","Login Berhasil %s"%(name),parent=self.gui)
            self.sec_screen()
            return 
        elif get_username == '' or get_password == '':
            msg.showwarning("Login Gagal","Email atau Password Tidak Boleh Kosong",parent=self.gui)
            self.entryUser.focus_set()
        else :
            msg.showerror('Login Gagal','Email atau Password Salah',parent=self.gui)
            self.delete_data()
    
    def open_password(self):
        Show = self.check.get()      
        if Show == 1:
            self.entryPass['show']=''
        else :
            self.entryPass['show']='#'

    def sec_screen(self):
        global screen2
        screen2 = Toplevel(app)
        screen2.title("CGV CINEMA")
        screen2.geometry('400x450')
        screen2.resizable(0,0)
              
        Label(screen2,text="PESAN TIKET" ,bg='Black',width='300',height='2',font= ('courier new',13, "bold"),fg='white').pack()
        Label(screen2, text='').pack()
        Label(screen2,text= "Nama\t\t:",).place(x=30, y=60)
        self.entryID = Entry(screen2, font = ("times new roman", 10))
        self.entryID.place(x=140, y=57)

        self.radiochr = IntVar()
        Label(screen2, text = "Seet\t\t:").place(x=30, y=80)
        self.entrykursi1 = Radiobutton(screen2, text = 'A', variable=self.radiochr,value =1,command=self.seet)
        self.entrykursi1.place(x = 140, y = 80)
        self.entrykursi2 = Radiobutton(screen2, text = 'B', variable=self.radiochr,value =2,command=self.seet1)
        self.entrykursi2.place(x = 140, y = 100)
        self.entrykursi3 = Radiobutton(screen2, text = 'C', variable=self.radiochr,value =3,command=self.seet2)
        self.entrykursi3.place(x = 140, y = 120)
        Label(screen2, text='Nomor\t\t:').place(x=30, y=140)
        
        self.radio = IntVar()
        Label(screen2, text = "Genre\t\t:").place(x=30, y=165)
        self.entrySrv1 = Radiobutton(screen2, text = 'Romance', variable=self.radio,value =1,command=self.roman_srv)
        self.entrySrv1.place(x = 140, y = 165)
        self.entrySrv2 = Radiobutton(screen2, text = 'Action', variable=self.radio,value =2,command=self.act_srv)
        self.entrySrv2.place(x = 140, y = 185)
        self.entrySrv3 = Radiobutton(screen2, text = 'Horor', variable=self.radio,value =3,command=self.hor_srv)
        self.entrySrv3.place(x = 140, y = 205)
        
        Label(screen2, text='Film\t\t:').place(x=30, y=230)
        Label (screen2, text ="Price List\t\t:").place(x=30, y=260)
        self.radiobtn = IntVar()
        self.radio1 = Radiobutton(screen2, text="Reguler - 30K",variable = self.radiobtn,value=31000).place(x = 140, y = 260)
        self.radio2 = Radiobutton(screen2,text="Sweet Box - 60K",variable = self.radiobtn,value=63000).place(x = 140, y = 280)
        
        Label(screen2,text="Payment Method\t:").place(x=30, y=320)
        self.strpym = StringVar(value='...') 
        self.combobox1 = ttk.Combobox(screen2,width = 17,font = ("times new roman", 10), textvariable = self.strpym, state ="readonly")
        self.combobox1.place(x=140, y=320)
        self.combobox1['values'] = ('Gopay','Dana','OVO','BCA','BRI')
        
        btn = Button(screen2, text="Pay", command=self.payment,bg= 'lightgreen',state=ACTIVE)
        btn.place(x=270 ,y=317)
        
        self.btnsub = Button(screen2, text="Order",font=('helvetica',13,'bold'),bg = "green",fg = "white",command = self.btn_sub,state = ACTIVE)
        self.btnsub.place(x = 320, y = 380)

    def payment(self):
        pym = self.strpym.get()
        
        if pym == 'Gopay' :
            Label(screen2, text='No Handphone\t\t:').place(x=30,y=347)
            self.entrynum = Entry(screen2, font = ("times new roman", 10))
            self.entrynum.place(x=140, y=347)
        elif pym == 'Dana':
            Label(screen2, text='No Handphone\t\t:').place(x=30,y=347)
            self.entrynum = Entry(screen2, font = ("times new roman", 10))
            self.entrynum.place(x=140, y= 347)
        elif pym == 'OVO':
            Label(screen2, text='No Handphone\t\t:').place(x=30,y=347)
            self.entrynum = Entry(screen2, font = ("times new roman", 10))
            self.entrynum.place(x=140, y= 347)
        elif pym == 'BRI':
            Label(screen2, text='No Rekening\t\t:').place(x=30,y=347)
            self.entrynum = Entry(screen2, font = ("times new roman", 10))
            self.entrynum.place(x=140, y= 347)
        else:
            Label(screen2, text ='No Rekening\t\t:').place(x=30, y= 347)
            self.entryrek = Entry(screen2, font=("times new roman", 10))
            self.entryrek.place(x=140, y=347)

    def btn_sub(self):
        name = self.entryID.get()
        kursi = self.radiochr.get()
        srv = self.radio.get()
        nom = self.radiobtn.get()
        pym = self.strpym.get()
        date = dt.datetime.now()
        
        if name == "" :
            msg.showwarning("Peringatan","Nama Tidak Boleh Kosong!",parent=self.gui)
            return
        if srv == 0:
            msg.showwarning("Peringatan","Genre Tidak Boleh Kosong!",parent=self.gui)
            return
        if nom == 0:
            msg.showwarning("Peringatan","Harap Pilih Nominal Tiket!",parent=self.gui)
            return
        if pym == "...":
            msg.showwarning("Peringatan","Harap Pilih Metode Pembayaran!",parent=self.gui)
            return
        else :
            msg.showinfo("Info Pesanan",f"Nama\t\t\t: {self.entryID.get()} \nKursi\t\t\t: {self.radiochr.get()} \nTanggal Pemesanan\t: {date:%A, %B %d, %Y} \nMetode Pembayaran\t: {self.strpym.get()} \nTotal Pembayaran\t\t: Rp.{self.radiobtn.get()},- \nStatus Pembayaran\t: Sukses!" )
            self.close_gui()

    def roman_srv(self):
        self.region = StringVar(value="...")
        self.region1 = ttk.Combobox(screen2,width=15,font=('times new romance',9),textvariable=self.region,state="readonly")
        self.region1.place(x=140, y=230)
        self.region1['values'] = ('A Whisker Away','Sweet And Sour','Josee, The Tiger and The Fish','Secret')
   
    def act_srv(self):
        self.region = StringVar(value="...")
        self.region1 = ttk.Combobox(screen2, width=15,font=('times new romance',9),textvariable=self.region,state="readonly")
        self.region1.place(x=140, y=230)
        self.region1['values'] = ('Doctor Strange in the Multiverse of Madness','Avengers: Endgame','Thor: Ragnarok','Black Panther')
    
    def hor_srv(self):
        self.region = StringVar(value="...")
        self.region1 = ttk.Combobox(screen2,width=15,font=('times new romance',9),textvariable=self.region,state="readonly")
        self.region1.place(x=140, y=230)
        self.region1['values'] = ('KKN di Desa Penari','Silent Hill')

    def seet(self):
        self.chair0 = StringVar(value="...")
        self.chair1 = ttk.Combobox(screen2,width=15,font=('times new romance',9),textvariable=self.chair0,state="readonly")
        self.chair1.place(x=140, y=140)
        self.chair1 ['values'] = ('1','2','3','4')
    
    def seet1(self):
        self.chair0 = StringVar(value="...")
        self.chair1 = ttk.Combobox(screen2, width=15,font=('times new romance',9),textvariable=self.chair0,state="readonly")
        self.chair1.place(x=140, y=140)
        self.chair1 ['values'] = ('1','2','3','4')
    def seet2(self):
        self.chair0 = StringVar(value="...")
        self.chair1 = ttk.Combobox(screen2,width=15,font=('times new romance',9),textvariable=self.chair0,state="readonly")
        self.chair1.place(x=140, y=140)
        self.chair1 ['values'] = ('1','2','3','4')

    def delete_data(self):
        self.entryUser.delete(0,END)
        self.entryPass.delete(0,END)
        self.entryUser.focus_set()
    
    def delete_uname(self): 
        self.entryPass.focus_set()
        self.entryUser.focus_set()
        self.entryUserName.delete(0,END)
        self.entryUserName.focus_set()
    
    def delete_email(self):
        self.entryUser.delete(0,END)
        self.entryPass.focus_set()
        self.entryUserName.focus_set()
        self.entryUser.focus_set()

    def delete_pass(self):
        self.entryPass.delete(0,END)
        self.entryUserName.focus_set()
        self.entryUser.focus_set()
        self.entryPass.focus_set()
        
    def close_gui(self):
        self.gui.destroy()

if __name__ == '__main__':
    global app
    app = Tk()
    logo = PhotoImage(file="Back1.png")
    app.iconphoto(True,logo)
    label = Label(app)
    bg = PhotoImage(file='Back.png')
    a_label = Label(app, image=bg)
    a_label.place(x=0, y=0, relheight=1, relwidth=1)
    start = Loginregisteruser(app,"CGV CINEMA")
    app.mainloop()
