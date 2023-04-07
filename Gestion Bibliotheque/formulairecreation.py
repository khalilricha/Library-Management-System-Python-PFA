from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import os

class Formulaire:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1080x720")

        #champs du formulaire

        creation_frame=Frame(self.root,bg="grey")
        creation_frame.place(x=300,y=200, width=400, height=400)

        #Titre
        title=Label(creation_frame,text="Création de compte",font=("Times New Roman",20,"bold"),bg='grey',fg='Yellow').place(x=100,y=20)

        #Champs Username et password
        lbl_username=Label(creation_frame,text="Nom d'Utilisateur",font=("Times New Roman",10,"bold"),bg="yellow").place(x=120,y=100,width=200,height=50)
        lbl_password=Label(creation_frame,text="Mot de Passe",font=("Times New Roman",10,"bold"),bg="yellow").place(x=120,y=210,width=200,height=50)

        self.txt_username=Entry(creation_frame,font=("Times New Roman",10),bg="lightgray")
        self.txt_username.place(x=120,y=160,width=200,height=40)

        self.txt_password=Entry(creation_frame,show="*",font=("Times New Roman",10),bg="lightgray")
        self.txt_password.place(x=120,y=270,width=200,height=40)

        #Boutons Créer et Connexion
        create_btn = Button(creation_frame, text="Créer compte", cursor="hand2", font=("Times New Roman", 15), bd=0,bg="lightgray", fg="green",command=self.creer).place(x=50, y=345)
        connect_btn = Button(creation_frame, text="Connexion", cursor="hand2", font=("Times New Roman", 15), bd=0,bg="lightgray", fg="green", command=self.fenetre_login).place(x=250, y=345)

    #Fonction création compte
    def creer(self):
        if self.txt_username.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Erreur","Veuillez remplir tous les champs",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="creer")
                cur=con.cursor()
                cur.execute("insert into compte (username,password) values(%s,%s)",(self.txt_username.get(),self.txt_password.get()))
                messagebox.showinfo("Succés","Votre compte a été créé !",parent=self.root)
                con.commit()
                con.close()
            except Exception as es:
                messagebox.showerror("Erreur",f"Erreur de connexion:{str(es)}",parent=self.root)

    #Liaison avec la page de login
    def fenetre_login(self):
        self.root.destroy()
        import login



root = Tk()
img = PhotoImage(file="libimg2.png")
Label(root, image=img).pack()
obj = Formulaire(root)
root.mainloop()