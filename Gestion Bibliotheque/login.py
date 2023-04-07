from tkinter import *
from tkinter import ttk, messagebox
import pymysql

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1080x720")

        #Champs du formulaire
        login_frame=Frame(self.root,bg="grey")
        login_frame.place(x=300,y=200, width=400, height=400)

        #Titre
        title=Label(login_frame,text="Connexion",font=("Times New Roman",20,"bold"),bg='grey',fg='Yellow').place(x=145,y=10)

        #Champs Username et Password
        lbl_username=Label(login_frame,text="Nom d'Utilisateur",font=("Times New Roman",10,"bold"),bg="yellow").place(x=120,y=100,width=200,height=50)
        lbl_password=Label(login_frame,text="Mot de Passe",font=("Times New Roman",10,"bold"),bg="yellow").place(x=120,y=210,width=200,height=50)

        self.txt_username=Entry(login_frame,font=("Times New Roman",10),bg="lightgray")
        self.txt_username.place(x=120,y=160,width=200,height=40)

        self.txt_password=Entry(login_frame,show="*",font=("Times New Roman",10),bg="lightgray")
        self.txt_password.place(x=120,y=270,width=200,height=40)

        #Boutons Créer et Connexion
        creer_btn=Button(login_frame,text="Créer un nouveau compte",cursor="hand2",font=("Times New Roman",10),bd=0,bg="gray",fg="green",command=self.fenetre_formulaire).place(x=135,y=320)
        connect_btn = Button(login_frame, text="Connexion", cursor="hand2", font=("Times New Roman", 15), bd=0,bg="lightgray", fg="green",command=self.connexion).place(x=160, y=345)

    #Connexion avec la base de données
    def connexion(self):
        if self.txt_username.get()=="" or self.txt_password=="":
            messagebox.showerror("Erreur","Veuillez saisir les champs de connexion")
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="creer")
                cur = con.cursor()
                cur.execute("select * from compte where username=%s and password=%s",(self.txt_username.get(),self.txt_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Erreur","Identifiant ou mot de passe invalides",parent=self.root)
                else:
                    messagebox.showinfo("Succés","Bienvenu")
                    con.close()
            except Exception as ex:
                messagebox.showerror("Erreur",f"Erreur de connexion{str(ex)}",parent=self.root)
        self.root.destroy()
        import main

    #Liaison avec le formulaire de création de compte
    def fenetre_formulaire(self):
        self.root.destroy()
        import formulairecreation







root=Tk()
img=PhotoImage(file="libimg2.png")
Label(root,image=img).pack()
obj=Login(root)
root.mainloop()