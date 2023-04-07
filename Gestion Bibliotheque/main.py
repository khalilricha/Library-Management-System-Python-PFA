from tkinter import *
from tkinter import  ttk,messagebox
import pymysql
from pymysql import cursors

class Bibliotheque:
    def __init__(self,root):
        self.root=root
        self.root.title("Gestion de la bibliothèque")
        self.root.geometry("1080x720+0+0")

        #Les variables

        self.id= StringVar()
        self.titre=StringVar()
        self.AuteurLivre=StringVar()
        self.annee=StringVar()

        self.recherche_par=StringVar()
        self.recherche=StringVar()

        #Titre

        Gestion_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="gray")
        Gestion_Frame.place(x=50,y=150,width=400,height=500)

        Gestion_title=Label(Gestion_Frame,text="Informations du Livre",font=("Times New Roman",20,"bold"),bg="gray",fg="Yellow")
        Gestion_title.place(x=50,y=50)

        #Champ ID Livre

        idLivre=Label(Gestion_Frame, text="ID Livre :",font=("Times New Roman",20),bg="gray")
        idLivre.place(x=50,y=150)

        id_txt=Entry(Gestion_Frame,textvariable=self.id, font=("Times New Roman",20),bg="lightgray")
        id_txt.place(x=180,y=150,width=200)

        #Champ Titre
        titre = Label(Gestion_Frame, text="Titre :", font=("Times New Roman", 20), bg="gray")
        titre.place(x=50, y=220)

        titre_txt = Entry(Gestion_Frame,textvariable=self.titre, font=("Times New Roman", 20), bg="lightgray")
        titre_txt.place(x=180, y=220, width=200)
        #Champ Auteur
        AuteurLivre = Label(Gestion_Frame, text="Auteur :", font=("Times New Roman", 20), bg="gray")
        AuteurLivre.place(x=50, y=280)

        AuteurLivre_txt = Entry(Gestion_Frame,textvariable=self.AuteurLivre, font=("Times New Roman", 20), bg="lightgray")
        AuteurLivre_txt.place(x=180, y=280, width=200)
        #Champ Annee
        annee = Label(Gestion_Frame, text="Année :", font=("Times New Roman", 20), bg="gray")
        annee.place(x=50, y=350)

        annee_txt = Entry(Gestion_Frame,textvariable=self.annee, font=("Times New Roman", 20), bg="lightgray")
        annee_txt.place(x=180, y=350, width=200)

        #Boutton Ajouter
        btn_ajouter=Button(Gestion_Frame,text="Ajouter",font=("Times New Roman",12),relief=GROOVE,bg="green",command=self.ajout_livre)
        btn_ajouter.place(x=30,y=420)

        # Boutton Modifier
        btn_modifier = Button(Gestion_Frame, text="Modifier", font=("Times New Roman", 12), relief=GROOVE, bg="yellow",command=self.modifier)
        btn_modifier.place(x=100, y=420)

        # Boutton Supprimer
        btn_supprimer = Button(Gestion_Frame, text="Supprimer", font=("Times New Roman", 12), relief=GROOVE, bg="red",command=self.supprimer)
        btn_supprimer.place(x=170, y=420)

        # Boutton Réinitialiser
        btn_reinit = Button(Gestion_Frame, text="Réinitialiser", font=("Times New Roman", 12), relief=GROOVE, bg="lightgray",command=self.reinitialiser)
        btn_reinit.place(x=250, y=420)

        # Affichage
        details_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="gray")
        details_Frame.place(x=500, y=150, width=720, height=500)

        #Champ rechercher par
        affichage_resultat = Label(details_Frame, text="Rechercher par", font=("Times New Roman", 15, "bold"),bg="gray")
        affichage_resultat.place(x=50, y=50)

        rech=ttk.Combobox(details_Frame,textvariable=self.recherche_par, font=("Times New Roman",15),state="readonly")
        rech["values"]=("Titre","Auteur","Année")
        rech.place(x=200 ,y=55,width=200,height=30)

        #Champ recherche texte
        rech_txt=Entry(details_Frame,textvariable=self.recherche,font=("Times New Roman",15),bd=5,relief=GROOVE)
        rech_txt.place(x=420,y=55,width=250,height=30)

        #Bouton Rechercher
        btn_rech=Button(details_Frame,text="Rechercher",font=("Times New Roman",15),bg="lightgray")
        btn_rech.place(x=150,y=100,width=120,height=30)

        #Bouton Afficher Tout
        btn_affichtout = Button(details_Frame, text="Afficher Tout", font=("Times New Roman", 15),bg="lightgray",command=self.afficherResultat)
        btn_affichtout.place(x=350, y=100, width=120, height=30)

        #Affichage

        result_Frame=Frame(details_Frame,bd=5,relief=GROOVE,bg="lightgray")
        result_Frame.place(x=10,y=140,width=700,height=350)

        scroll_x=Scrollbar(result_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(result_Frame,orient=VERTICAL)
        self.tabl_resul=ttk.Treeview(result_Frame,columns=("ID","Titre","Auteur","Annee"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.tabl_resul.heading("ID",text="ID Livre")
        self.tabl_resul.heading("Titre", text="Titre")
        self.tabl_resul.heading("Auteur", text="Auteur")
        self.tabl_resul.heading("Annee", text="Année Publication")

        self.tabl_resul["show"]="headings"

        self.tabl_resul.column("ID", width=100)
        self.tabl_resul.column("Titre", width=150)
        self.tabl_resul.column("Auteur", width=150)
        self.tabl_resul.column("Annee", width=100)

        self.tabl_resul.pack()

        self.tabl_resul.bind("<ButtonRelease-1>",self.information)

        self.afficherResultat()
    #Fonctions d'ajout,modification,suppression et reinitialisation des livres
    def ajout_livre(self):
        if self.titre.get()=="":
            messagebox.showerror("Erreur","Titre Obligatoire")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="lbms")
            cur=con.cursor()
            cur.execute("INSERT INTO livres VALUES(%s,%s,%s,%s)",(self.id.get(),self.titre.get(),self.AuteurLivre.get(),self.annee.get()))
            con.commit()
            self.afficherResultat()
            con.close()
            messagebox.showinfo("Succés","Enregistrement effectué")
    def afficherResultat(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="lbms")
        cur=con.cursor()
        cur.execute("select * from livres")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.tabl_resul.delete(*self.tabl_resul.get_children())
            for row in rows:
                self.tabl_resul.insert("", END,values=row)
        con.commit()
        con.close()
    def reinitialiser(self):
        self.id.set("")
        self.titre.set("")
        self.AuteurLivre.set("")
        self.annee.set("")

    #Recuperer les valeurs de la ligne choisie dans les entrees du formulaire
    def information(self,ev):
        cursors_row=self.tabl_resul.focus()
        contents=self.tabl_resul.item(cursors_row)
        row=contents["values"]
        self.id.set(row[0])
        self.titre.set(row[1])
        self.AuteurLivre.set(row[2])
        self.annee.set(row[3])
    def modifier(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="lbms")
        cur = con.cursor()
        cur.execute("update livres set titre=%s,auteur=%s,annee=%s where id=%s",(self.titre.get(),self.AuteurLivre.get(),self.annee.get(),self.id.get()))
        con.commit()
        messagebox.showinfo("Succés","Modification effectuée")
        self.afficherResultat()
        self.reinitialiser()
        con.close()
    def supprimer(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="lbms")
        cur = con.cursor()
        cur.execute("delete from livres where id=%s",self.id.get())
        con.commit()
        self.afficherResultat()
        self.reinitialiser()
        con.close()
    def rechercher(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="lbms")
        cur = con.cursor()
        cur.execute("select * livres where"+str(self.recherche_par.get())+"LIKE '%"+str(self.recherche_par.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.tabl_resul.delete(*self.tabl_resul.get_children())
            for row in rows:
                self.tabl_resul.insert('',END,values=row)
        con.commit()
        con.close



root=Tk()
img=PhotoImage(file="libimg2.png")
Label(root,image=img).pack()
obj=Bibliotheque(root)
root.mainloop()