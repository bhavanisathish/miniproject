# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 18:17:39 2020

pip install mysql-connector

@author: Bhavani
"""
import datetime
from tkinter import messagebox
import webbrowser
from openpyxl import Workbook
import os
import glob
from fpdf import FPDF
import tkinter as tk
import tkinter.ttk as ttk 
from ttkthemes import ThemedStyle
import mysql.connector
db_cur=mysql.connector.connect(host='localhost',user='root',passwd='',database='studentform')
db=db_cur.cursor()
class MyFirstGui(tk.Tk):
       def __init__(self):
                tk.Tk.__init__(self)
                self._frame = None
                
                self.switch_frame(StartPage)
                self.state("zoomed")
       
       def switch_frame(self, frame_class):
                new_frame = frame_class(self)
                if self._frame is not None:
                    self._frame.destroy()
                style = ThemedStyle(self)
                style.set_theme("plastik")
               
                style.configure('W.TButton', font =
                   ('calibri', 20, 'bold'))  
                style.configure('B.TButton', font =
                   ('calibri', 5, 'bold')) 
                style.configure('L.TButton', font =
                   ('calibri', 20, 'bold')) 
                self._frame = new_frame
                self._frame.pack()
                self.state("zoomed")
           
       
        
         
class StartPage(tk.Frame): 
           
      def __init__(self, master):
                    tk.Frame.__init__(self,master)
                    self.configure(background='powderblue')
                    
                    global username,passwords
                    self.l1=ttk.Label(self,text="Login here",font=("Times 40 italic"),background="powderblue")
                    self.l1.grid(row=3,column=1,columnspan=2,sticky='W',padx=10,pady=50)
                    self.l2=ttk.Label(self,text="Username",font=("Times 30 italic"),background="powderblue")
                    self.l2.grid(row=5,column=0,padx=10,pady=50)
                    self.password=ttk.Label(self,text="Password",font=("Times 30 italic"),background="powderblue")
                    self.password.grid(row=7,column=0,padx=10,pady=50)
                    self.e1=ttk.Entry(self,font=("Times 18 italic"))
                    self.e1.grid(row=5,column=2,padx=5,pady=5,ipady=5)
                    self.e2=ttk.Entry(self,font=("Times 18 italic"))
                    self.e2.grid(row=7,column=2,padx=5,pady=5,ipady=5)
                    self.b1=ttk.Button(self,text="SUBMIT",style = 'W.TButton',command=self.passd)
                    self.b1.grid(row=9,column=0,padx=30,pady=50)
                    self.b12=ttk.Button(self,text="Register",style = 'W.TButton',command=lambda: master.switch_frame(registration))
                    self.b12.grid(row=9,column=1,padx=30,pady=50)
                    self.b2=ttk.Button(self,text="RESET",style = 'W.TButton')
                    self.b2.grid(row=9,column=2,padx=30,pady=50)
                    
                    #self.button=tk.Button(self,text="->",width=10,command=lambda: master.switch_frame(pageOne))
                    #self.button.grid(row=4,column=0,sticky='W')
                    
            #self.ll1=tk.Button(self, text = 'Click Me !', image = photo1)
            #self.ll1.grid(row=4,column=0,sticky='W')
      def passd(self):
            self.username = self.e1.get()
            self.passwords = self.e2.get()
            db.execute("select *from adminlogin where name='%s' and password='%s'"%(self.username,self.passwords))
            l=db.fetchone()
            if(l):
                print("check")
                #self.switch_frame(pageOne)
                MyFirstGui().switch_frame(pageOne)
                db_cur.commit()
            else:
                 messagebox.showinfo("SIGN IN ERROE", "PLEASE ENTER A VALID USERNAME OR PASSWORD")


class registration(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.configure(background='powderblue')
        self.lb1=ttk.Label(self,text="Register here",font=("Times 40 italic"),background="powderblue")
        self.lb1.grid(row=0,column=0,padx=10,pady=30)
        self.lb2=ttk.Label(self,text="Name",font=("Times 18 italic"),background="powderblue")
        self.lb2.grid(row=1,column=0,padx=10,pady=30)
        self.ent1=ttk.Entry(self,font=("Times 18 italic"))
        self.ent1.grid(row=1,column=1,padx=5,pady=5,ipady=5)
        self.lb3=ttk.Label(self,text="Password",font=("Times 18 italic"),background="powderblue")
        self.lb3.grid(row=2,column=0,padx=10,pady=30)
        self.ent2=ttk.Entry(self,font=("Times 18 italic"))
        self.ent2.grid(row=2,column=1,padx=5,pady=5,ipady=5)
        self.lb4=ttk.Label(self,text="Department",font=("Times 18 italic"),background="powderblue")
        self.lb4.grid(row=3,column=0,padx=10,pady=30)
        self.ent3=ttk.Entry(self,font=("Times 18 italic"))
        self.ent3.grid(row=3,column=1,padx=5,pady=5,ipady=5)
        self.lb5=ttk.Label(self,text="Posting",font=("Times 18 italic"),background="powderblue")
        self.lb5.grid(row=4,column=0,padx=10,pady=30)
        self.ent4=ttk.Entry(self,font=("Times 18 italic"))
        self.ent4.grid(row=4,column=1,padx=5,pady=5,ipady=5)
        self.bt1=ttk.Button(self,text="Register",command=self.regg)
        self.bt1.grid(row=5,column=0,sticky='S',padx=10,pady=30)
       
        self.bt2=ttk.Button(self,text="RESET")
        self.bt2.grid(row=5,column=2,padx=30,pady=50)
    def regg(self):
        self.namee=self.ent1.get()
        self.passsword=self.ent2.get()
        self.depart=self.ent3.get()
        self.post=self.ent4.get()
        sql1="INSERT INTO `adminlogin`(`name`, `password`, `department`, `posting`) VALUES(%s,%s,%s,%s)"
        val1=(self.namee,self.passsword,self.depart,self.post)
        db.execute(sql1, val1)
        db_cur.commit()
        MyFirstGui().switch_frame(StartPage)
        


       
class pageOne(tk.Frame):
      def __init__(self,master):
             tk.Frame.__init__(self,master)
             self.configure(background='powderblue')
             lable1=ttk.Label(self,text="Start page",font=("Times 30 italic"),background="powderblue")
             lable1.grid(row=0,column=1,padx=10,pady=90)
             bb1=ttk.Button(self,text="TC generation",style = 'L.TButton',command=lambda: master.switch_frame(transferspecify))
             bb1.grid(row=1,column=1,sticky='W')
            
             bb2=ttk.Button(self,text="Edit",style = 'L.TButton',command=lambda: master.switch_frame(editspecify))
             bb2.grid(row=3,column=1,sticky='W',pady=50)
             bb4=ttk.Button(self,text="Insert Record",style = 'L.TButton',command=lambda: master.switch_frame(newreg))
             bb4.grid(row=4,column=1,sticky='W',pady=30)
             
             bb3=ttk.Button(self,text="Search",style = 'L.TButton',command=lambda: master.switch_frame(search))
             bb3.grid(row=5,column=1,sticky='W',pady=30)
             
             self.button11=ttk.Button(self,text="<-",style = 'B.TButton',command=lambda: master.switch_frame(StartPage))
             self.button11.grid(row=0,column=0,sticky='W')
        
class transferspecify(tk.Frame):
      def __init__(self, master):
             tk.Frame.__init__(self,master)
             self.configure(background='powderblue')
             lablle1=ttk.Label(self,text="Certificate",font=("Times 30 italic"),background="powderblue")
             lablle1.grid(row=0,column=1,sticky='NSWE',padx=10,pady=90)
             button=ttk.Button(self,text="Individual Transfer Certificate",style = 'W.TButton',command=lambda: master.switch_frame(transfersingle))
             button.grid(row=1,column=1,sticky='W')
             ll=ttk.Label(self)
             ll.grid(row=2,column=1,padx=10,pady=80)
             Button1=ttk.Button(self,text="Batch Transfer Certificate",style = 'W.TButton',command=lambda: master.switch_frame(transfergroup))
             Button1.grid(row=2,column=1,sticky='W')
             
             self.button13=ttk.Button(self,text="<-",style = 'B.TButton',command=lambda: master.switch_frame(pageOne))
             self.button13.grid(row=3,column=0,sticky='W')
         
class transfergroup(tk.Frame):
        def __init__(self, master):
                tk.Frame.__init__(self,master)
                self.configure(background='powderblue')
                l=ttk.Label(self,text="Enter the Details",font=("Times 30 italic"),background="powderblue")
                l.grid(row=0,padx=10,pady=70)
                
                l1=ttk.Label(self,text="Batch",bg="powderblue",font=("Times 30 italic"),background="powderblue")
                l1.grid(row=1,column=0,padx=10,pady=50,sticky='W')
                e1=ttk.Entry(self,font=("Times 18 italic"))
                e1.grid(row=1,column=2,sticky='W',padx=5,pady=5,ipady=5)
                l2=ttk.Label(self,text="Leaving Date",bg="powderblue",font=("Times 30 italic"),background="powderblue")
                l2.grid(row=2,column=0,padx=10,pady=50,sticky='W')
                e2=ttk.Entry(self,font=("Times 18 italic"))
                e2.grid(row=2,column=2,padx=5,pady=5,ipady=5,sticky='W')
                
                but=ttk.Button(self,text="Submit",style = 'W.TButton')
                but.grid(row=3,column=2,padx=10,pady=50,sticky='E')
                
                button15=ttk.Button(self,text="<-",style = 'B.TButton',command=lambda: master.switch_frame(transferspecify))
                button15.grid(row=4,column=0,sticky='W')
            
            
            
class transfersingle(tk.Frame):
          
          def __init__(self, master):
                tk.Frame.__init__(self,master)
                self.configure(background='powderblue')
                self.l=ttk.Label(self,text="Enter the Details",font=("Times 30 italic"),background="powderblue")
                self.l.grid(row=0,padx=10,pady=70)
                
                self.l1=ttk.Label(self,text="Reg No",font=("Times 30 italic"),background="powderblue")
                self.l1.grid(row=1,column=0,padx=10,pady=50,sticky='W')
                self.entr1=ttk.Entry(self,font=("Times 18 italic"))
                self.entr1.grid(row=1,column=2,padx=5,pady=5,ipady=5,sticky='W')
                self.l2=ttk.Label(self,text="Leaving Date",font=("Times 30 italic"),background="powderblue")
                self.l2.grid(row=2,column=0,padx=10,pady=50,sticky='W')
                self.e2=ttk.Entry(self,font=("Times 18 italic"))
                self.e2.grid(row=2,column=2,padx=5,pady=5,ipady=5,sticky='W')
                #print(entr1.get())
                self.but=ttk.Button(self,text="Submit",style = 'W.TButton',command=self.tranz)
                self.but.grid(row=3,column=2,padx=10,pady=50,sticky='E')
              
                self.button16=ttk.Button(self,text="<-",style = 'B.TButton',command=lambda: master.switch_frame(transferspecify))
                self.button16.grid(row=4,column=0,sticky='W')
          def tranz(self):
              global setentvar,sete2var
              setentvar=self.entr1.get()
              sete2var=self.e2.get()
              MyFirstGui().switch_frame(transferCertificate)
                
          
           
class transferCertificate(tk.Frame):
            
   def __init__(self, master):
                tk.Frame.__init__(self,master)
                self.configure(background='powderblue')
                db.execute("select *from studentdetails where reg_number=%s"%(setentvar))
                f=db.fetchone()
                if(f):
                    print("ok")
                Labe=ttk.Label(self,text="TRANSFER CERTIFICATE",font=("Times 30 italic"),background="powderblue")
                Labe.grid(row=2,sticky='NSWE',pady=15)
                lab=ttk.Label(self,text="SI.NO :",font=("Times 30 italic"),background="powderblue")
                lab.grid(row=3,column=0,sticky='W',pady=15)
                la=ttk.Label(self,text="ROLL NO",font=("Times 30 italic"),background="powderblue")
                la.grid(row=3,column=3,sticky='W',pady=15)
                
                
                
                l1=ttk.Label(self,text="1.  Name of the student",font=("Times 30 italic"),background="powderblue")
                l1.grid(row=4,column=0,sticky='W',pady=7)
                s1=ttk.Label(self,text=" : ",background="powderblue")
                s1.grid(row=4,column=1,sticky='W',pady=7)
                a1=ttk.Label(self,text=f[0],font=("Times 30 italic"),background="powderblue")
                a1.grid(row=4,column=2,sticky='W',pady=7)
                
                l2=ttk.Label(self,text="2.  Name of the parent/Guardian",font=("Times 30 italic"),background="powderblue")
                l2.grid(row=5,column=0,sticky='W',pady=7)
                s2=ttk.Label(self,text=" : ",background="powderblue")
                s2.grid(row=5,column=1,sticky='W',pady=7)
                a2=ttk.Label(self,text=f[3],font=("Times 30 italic"),background="powderblue")
                a2.grid(row=5,column=2,sticky='W',pady=7)
                
                l3=ttk.Label(self,text="3.  Nationality Religion and coommunity",font=("Times 30 italic"),background="powderblue")
                l3.grid(row=6,column=0,sticky='W',pady=7)
                s3=ttk.Label(self,text=" : ",background="powderblue")
                s3.grid(row=6,column=1,sticky='W',pady=7)
                a3=ttk.Label(self,text=f[4]+"  "+f[5]+"  "+f[7],font=("Times 30 italic"),background="powderblue")
                a3.grid(row=6,column=2,sticky='W',pady=7)
                
                l4=ttk.Label(self,text="4.  Sex",font=("Times 30 italic"),background="powderblue")
                l4.grid(row=7,column=0,sticky='W',pady=7)
                s4=ttk.Label(self,text=" : ",background="powderblue")
                s4.grid(row=7,column=1,sticky='W',pady=7)
                a4=ttk.Label(self,text=f[8],font=("Times 30 italic"),background="powderblue")
                a4.grid(row=7,column=2,sticky='W',pady=7)
                
                l5=ttk.Label(self,text="5.  Date of Birth (in figure and words) as entered in the admission register",font=("Times 30 italic"),background="powderblue")
                l5.grid(row=8,column=0,sticky='W',pady=7)
                s5=ttk.Label(self,text=" : ",background="powderblue")
                s5.grid(row=8,column=1,sticky='W',pady=7)
                a5=ttk.Label(self,text=f[9],font=("Times 30 italic"),background="powderblue")
                a5.grid(row=8,column=2,sticky='W',pady=7)
                
                l6=ttk.Label(self,text="6.  Course of Study",font=("Times 30 italic"),background="powderblue")
                l6.grid(row=9,column=0,sticky='W',pady=7)
                s6=ttk.Label(self,text=" : ",background="powderblue")
                s6.grid(row=9,column=1,sticky='W',pady=7)
                a6=ttk.Label(self,text=f[10],font=("Times 30 italic"),background="powderblue")
                a6.grid(row=9,column=2,sticky='W',pady=7)
                
                l7=ttk.Label(self,text="7.  Date of Admission to this college",font=("Times 30 italic"),background="powderblue")
                l7.grid(row=10,column=0,sticky='W',pady=7)
                s7=ttk.Label(self,text=" : ",background="powderblue")
                s7.grid(row=10,column=1,sticky='W',pady=7)
                a7=ttk.Label(self,text=f[12],font=("Times 30 italic"),background="powderblue")
                a7.grid(row=10,column=2,sticky='W',pady=7)
                
                l8=ttk.Label(self,text="8.  a) Whether the Student has paid all the Fees due to the college ?",font=("Times 30 italic"),background="powderblue")
                l8.grid(row=11,column=0,sticky='W',pady=7)
                s8=ttk.Label(self,text=" : ",background="powderblue")
                s8.grid(row=11,column=1,sticky='W',pady=7)
                a8=ttk.Label(self,text="",font=("Times 30 italic"),background="powderblue")
                a8.grid(row=11,column=2,sticky='W',pady=7)
                
                l9=ttk.Label(self,text="8.  b) Whether the Student was in receipt of any scholarship",font=("Times 30 italic"),background="powderblue")
                l9.grid(row=12,column=0,sticky='W',pady=7)
                s9=ttk.Label(self,text=" : ",background="powderblue")
                s9.grid(row=12,column=1,sticky='W',pady=7)
                a9=ttk.Label(self,text="",font=("Times 30 italic"),background="powderblue")
                a9.grid(row=12,column=2,sticky='W',pady=7)
                
                l10=ttk.Label(self,text="9.  Whether the Student has undergone Medical inspection during the year",font=("Times 30 italic"),background="powderblue")
                l10.grid(row=13,column=0,sticky='W',pady=7)
                s10=ttk.Label(self,text=" : ",background="powderblue")
                s10.grid(row=13,column=1,sticky='W',pady=7)
                a10=ttk.Label(self,text="",font=("Times 30 italic"),background="powderblue")
                a10.grid(row=13,column=2,sticky='W',pady=7)
                
                l11=ttk.Label(self,text="10.  Reasons for leaving the College",font=("Times 30 italic"),background="powderblue")
                l11.grid(row=14,column=0,sticky='W',pady=7)
                s11=ttk.Label(self,text=" : ",background="powderblue")
                s11.grid(row=14,column=1,sticky='W',pady=7)
                a11=ttk.Label(self,text="",font=("Times 30 italic"),background="powderblue")
                a11.grid(row=14,column=2,sticky='W',pady=7)
                
                l12=ttk.Label(self,text="11.  Date of Leaving",font=("Times 30 italic"),background="powderblue")
                l12.grid(row=15,column=0,sticky='W',pady=7)
                s12=ttk.Label(self,text=" : ",background="powderblue")
                s12.grid(row=15,column=1,sticky='W',pady=7)
                a12=ttk.Label(self,text=sete2var,font=("Times 30 italic"),background="powderblue")
                a12.grid(row=15,column=2,sticky='W',pady=7)
                
                l13=ttk.Label(self,text="12.  Date on which application for Transfer Certificate was made by the Student or On his/her behalf by Parent/Guardian",font=("Times 30 italic"),background="powderblue")
                l13.grid(row=16,column=0,sticky='W',pady=7)
                s13=ttk.Label(self,text=" : ",background="powderblue")
                s13.grid(row=16,column=1,sticky='W',pady=7)
                a13=ttk.Label(self,text="",font=("Times 30 italic"),background="powderblue")
                a13.grid(row=16,column=2,sticky='W',pady=7)
                
                l14=ttk.Label(self,text="13.  Date of the Transfer Certificate",font=("Times 30 italic"),background="powderblue")
                l14.grid(row=17,column=0,sticky='W',pady=7)
                s14=ttk.Label(self,text=" : ",background="powderblue")
                s14.grid(row=17,column=1,sticky='W',pady=7)
                a14=ttk.Label(self,text="",font=("Times 30 italic"),background="powderblue")
                a14.grid(row=17,column=2,sticky='W',pady=7)
                
                l15=ttk.Label(self,text="14.  MEDIUM",font=("Times 30 italic"),background="powderblue")
                l15.grid(row=18,column=0,sticky='W',pady=7)
                s15=ttk.Label(self,text=" : ",background="powderblue")
                s15.grid(row=18,column=1,sticky='W',pady=7)
                a15=ttk.Label(self,text="ENGLISH",font=("Times 30 italic"),background="powderblue")
                a15.grid(row=18,column=2,sticky='W',pady=7)
                
                l16=ttk.Label(self,text="SEAL",font=("Times 30 italic"),background="powderblue")
                l16.grid(row=19,column=0,sticky='W',pady=7)
                s16=ttk.Label(self,text=" : ",background="powderblue")
                s16.grid(row=19,column=1,sticky='W',pady=7)
                a16=ttk.Label(self,text="",font=("Times 30 italic"),background="powderblue")
                a16.grid(row=19,column=2,sticky='W',pady=7)
                buttt=ttk.Button(self,text="print",style = 'W.TButton',command=self.printpdf)
                buttt.grid(row=20,column=1,sticky='W',pady=7)
                button17=ttk.Button(self,text="<-",style = 'B.TButton',command=lambda: master.switch_frame(transfersingle))
                button17.grid(row=20,column=0,sticky='W',pady=7)
                        
   def printpdf(self):
         
                db.execute("select *from studentdetails where reg_number=%s"%(setentvar))
                f=db.fetchone()
                reg=setentvar
                
                pdf=FPDF()
                pdf.add_page()
                pdf.set_font("Arial",size=12)
                pdf.cell(100,10,txt="ALAGAPPA CHETTIAR GOVERNMENT COLLEGE OF ENGINEERING AND TECHNOLOGY")
                pdf.ln(10)
                pdf.cell(100,10,txt="                                      TRANSFER CERTIFICATE")
                pdf.ln(10)
                pdf.cell(100,10,txt="1.  Name of the student")
                pdf.cell(100,10,txt=str(f[0]))
                pdf.ln(10)
                pdf.cell(100,10,txt="2.  Name of the parent/Guardian")
                pdf.cell(100,10,txt=str(f[3]))
                pdf.ln(10)
                pdf.cell(100,10,txt="3.  Nationality Religion and coommunity")
                pdf.cell(100,10,txt=str(f[6]))
                pdf.ln(10)
                pdf.cell(100,10,txt="4.  Sex")
                pdf.cell(100,10,txt=str(f[8]))
                pdf.ln(10)
                pdf.cell(100,10,txt="5.  Date of Birth (in figure and words) ")
                pdf.cell(100,10,txt=str(f[9]))
                pdf.ln(10)
                pdf.cell(100,10,txt="as entered in the admission register")
                pdf.ln(10)
                pdf.cell(100,10,txt="6.  Course of Study")
                pdf.cell(100,10,txt=str(f[10]))
                pdf.ln(10)
                pdf.cell(100,10,txt="7.  Date of Admission to this college")
                pdf.cell(100,10,txt=str(f[12]))
                pdf.ln(10)
                pdf.cell(100,10,txt="8.  a) Whether the Student has paid all the  ")
                pdf.cell(100,10,txt="")
                pdf.ln(10)
                pdf.cell(100,10,txt="Fees due to the college ?")
                pdf.ln(10)
                pdf.cell(100,10,txt="8.  b) Whether the Student was in receipt of ")
                pdf.cell(100,10,txt="")
                pdf.ln(10)
                pdf.cell(100,10,txt="any scholarship")
                pdf.ln(10)
                pdf.cell(100,10,txt="9.  Whether the Student has undergone ")
                
                pdf.cell(100,10,txt="")
                pdf.ln(10)
                pdf.cell(100,10,txt="Medical inspection during the year")
                pdf.ln(10)
                pdf.cell(100,10,txt="10.  Reasons for leaving the College")
                
                pdf.cell(100,10,txt="")
                pdf.ln(10)
                pdf.cell(100,10,txt="11.  Date of Leaving")
                pdf.cell(100,10,txt="")
                pdf.ln(10)
                pdf.cell(100,10,txt="12.  Date on which application for Transfer  ")
                pdf.cell(100,10,txt="")
                pdf.ln(10)
                pdf.cell(100,10,txt="Certificate was made by the Student or On his/her")
                pdf.ln(10)
                pdf.cell(100,10,txt="behalf by Parent/Guardian")
                pdf.ln(10)
                pdf.cell(100,10,txt="13.  Date of the Transfer Certificate")
                pdf.cell(100,10,txt=str(f[23]))
                pdf.ln(10)
                pdf.cell(100,10,txt="14.  MEDIUM")
                pdf.cell(100,10,txt="English")
                pdf.ln(10)
                pdf.cell(100,10,txt="Seal")
                pdf.cell(100,10,txt="")
                pdf.ln(10)
                r=reg+".pdf"
                pdf.output(r)
                if os.path.exists(r):
                           os.startfile(r)


class editspecify(tk.Frame):
      def __init__(self, master):
             tk.Frame.__init__(self,master)
             self.configure(background='powderblue')
             lablle1=ttk.Label(self,text="Certificate",font=("Times 30 italic"),background="powderblue")
             lablle1.grid(row=0,column=0,sticky='NSWE',pady=50)
             lp=ttk.Label(self,text="Enter the Register number",font=("Times 30 italic"),background="powderblue")
             lp.grid(row=1,column=0,sticky='NSWE',pady=30)
             self.ent=ttk.Entry(self,font=("Times 18 italic"))
             self.ent.grid(row=2,column=0,sticky='NSWE',padx=5,pady=5,ipady=5)
             buton1=ttk.Button(self,text="submit",style = 'W.TButton',command=self.editz)
             buton1.grid(row=3,column=1,sticky='W')
             
             button18=ttk.Button(self,text="<-",style = 'B.TButton',command=lambda: master.switch_frame(pageOne))
             button18.grid(row=4,column=0,sticky='W',pady=30)
      def editz(self):
          global setvar
          setvar=self.ent.get()
          MyFirstGui().switch_frame(edit)
          
                                                     
class edit(tk.Frame):
              def __init__(self, master):
                    tk.Frame.__init__(self, master)
                    def Validate():
                        date_format = '%Y-%m-%d'
                        rule = re.compile(r'(^[+0-9]{1,3})*([0-9]{10,11}$)')
                        if not rule.search(self.ea22.get()):
                            messagebox.showinfo("INVALID MOBILE NUMBER", "PLEASE ENTER A VALID MOBILE NUMBER")
                        try:
                            date_obj = datetime.datetime.strptime(self.e10.get(), date_format)
                        except ValueError:
                          messagebox.showinfo("INVALID DATE FORMAT", "PLEASE ENTER A VALID DATE OF BIRTH('%Y-%m-%d')")   
                        try:
                            date_obj = datetime.datetime.strptime(self.e13.get(), date_format)
                        except ValueError:
                          messagebox.showinfo("INVALID DATE FORMAT", "PLEASE ENTER A VALID ADMISSION ('%Y-%m-%d')")   
                        try:
                            date_obj = datetime.datetime.strptime(self.e15.get(), date_format)
                        except ValueError:
                          messagebox.showinfo("INVALID DATE FORMAT", "PLEASE ENTER A VALID RECEIPT DATE('%Y-%m-%d')")   
                        try:
                            date_obj = datetime.datetime.strptime(self.ea25.get(), date_format)
                        except ValueError:
                          messagebox.showinfo("INVALID DATE FORMAT", "PLEASE ENTER A VALID ISSUED ON DATE('%Y-%m-%d')")   
                        
                    #self._rootwindow.bind('<Configure>', self.onResize)
                    self.configure(background='powderblue')
                    db.execute("select *from studentdetails where reg_number='%s'"%(setvar))
                    e=db.fetchone()
                    self.labe=ttk.Label(self,text="EDIT",font=("Times 10 italic"),background="powderblue")
                    self.labe.grid(row=0,column=0,sticky='W')
                    
                    self.l1=ttk.Label(self,text="Name Of The Candidate",font=("Times 10 italic"),background="powderblue")
                    self.l1.grid(row=1,column=0,sticky='W',pady=5)
                    self.ll1=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll1.grid(row=1,column=1,sticky='W',pady=5)
                    self.e1=ttk.Entry(self,font=("Times 10 italic"))
                    self.e1.grid(row=1,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e1.insert(0,e[0])
                    self.l2=ttk.Label(self,text="Reg Number",font=("Times 10 italic"),background="powderblue")
                    self.l2.grid(row=2,column=0,sticky='W',pady=5)
                    self.ll2=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll2.grid(row=2,column=1,sticky='W',pady=5)
                    self.e2=ttk.Entry(self,font=("Times 10 italic"),text="crazy")
                    self.e2.grid(row=2,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e2.insert(0,e[1])
                    
                    self.l3=ttk.Label(self,text="Roll Number",font=("Times 10 italic"),background="powderblue")
                    self.l3.grid(row=3,column=0,sticky='W',pady=5)
                    self.ll3=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll3.grid(row=3,column=1,sticky='W',pady=5)
                    self.e3=ttk.Entry(self,font=("Times 10 italic"))
                    self.e3.grid(row=3,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e3.insert(0,e[2])
                    self.l4=ttk.Label(self,text="Father's Name",font=("Times 10 italic"),background="powderblue")
                    self.l4.grid(row=4,column=0,sticky='W',pady=5)
                    self.ll4=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll4.grid(row=4,column=1,sticky='W',pady=5)
                    self.e4=ttk.Entry(self,font=("Times 10 italic"))
                    self.e4.grid(row=4,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e4.insert(0,e[3])
                    self.l5=ttk.Label(self,text="Nationality",font=("Times 10 italic"),background="powderblue")
                    self.l5.grid(row=5,column=0,sticky='W',pady=5)
                    self.ll5=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll5.grid(row=5,column=1,sticky='W',pady=5)
                    self.e5=ttk.Entry(self,font=("Times 10 italic"))
                    self.e5.grid(row=5,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e5.insert(0,e[4])
                    self.l6=ttk.Label(self,text="Religion",font=("Times 10 italic"),background="powderblue")
                    self.l6.grid(row=6,column=0,sticky='W',pady=5)
                    self.ll6=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll6.grid(row=6,column=1,sticky='W',pady=5)
                    self.e6=ttk.Entry(self,font=("Times 10 italic"))
                    self.e6.grid(row=6,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e6.insert(0,e[5])
                    self.l7=ttk.Label(self,text="Caste",font=("Times 10 italic"),background="powderblue")
                    self.l7.grid(row=7,column=0,sticky='W',pady=5)
                    self.ll7=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll7.grid(row=7,column=1,sticky='W',pady=5)
                    self.e7=ttk.Entry(self,font=("Times 10 italic"))
                    self.e7.grid(row=7,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e7.insert(0,e[6])
                    self.l8=ttk.Label(self,text="Community",font=("Times 10 italic"),background="powderblue")
                    self.l8.grid(row=8,column=0,sticky='W',pady=5)
                    self.ll8=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll8.grid(row=8,column=1,sticky='W',pady=5)
                    self.e8=ttk.Entry(self,font=("Times 10 italic"))
                    self.e8.grid(row=8,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e8.insert(0,e[7])
                    self.l9=ttk.Label(self,text="Sex",font=("Times 10 italic"),background="powderblue")
                    self.l9.grid(row=9,column=0,sticky='W',pady=5)
                    self.ll9=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll9.grid(row=9,column=1,sticky='W',pady=5)
                    self.e9=ttk.Entry(self,font=("Times 10 italic"))
                    self.e9.grid(row=9,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e9.insert(0,e[8])
                    self.l10=ttk.Label(self,text="Date Of Birth",font=("Times 10 italic"),background="powderblue")
                    self.l10.grid(row=10,column=0,sticky='W',pady=5)
                    self.ll10=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll10.grid(row=10,column=1,sticky='W',pady=5)
                    self.e10=ttk.Entry(self,font=("Times 10 italic"))
                    self.e10.grid(row=10,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e10.insert(0,e[9])
                    self.l11=ttk.Label(self,text="Course Of Study",font=("Times 10 italic"),background="powderblue")
                    self.l11.grid(row=11,column=0,sticky='W',pady=5)
                    self.ll11=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll11.grid(row=11,column=1,sticky='W',pady=5)
                    self.e11=ttk.Entry(self,font=("Times 10 italic"))
                    self.e11.grid(row=11,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e11.insert(0,e[10])
                    self.l12=ttk.Label(self,text="Branch Of Study",font=("Times 10 italic"),background="powderblue")
                    self.l12.grid(row=12,column=0,sticky='W',pady=5)
                    self.ll12=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll12.grid(row=12,column=1,sticky='W',pady=5)
                    self.e12=ttk.Entry(self,font=("Times 10 italic"))
                    self.e12.grid(row=12,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e12.insert(0,e[11])
                    self.l13=ttk.Label(self,text=" Admitted On",font=("Times 10 italic"),background="powderblue")
                    self.l13.grid(row=13,column=0,sticky='W',pady=5)
                    self.ll13=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll13.grid(row=13,column=1,sticky='W',pady=5)
                    self.e13=ttk.Entry(self,font=("Times 10 italic"))
                    self.e13.grid(row=13,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e13.insert(0,e[12])
                    self.l14=ttk.Label(self,text="Receipt Number",font=("Times 10 italic"),background="powderblue")
                    self.l14.grid(row=14,column=0,sticky='W',pady=5)
                    self.ll14=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll14.grid(row=14,column=1,sticky='W',pady=5)
                    self.e14=ttk.Entry(self,font=("Times 10 italic"))
                    self.e14.grid(row=14,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e14.insert(0,e[13])
                    self.l15=ttk.Label(self,text="Receipt Date",font=("Times 10 italic"),background="powderblue")
                    self.l15.grid(row=15,column=0,sticky='W',pady=5)
                    self.ll15=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll15.grid(row=15,column=1,sticky='W',pady=5)
                    self.e15=ttk.Entry(self,font=("Times 10 italic"))
                    self.e15.grid(row=15,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e15.insert(0,e[14])
                    self.l16=ttk.Label(self,text="Mother Tongue",font=("Times 10 italic"),background="powderblue")
                    self.l16.grid(row=16,column=0,sticky='W',pady=5)
                    self.ll16=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll16.grid(row=16,column=1,sticky='W',pady=5)
                    self.e16=ttk.Entry(self,font=("Times 10 italic"))
                    self.e16.grid(row=16,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e16.insert(0,e[15])
                    self.l17=ttk.Label(self,text="Name Of State",font=("Times 10 italic"),background="powderblue")
                    self.l17.grid(row=17,column=0,sticky='W',pady=5)
                    self.ll17=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll17.grid(row=17,column=1,sticky='W',pady=5)
                    self.e17=ttk.Entry(self,font=("Times 10 italic"))
                    self.e17.grid(row=17,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e17.insert(0,e[16])
                    self.l18=ttk.Label(self,text="Present address ",font=("Times 10 italic"),background="powderblue")
                    self.l18.grid(row=18,column=0,sticky='W',pady=5)
                    self.ll18=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll18.grid(row=18,column=1,sticky='W',pady=5,padx=30)
                    self.e18=ttk.Entry(self,font=("Times 10 italic"))
                    self.e18.grid(row=18,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e18.insert(0,e[17])
                    self.l19=ttk.Label(self,text="Taluk ",font=("Times 10 italic"),background="powderblue")
                    self.l19.grid(row=19,column=0,sticky='W',pady=5)
                    self.ll19=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll19.grid(row=19,column=1,sticky='W',pady=5)
                    self.e19=ttk.Entry(self,font=("Times 10 italic"))
                    self.e19.grid(row=19,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e19.insert(0,e[18])
                    self.l20=ttk.Label(self,text="City",font=("Times 10 italic"),background="powderblue")
                    self.l20.grid(row=20,column=0,sticky='W',pady=5)
                    self.ll20=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll20.grid(row=20,column=1,sticky='W',pady=5)
                    self.e20=ttk.Entry(self,font=("Times 10 italic"))
                    self.e20.grid(row=20,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e20.insert(0,e[19])
                    self.l21=ttk.Label(self,text="District",font=("Times 10 italic"),background="powderblue")
                    self.l21.grid(row=21,column=0,sticky='W',pady=5)
                    self.ll21=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.ll21.grid(row=21,column=1,sticky='W',pady=5)
                    self.e21=ttk.Entry(self,font=("Times 10 italic"))
                    self.e21.grid(row=21,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e21.insert(0,e[20])
                    self.la22=ttk.Label(self,text="Cell Number",font=("Times 10 italic"),background="powderblue")
                    self.la22.grid(row=22,column=0,sticky='W',pady=5)
                    self.lla22=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.lla22.grid(row=22,column=1,sticky='W',pady=5)
                    self.ea22=ttk.Entry(self,font=("Times 10 italic"))
                    self.ea22.grid(row=22,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.ea22.insert(0,e[21])
                    self.la23=ttk.Label(self,text="Aadhar Number",font=("Times 10 italic"),background="powderblue")
                    self.la23.grid(row=23,column=0,sticky='W',pady=5)
                    self.lla23=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.lla23.grid(row=23,column=1,sticky='W',pady=5)
                    self.ea23=ttk.Entry(self,font=("Times 10 italic"))
                    self.ea23.grid(row=23,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.ea23.insert(0,e[22])
                     
                    self.la24=ttk.Label(self,text="T.C.No",font=("Times 10 italic"),background="powderblue")
                    self.la24.grid(row=24,column=0,sticky='W',pady=5)
                    self.lla24=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.lla24.grid(row=24,column=1,sticky='W',pady=5)
                    self.ea24=ttk.Entry(self,font=("Times 10 italic"))
                    self.ea24.grid(row=24,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.ea24.insert(0,e[23]) 
                    self.la25=ttk.Label(self,text=" Issued ON",font=("Times 10 italic"),background="powderblue")
                    self.la25.grid(row=25,column=0,sticky='W',pady=5)
                    self.lla25=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                    self.lla25.grid(row=25,column=1,sticky='W',pady=5)
                    self.ea25=ttk.Entry(self,font=("Times 10 italic"))
                    self.ea25.grid(row=25,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.ea25.insert(0,e[24])
                    self.llla24=ttk.Button(self,style = 'W.TButton',text="SUBMIT",command=self.callme)
                    self.llla24.grid(row=26,column=2,sticky='E',pady=5)
                    self.button19=ttk.Button(self,text="<-",style = 'B.TButton',command=lambda: master.switch_frame(transferspecify))
                    self.button19.grid(row=26,column=0,sticky='W',pady=5)
                    
                    #button19=tk.Button(self,text="<-",style = 'B.TButton',command=lambda: master.switch_frame(editspecify))
                    #button19.grid(row=23,column=0,sticky='W')
                    self.llla24.configure(command=Validate)
    
                    print(self.e1.get())

              def callme(self):
                        sql="UPDATE `studentdetails` SET `name`=%s,`father_name`=%s,`nationality`=%s,`religion`=%s,`caste`=%s,`community`=%s,`sex`=%s,`dateofbirth`=%s,`course`=%s,`branch`=%s,`admittedon`=%s,`receiptno`=%s,`receiptdate`=%s,`mothertongue`=%s,`state`=%s,`present_address`=%s,`city`=%s,`district`=%s,`cell_number`=%s,`aadhar_number`=%s,`tcno`=%s,`issuedon`=%s WHERE reg_number='1715007'"
                        val=(self.e1.get(),self.e3.get(),self.e4.get(),self.e5.get(),self.e6.get(),self.e7.get(),self.e8.get(),self.e9.get(),self.e10.get(),self.e11.get(),self.e12.get(),self.e13.get(),self.e14.get(),self.e15.get(),self.e16.get(),self.e17.get(),self.e18.get(),self.e19.get(),self.e20.get(),self.e21.get(),self.ea22.get(),self.ea23.get())
                        db.execute(sql, val)
                        db_cur.commit()
                        MyFirstGui().switch_frame(pageOne)
                
           
class newreg(tk.Frame):
          
            def __init__(self, master):
                tk.Frame.__init__(self,master)
                self.configure(background='powderblue')
                #db.execute("select *from studentdetails where reg_number='%s'"%(setvar))
                #e=db.fetchone()
                def Validate():
                    date_format = '%Y-%m-%d'
                    rule = re.compile(r'(^[+0-9]{1,3})*([0-9]{10,11}$)')
                    if not rule.search(self.ea22.get()):
                        messagebox.showinfo("INVALID MOBILE NUMBER", "PLEASE ENTER A VALID MOBILE NUMBER")
                    try:
                        date_obj = datetime.datetime.strptime(self.e10.get(), date_format)
                    except ValueError:
                      messagebox.showinfo("INVALID DATE FORMAT", "PLEASE ENTER A VALID DATE OF BIRTH('%Y-%m-%d')")   
                    try:
                        date_obj = datetime.datetime.strptime(self.e13.get(), date_format)
                    except ValueError:
                      messagebox.showinfo("INVALID DATE FORMAT", "PLEASE ENTER A VALID ADMISSION ('%Y-%m-%d')")   
                    try:
                        date_obj = datetime.datetime.strptime(self.e15.get(), date_format)
                    except ValueError:
                      messagebox.showinfo("INVALID DATE FORMAT", "PLEASE ENTER A VALID RECEIPT DATE('%Y-%m-%d')")   
                    try:
                        date_obj = datetime.datetime.strptime(self.ea25.get(), date_format)
                    except ValueError:
                      messagebox.showinfo("INVALID DATE FORMAT", "PLEASE ENTER A VALID ISSUED ON DATE('%Y-%m-%d')")   
                labe=tk.Label(self,text="REGISTER",font=("Times 10 italic"),background="powderblue")
                labe.grid(row=0,column=0,sticky='W')
                global name,regno,rollno,taluk,father,nation,religion,caste,community,sex,dob,course,branch,admiton,receiptno,mothertongue,state,address,city,district,cellno,aadharno,tcno,issuedon
                self.l1=ttk.Label(self,text="Name Of The Candidate",font=("Times 10 italic"),background="powderblue")
                self.l1.grid(row=1,column=0,sticky='W',pady=5)
                self.ll1=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll1.grid(row=1,column=1,sticky='W')
                self.e1=ttk.Entry(self,font=("Times 10 italic"))
                self.e1.grid(row=1,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.l2=ttk.Label(self,text="Reg Number",font=("Times 10 italic"),background="powderblue")
                self.l2.grid(row=2,column=0,sticky='W',pady=5)
                self.ll2=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll2.grid(row=2,column=1,sticky='W',pady=5)
                self.e2=ttk.Entry(self,font=("Times 10 italic"))
                self.e2.grid(row=2,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.l3=ttk.Label(self,text="Roll Number",font=("Times 10 italic"),background="powderblue")
                self.l3.grid(row=3,column=0,sticky='W',pady=5)
                self.ll3=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll3.grid(row=3,column=1,sticky='W',pady=5)
                self.e3=ttk.Entry(self,font=("Times 10 italic"))
                self.e3.grid(row=3,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.l4=ttk.Label(self,text="Father's Name",font=("Times 10 italic"),background="powderblue")
                self.l4.grid(row=4,column=0,sticky='W',pady=5)
                self.ll4=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll4.grid(row=4,column=1,sticky='W',pady=5)
                self.e4=ttk.Entry(self,font=("Times 10 italic"))
                self.e4.grid(row=4,column=2,sticky='W',padx=5,pady=5,ipady=5)
            
                self.l5=ttk.Label(self,text="Nationality",font=("Times 10 italic"),background="powderblue")
                self.l5.grid(row=5,column=0,sticky='W',pady=5)
                self.ll5=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll5.grid(row=5,column=1,sticky='W',pady=5)
                self.e5=ttk.Entry(self,font=("Times 10 italic"))
                self.e5.grid(row=5,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.l6=ttk.Label(self,text="Religion",font=("Times 10 italic"),background="powderblue")
                self.l6.grid(row=6,column=0,sticky='W',pady=5)
                self.ll6=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll6.grid(row=6,column=1,sticky='W',pady=5)
                self.e6=ttk.Entry(self,font=("Times 10 italic"))
                self.e6.grid(row=6,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.l7=ttk.Label(self,text="Caste",font=("Times 10 italic"),background="powderblue")
                self.l7.grid(row=7,column=0,sticky='W',pady=5)
                self.ll7=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll7.grid(row=7,column=1,sticky='W',pady=5)
                self.e7=ttk.Entry(self,font=("Times 10 italic"))
                self.e7.grid(row=7,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.l8=ttk.Label(self,text="Community",font=("Times 10 italic"),background="powderblue")
                self.l8.grid(row=8,column=0,sticky='W',pady=5)
                self.ll8=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll8.grid(row=8,column=1,sticky='W',pady=5)
                self.e8=ttk.Entry(self,font=("Times 10 italic"))
                self.e8.grid(row=8,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.l9=ttk.Label(self,text="Sex",font=("Times 10 italic"),background="powderblue")
                self.l9.grid(row=9,column=0,sticky='W',pady=5)
                self.ll9=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll9.grid(row=9,column=1,sticky='W',pady=5)
                self.e9=ttk.Entry(self,font=("Times 10 italic"))
                self.e9.grid(row=9,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.l10=ttk.Label(self,text="Date Of Birth",font=("Times 10 italic"),background="powderblue")
                self.l10.grid(row=10,column=0,sticky='W',pady=5)
                self.ll10=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll10.grid(row=10,column=1,sticky='W',pady=5)
                self.e10=ttk.Entry(self,font=("Times 10 italic"))
                self.e10.grid(row=10,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.l11=ttk.Label(self,text="Course Of Study",font=("Times 10 italic"),background="powderblue")
                self.l11.grid(row=11,column=0,sticky='W',pady=5)
                self.ll11=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll11.grid(row=11,column=1,sticky='W',pady=5)
                self.e11=ttk.Entry(self,font=("Times 10 italic"))
                self.e11.grid(row=11,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.l12=ttk.Label(self,text="Branch Of Study",font=("Times 10 italic"),background="powderblue")
                self.l12.grid(row=12,column=0,sticky='W',pady=5)
                self.ll12=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll12.grid(row=12,column=1,sticky='W',pady=5)
                self.e12=ttk.Entry(self,font=("Times 10 italic"))
                self.e12.grid(row=12,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.l13=ttk.Label(self,text=" Admitted On",font=("Times 10 italic"),background="powderblue")
                self.l13.grid(row=13,column=0,sticky='W',pady=5)
                self.ll13=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll13.grid(row=13,column=1,sticky='W',pady=5)
                self.e13=ttk.Entry(self,font=("Times 10 italic"))
                self.e13.grid(row=13,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.l14=ttk.Label(self,text="Receipt Number",font=("Times 10 italic"),background="powderblue")
                self.l14.grid(row=14,column=0,sticky='W',pady=5)
                self.ll14=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll14.grid(row=14,column=1,sticky='W',pady=5)
                self.e14=ttk.Entry(self,font=("Times 10 italic"))
                self.e14.grid(row=14,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.l15=ttk.Label(self,text="Receipt Date",font=("Times 10 italic"),background="powderblue")
                self.l15.grid(row=15,column=0,sticky='W',pady=5)
                self.ll15=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll15.grid(row=15,column=1,sticky='W',pady=5)
                self.e15=ttk.Entry(self,font=("Times 10 italic"))
                self.e15.grid(row=15,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.l16=ttk.Label(self,text="Mother Tongue",font=("Times 10 italic"),background="powderblue")
                self.l16.grid(row=16,column=0,sticky='W',pady=5)
                self.ll16=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll16.grid(row=16,column=1,sticky='W',pady=5)
                self.e16=ttk.Entry(self,font=("Times 10 italic"))
                self.e16.grid(row=16,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.l17=ttk.Label(self,text="Name Of State",font=("Times 10 italic"),background="powderblue")
                self.l17.grid(row=17,column=0,sticky='W',pady=5)
                self.ll17=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll17.grid(row=17,column=1,sticky='W',pady=5)
                self.e17=ttk.Entry(self,font=("Times 10 italic"))
                self.e17.grid(row=17,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.l18=ttk.Label(self,text="Present address ",font=("Times 10 italic"),background="powderblue")
                self.l18.grid(row=18,column=0,sticky='W',pady=5)
                self.ll18=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll18.grid(row=18,column=1,sticky='W',pady=5)
                self.e18=ttk.Entry(self,font=("Times 10 italic"))
                self.e18.grid(row=18,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.l19=ttk.Label(self,text="Taluk ",font=("Times 10 italic"),background="powderblue")
                self.l19.grid(row=19,column=0,sticky='W',pady=5)
                self.ll19=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll19.grid(row=19,column=1,sticky='W',pady=5)
                self.e19=ttk.Entry(self,font=("Times 10 italic"))
                self.e19.grid(row=19,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.l20=ttk.Label(self,text="City",font=("Times 10 italic"),background="powderblue")
                self.l20.grid(row=20,column=0,sticky='W',pady=5)
                self.ll20=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll20.grid(row=20,column=1,sticky='W',pady=5)
                self.e20=ttk.Entry(self,font=("Times 10 italic"))
                self.e20.grid(row=20,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.l21=ttk.Label(self,text="District",font=("Times 10 italic"),background="powderblue")
                self.l21.grid(row=21,column=0,sticky='W',pady=5)
                self.ll21=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.ll21.grid(row=21,column=1,sticky='W',pady=5)
                self.e21=ttk.Entry(self,font=("Times 10 italic"))
                self.e21.grid(row=21,column=2,sticky='W',padx=5,pady=5,ipady=5)
            
                self.la22=ttk.Label(self,text="Cell Number",font=("Times 10 italic"),background="powderblue")
                self.la22.grid(row=22,column=0,sticky='W',pady=5)
                self.lla22=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.lla22.grid(row=22,column=1,sticky='W',pady=5)
                self.ea22=ttk.Entry(self,font=("Times 10 italic"))
                self.ea22.grid(row=22,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                self.la23=ttk.Label(self,text="Aadhar Number",font=("Times 10 italic"),background="powderblue")
                self.la23.grid(row=23,column=0,sticky='W',pady=5)
                self.lla23=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.lla23.grid(row=23,column=1,sticky='W',pady=5)
                self.ea23=ttk.Entry(self,font=("Times 10 italic"))
                self.ea23.grid(row=23,column=2,sticky='W',padx=5,pady=5,ipady=5)
                
                 
                self.la24=ttk.Label(self,text="T.C.No",font=("Times 10 italic"),background="powderblue")
                self.la24.grid(row=24,column=0,sticky='W',pady=5)
                self.lla24=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.lla24.grid(row=24,column=1,sticky='W',pady=5)
                self.ea24=ttk.Entry(self,font=("Times 10 italic"))
                self.ea24.grid(row=24,column=2,sticky='W',padx=5,pady=5,ipady=5)
                 
                self.la25=ttk.Label(self,text=" Issued ON",font=("Times 10 italic"),background="powderblue")
                self.la25.grid(row=25,column=0,sticky='W',pady=5)
                self.lla25=ttk.Label(self,text="  :  ",font=("Times 10 italic"),background="powderblue")
                self.lla25.grid(row=25,column=1,sticky='W',pady=5)
                self.ea25=ttk.Entry(self,font=("Times 10 italic"))
                self.ea25.grid(row=25,column=2,sticky='W',padx=5,pady=5,ipady=5)
                self.b1=ttk.Button(self,text="Register",style = 'W.TButton',command=self.calle)
                self.b1.grid(row=26,column=2,padx=10,pady=50)
                
                self.b1.configure(command=Validate)
                
                self.but=ttk.Button(self,style = 'B.TButton',text="<-",command=lambda: master.switch_frame(pageOne))
                self.but.grid(row=26,column=0,sticky='W')
          
              
            def calle(self):
                
                self.name=self.e1.get()
                self.regno=self.e2.get()
                self.rollno=self.e3.get()
                self.father=self.e4.get()
                self.nation=self.e5.get()
                self.religion=self.e6.get()
                self.caste=self.e7.get()
                self.community=self.e7.get()
                self.sex=self.e8.get()
                self.dob=self.e10.get()
                self.course=self.e11.get()
                self.branch=self.e12.get()
                self.admiton=self.e13.get()
                self.receiptno=self.e14.get()
                self.receiptdate=self.e15.get()
                self.mothertongue=self.e16.get()
                self.state=self.e17.get()
                self.address=self.e18.get()
                self.taluk=self.e19.get()
                self.city=self.e20.get()  
                self.district=self.e21.get()
                self.cellno=self.ea22.get()
                self.aadharno=self.ea23.get()
                self.tcno=self.ea24.get()
                self.issuedon=self.ea25.get()
                #INSERT INTO `studentdetails`(`name`, `reg_number`, `roll_number`, `father_name`, `nationality`, `religion`, `caste`, `community`, `sex`, `dateofbirth`, `course`, `branch`, `admittedon`, `receiptno`, `receiptdate`, `mothertongue`, `state`, `present_address`, `city`, `district`, `cell_number`, `aadhar_number`, `tcno`, `issuedon`) 
                sql1="INSERT INTO studentdetails (name,reg_number,roll_number,father_name,nationality,religion,caste,community,sex,dateofbirth,course,branch,admittedon,receiptno,receiptdate,mothertongue,state,present_address,taluk,city,district,cell_number,aadhar_number,tcno,issuedon)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val1=(self.name,self.regno,self.rollno,self.father,self.nation,self.religion,self.caste,self.community,self.sex,self.dob,self.course,self.branch,self.admiton,self.receiptno,self.receiptdate,self.mothertongue,self.state,self.address,self.taluk,self.city,self.district,self.cellno, self.aadharno,self.tcno,self.issuedon)
                db.execute(sql1, val1)
                db_cur.commit()
                MyFirstGui().switch_frame(pageOne) 
           
       
class search(tk.Frame):
                  def __init__(self, master):
                        tk.Frame.__init__(self,master)
                        self.la=tk.Label(self,text="search")
                        self.la.grid(row=0,column=1,sticky='W')
                        self.la1=tk.Label(self,text="Religion")
                        self.la1.grid(row=1,column=0,sticky='W')
                        self.eta1=tk.Entry(self)
                        self.eta1.grid(row=1,column=1,sticky='W')
                        self.la2=tk.Label(self,text="Caste")
                        self.la2.grid(row=2,column=0,sticky='W')
                        self.eta2=tk.Entry(self)
                        self.eta2.grid(row=2,column=1,sticky='W')
                        self.la3=tk.Label(self,text="Sex")
                        self.la3.grid(row=3,column=0,sticky='W')
                        self.eta3=tk.Entry(self)
                        self.eta3.grid(row=3,column=1,sticky='W')
                        self.la4=tk.Label(self,text="Branch Of Study")
                        self.la4.grid(row=4,column=0,sticky='W')
                        self.eta4=tk.Entry(self)
                        self.eta4.grid(row=4,column=1,sticky='W')
                        self.la5=tk.Label(self,text="Taluk")
                        self.la5.grid(row=5,column=0,sticky='W')
                        self.eta5=tk.Entry(self)
                        self.eta5.grid(row=5,column=1,sticky='W')
                        self.la6=tk.Label(self,text="District")
                        self.la6.grid(row=6,column=0,sticky='W')
                        self.eta6=tk.Entry(self)
                        self.eta6.grid(row=6,column=1,sticky='W')
                        self.buty=tk.Button(self,text="search",command=self.say_hello)
                        self.buty.grid(row=7,column=1,sticky='W')
                        
                 
                      
                      
                  def say_hello(self):
                      # reli,cast,seex,bos,tal,dis
                      self.reli=self.eta1.get()
                      self.cast=self.eta2.get()
                      self.seex=self.eta3.get()
                      self.bos=self.eta4.get()
                      self.tal=self.eta5.get()
                      self.dis=self.eta6.get()
                      wb = Workbook()
                      #global ff
                      #print(self.reli)
                      if(self.reli!="" and self.cast =="" and self.seex == ""  and self.bos==""  and self.tal =="" and self.dis==""):
                          db.execute("select *from studentdetails where religion='%s'" %(self.reli))
                          #ff=db.fetchone()
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religion"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)

                      elif(self.reli==" " and self.cast !="" and self.seex ==""  and self.bos==""  and self.tal =="" and self.dis==""):
                          db.execute("select *from studentdetails where caste ='%s'" %(self.cast))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "caste"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli==" " and self.cast =="" and self.seex !=""  and self.bos==""  and self.tal =="" and self.dis==""):
                          db.execute("select *from studentdetails where sex ='%s'" %(self.seex))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "gender"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli==" " and self.cast =="" and self.seex ==""  and self.bos!=""  and self.tal =="" and self.dis==""):
                          db.execute("select *from studentdetails where branch ='%s'" %(self.bos))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "Branch of study"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli==" " and self.cast =="" and self.seex ==""  and self.bos==""  and self.tal !="" and self.dis==""):
                          db.execute("select *from studentdetails where taluk ='%s'" %(self.tal))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "Taluk"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli==" " and self.cast =="" and self.seex ==""  and self.bos==""  and self.tal =="" and self.dis!=""):
                          db.execute("select *from studentdetails where district ='%s'" %(self.dis))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "District"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!=" " and self.cast !="" and self.seex ==""  and self.bos==""  and self.tal =="" and self.dis==""):
                          db.execute("select *from studentdetails where religion ='%s' and caste ='%s'" %(self.reli,self.cast))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religioncaste"
                          wb.save(workbook_name + ".xlsx")
                      elif(self.reli!="" and self.cast =="" and self.seex !=""  and self.bos==""  and self.tal =="" and self.dis==""):
                          db.execute("select *from studentdetails where religion ='%s' and sex='%s'" %(self.reli,self.seex))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religiongender"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast =="" and self.seex ==""  and self.bos!=""  and self.tal =="" and self.dis==""):
                          db.execute("select *from studentdetails where religion ='%s' and branch='%s'" %(self.reli,self.bos))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religionbranch"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast =="" and self.seex ==""  and self.bos==""  and self.tal !="" and self.dis==""):
                          db.execute("select *from studentdetails where religion ='%s' and taluk='%s'" %(self.reli,self.tal))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religiontaluk"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast =="" and self.seex ==""  and self.bos==""  and self.tal =="" and self.dis!=""):
                          db.execute("select *from studentdetails where religion ='%s' and branch='%s'" %(self.reli,self.dis))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religionbranch"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast !="" and self.seex !=""  and self.bos==""  and self.tal =="" and self.dis==""):
                          db.execute("select *from studentdetails where caste='%s' and sex='%s'" %(self.cast,self.seex))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "castesex"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast !="" and self.seex ==""  and self.bos!=""  and self.tal =="" and self.dis==""):
                          db.execute("select *from studentdetails where caste='%s' and branch='%s'" %(self.cast,self.bos))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "castebranch"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast !="" and self.seex ==""  and self.bos==""  and self.tal !="" and self.dis==""):
                          db.execute("select *from studentdetails where caste='%s' and taluk='%s'" %(self.cast,self.tal))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "castetaluk"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast !="" and self.seex ==""  and self.bos==""  and self.tal =="" and self.dis!=""):
                          db.execute("select *from studentdetails where caste='%s' and district='%s'" %(self.cast,self.dis))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "castedistrict"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast =="" and self.seex !=""  and self.bos!=""  and self.tal =="" and self.dis==""):
                          db.execute("select *from studentdetails where sex='%s' and branch='%s'" %(self.seex,self.bos))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "sexbranch"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast =="" and self.seex !=""  and self.bos==""  and self.tal !="" and self.dis==""):
                          db.execute("select *from studentdetails where sex='%s' and taluk='%s'" %(self.seex,self.tal))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "sextaluk"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast =="" and self.seex !=""  and self.bos==""  and self.tal =="" and self.dis!=""):
                          db.execute("select *from studentdetails where sex='%s' and district='%s'" %(self.seex,self.dis))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "sexdistrict"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast =="" and self.seex ==""  and self.bos!=""  and self.tal !="" and self.dis==""):
                          db.execute("select *from studentdetails where branch='%s' and taluk='%s'" %(self.bos,self.tal))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "branchtaluk"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast =="" and self.seex ==""  and self.bos!=""  and self.tal =="" and self.dis!=""):
                          db.execute("select *from studentdetails where branch='%s' and district='%s'" %(self.bos,self.dis))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "branchdistrict"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast =="" and self.seex !=""  and self.bos==""  and self.tal =="" and self.dis!=""):
                          db.execute("select *from studentdetails where taluk='%s' and district='%s'" %(self.tal,self.dis))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "talukdistrict"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      #3 combo  
                      elif(self.reli!="" and self.cast !="" and self.seex !=""  and self.bos==""  and self.tal =="" and self.dis==""):
                          db.execute("select *from studentdetails where religion='%s' and caste='%s' and sex='%s'" %(self.reli,self.cast,self.seex))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religioncastesex"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast !="" and self.seex ==""  and self.bos!=""  and self.tal =="" and self.dis==""):
                          db.execute("select *from studentdetails where religion='%s' and caste='%s' and branch='%s'" %(self.reli,self.cast,self.bos))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religioncastebranch"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast !="" and self.seex ==""  and self.bos==""  and self.tal !="" and self.dis==""):
                          db.execute("select *from studentdetails where religion='%s' and caste='%s' and taluk='%s'" %(self.reli,self.cast,self.tal))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religioncastetaluk"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast !="" and self.seex ==""  and self.bos==""  and self.tal =="" and self.dis!=""):
                          db.execute("select *from studentdetails where religion='%s' and caste='%s' and district='%s'" %(self.reli,self.cast,self.dis))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religioncastedistrict"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast=="" and self.seex !=""  and self.bos!=""  and self.tal =="" and self.dis==""):
                          db.execute("select *from studentdetails where religion='%s' and sex='%s' and branch='%s'" %(self.reli,self.seex,self.bos))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religionsexbranch"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast=="" and self.seex !=""  and self.bos==""  and self.tal !="" and self.dis==""):
                          db.execute("select *from studentdetails where religion='%s' and sex='%s' and taluk='%s'" %(self.reli,self.seex,self.tal))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religionsextaluk"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast=="" and self.seex !=""  and self.bos==""  and self.tal =="" and self.dis!=""):
                          db.execute("select *from studentdetails where religion='%s' and sex='%s' and branch='%s' and district='%s'" %(self.reli,self.seex,self.dis))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religionsexbranch"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast=="" and self.seex ==""  and self.bos!=""  and self.tal !="" and self.dis==""):
                          db.execute("select *from studentdetails where religion='%s' and taluk='%s' and branch='%s'" %(self.reli,self.tal,self.bos))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religiontalukbranch"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast=="" and self.seex ==""  and self.bos!=""  and self.tal =="" and self.dis!=""):
                          db.execute("select *from studentdetails where religion='%s' and district='%s' and branch='%s'" %(self.reli,self.dis,self.bos))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religiondistrictbranch"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast=="" and self.seex ==""  and self.bos==""  and self.tal !="" and self.dis!=""):
                          db.execute("select *from studentdetails where religion='%s' and taluk='%s' and district='%s'" %(self.reli,self.tal,self.dis))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religiontalukdistrict"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast!="" and self.seex !=""  and self.bos!=""  and self.tal =="" and self.dis==""):
                          db.execute("select *from studentdetails where caste='%s' and sex='%s' and branch='%s'" %(self.cast,self.seex,self.bos))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "castesexbranch"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast!="" and self.seex !=""  and self.bos==""  and self.tal !="" and self.dis==""):
                          db.execute("select *from studentdetails where caste='%s' and sex='%s' and taluk='%s'" %(self.cast,self.seex,self.tal))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "castesextaluk"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast!="" and self.seex !=""  and self.bos==""  and self.tal =="" and self.dis!=""):
                          db.execute("select *from studentdetails where caste='%s' and sex='%s' and district='%s'" %(self.cast,self.seex,self.dis))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "castesexdistrict"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast!="" and self.seex ==""  and self.bos!=""  and self.tal !="" and self.dis==""):
                          db.execute("select *from studentdetails where caste='%s' and taluk='%s' and branch='%s'" %(self.cast,self.tal,self.bos))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "castetalukbranch"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast!="" and self.seex ==""  and self.bos!=""  and self.tal =="" and self.dis!=""):
                          db.execute("select *from studentdetails where caste='%s' and district='%s' and branch='%s'" %(self.cast,self.dis,self.bos))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "castedistrictbranch"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast!="" and self.seex ==""  and self.bos==""  and self.tal !="" and self.dis!=""):
                          db.execute("select *from studentdetails where caste='%s' and taluk='%s' and district='%s'" %(self.cast,self.tal,self.dis))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "castetaukdistrict"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast=="" and self.seex !=""  and self.bos!=""  and self.tal !="" and self.dis==""):
                          db.execute("select *from studentdetails where taluk='%s' and sex='%s' and branch='%s'" %(self.tal,self.seex,self.bos))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "taluksexbranch"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast=="" and self.seex !=""  and self.bos!=""  and self.tal =="" and self.dis!=""):
                          db.execute("select *from studentdetails where district='%s' and sex='%s' and branch='%s'" %(self.dis,self.seex,self.bos))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "districtsexbranch"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast=="" and self.seex !=""  and self.bos==""  and self.tal !="" and self.dis!=""):
                          db.execute("select *from studentdetails where district='%s' and sex='%s' and taluk='%s'" %(self.dist,self.seex,self.tal))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                         
                          workbook_name = "districtsextaluk"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast=="" and self.seex ==""  and self.bos!=""  and self.tal !="" and self.dis!=""):
                          db.execute("select *from studentdetails where district='%s' and taluk='%s' and branch='%s'" %(self.dis,self.tal,self.bos))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "districttalukbranch"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast!="" and self.seex !=""  and self.bos!=""  and self.tal =="" and self.dis==""):
                          db.execute("select *from studentdetails where religion='%s' and caste='%s' and sex='%s' and branch='%s'" %(self.reli,self.cast,self.seex,self.bos))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religioncastesexbranch"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast!="" and self.seex !=""  and self.bos==""  and self.tal !="" and self.dis==""):
                          db.execute("select *from studentdetails where religion='%s' and caste='%s' and sex='%s' and taluk='%s'" %(self.reli,self.cast,self.seex,self.tal))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religioncastesextaluk"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast!="" and self.seex !=""  and self.bos==""  and self.tal =="" and self.dis!=""):
                          db.execute("select *from studentdetails where religion='%s' and caste='%s' and sex='%s' and district='%s'" %(self.reli,self.cast,self.seex,self.dis))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religioncastesexdistrict"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast!="" and self.seex ==""  and self.bos!=""  and self.tal !="" and self.dis==""):
                          db.execute("select *from studentdetails where religion='%s' and caste='%s' and branch='%s' and taluk='%s'" %(self.reli,self.cast,self.bos,self.tal))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religioncastebranchtaluk"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast!="" and self.seex ==""  and self.bos!=""  and self.tal =="" and self.dis!=""):
                          db.execute("select *from studentdetails where religion='%s' and caste='%s' and branch='%s' and district='%s'" %(self.reli,self.cast,self.bos,self.dis))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religioncastebranchdistrict"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast!="" and self.seex ==""  and self.bos==""  and self.tal !="" and self.dis!=""):
                          db.execute("select *from studentdetails where religion='%s' and caste='%s' and district='%s' and taluk='%s'" %(self.reli,self.cast,self.dis,self.tal))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religioncastedistricttaluk"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast!="" and self.seex !=""  and self.bos!=""  and self.tal !="" and self.dis==""):
                          db.execute("select *from studentdetails where sex='%s' and caste='%s' and branch='%s' and taluk='%s'" %(self.seex,self.cast,self.bos,self.tal))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "sexcastebranchtaluk"
                          wb.save(workbook_name + ".xlsx")
                      elif(self.reli=="" and self.cast!="" and self.seex !=""  and self.bos!=""  and self.tal =="" and self.dis!=""):
                          db.execute("select *from studentdetails where sex='%s' and caste='%s' and branch='%s' and district='%s'" %(self.seex,self.cast,self.bos,self.dis))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "sexcastebranchdistrict"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast!="" and self.seex !=""  and self.bos==""  and self.tal !="" and self.dis!=""):
                          db.execute("select *from studentdetails where sex='%s' and caste='%s' and district='%s' and taluk='%s'" %(self.seex,self.cast,self.dis,self.tal))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "sexcaste districtaluk"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast=="" and self.seex !=""  and self.bos!=""  and self.tal !="" and self.dis==""):
                          db.execute("select *from studentdetails where religion='%s' and sex='%s' and branch='%s' and taluk='%s'" %(self.reli,self.seex,self.bos,self.tal))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religionsexbranchtaluk"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast=="" and self.seex !=""  and self.bos!=""  and self.tal =="" and self.dis!=""):
                          db.execute("select *from studentdetails where religion='%s' and sex='%s' and branch='%s' and district='%s'" %(self.reli,self.seex,self.bos,self.dis))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religionsexbranchdistrict"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast=="" and self.seex !=""  and self.bos==""  and self.tal !="" and self.dis!=""):
                          db.execute("select *from studentdetails where religion='%s' and sex='%s' and district='%s' and taluk='%s'" %(self.reli,self.seex,self.dis,self.tal))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religionsexdistricttaluk"
                          wb.save(workbook_name + ".xlsx")
                      elif(self.reli!="" and self.cast=="" and self.seex ==""  and self.bos!=""  and self.tal !="" and self.dis!=""):
                          db.execute("select *from studentdetails where religion='%s' and district='%s' and branch='%s' and taluk='%s'" %(self.reli,self.dis,self.bos,self.tal))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religiondistrictbranchtaluk"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast!="" and self.seex ==""  and self.bos!=""  and self.tal !="" and self.dis!=""):
                          db.execute("select *from studentdetails where district='%s' and caste='%s' and branch='%s' and taluk='%s'" %(self.dis,self.cast,self.bos,self.tal))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "districtcastebranchtaluk"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast=="" and self.seex !=""  and self.bos!=""  and self.tal !="" and self.dis!=""):
                          db.execute("select *from studentdetails where sex='%s' and district='%s' and branch='%s' and taluk='%s'" %(self.seex,self.dis,self.bos,self.tal))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "sexdistrictbranchtaluk"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast!="" and self.seex !=""  and self.bos!=""  and self.tal !="" and self.dis==""):
                          db.execute("select *from studentdetails where religion='%s' and caste='%s' and branch='%s' and taluk='%s' and sex='%s'" %(self.reli,self.cast,self.bos,self.tal,self.seex))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religioncastebranchtaluksex"
                          wb.save(workbook_name + ".xlsx")
                          wb.system(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast!="" and self.seex !=""  and self.bos!=""  and self.tal =="" and self.dis!=""):
                          db.execute("select *from studentdetails where religion='%s' and caste='%s' and branch='%s' and district='%s' and sex='%s'" %(self.reli,self.cast,self.bos,self.dis,self.seex))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religioncastebranchdistrictsex"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast!="" and self.seex !=""  and self.bos==""  and self.tal !="" and self.dis!=""):
                          db.execute("select *from studentdetails where religion='%s' and caste='%s' and district='%s' and taluk='%s' and sex='%s'" %(self.reli,self.cast,self.dis,self.tal,self.seex))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religioncastedistricttaluksex"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast!="" and self.seex ==""  and self.bos!=""  and self.tal !="" and self.dis!=""):
                          db.execute("select *from studentdetails where religion='%s' and caste='%s' and branch='%s' and taluk='%s' and district='%s'" %(self.reli,self.cast,self.bos,self.tal,self.dis))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religioncastebranchtalukdistrict"
                          wb.save(workbook_name + ".xlsx")
                      elif(self.reli!="" and self.cast=="" and self.seex !=""  and self.bos!=""  and self.tal !="" and self.dis!=""):
                          db.execute("select *from studentdetails where religion='%s' and district='%s' and branch='%s' and taluk='%s' and sex='%s'" %(self.reli,self.dis,self.bos,self.tal,self.seex))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religiondistrictbranchtaluksex"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli=="" and self.cast!="" and self.seex !=""  and self.bos!=""  and self.tal !="" and self.dis!=""):
                          db.execute("select *from studentdetails where district='%s' and caste='%s' and branch='%s' and taluk='%s' and sex='%s'" %(self.dis,self.cast,self.bos,self.tal,self.seex))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "districtcastebranchtaluksex"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                      elif(self.reli!="" and self.cast!="" and self.seex !=""  and self.bos!=""  and self.tal !="" and self.dis!=""):
                          db.execute("select *from studentdetails where religion='%s' and caste='%s' and branch='%s' and taluk='%s' and sex='%s' and district='%s'" %(self.reli,self.cast,self.bos,self.tal,self.sex,self.dis))
                          results = db.fetchall()
                          ws = wb.create_sheet(0)
                          #ws.title = studentdetails
                          ws.append(db.column_names)
                          for row in results:
                            ws.append(row)
                          workbook_name = "religioncastebranchtaluksexdistrict"
                          wb.save(workbook_name + ".xlsx")
                          v=os.path.abspath(workbook_name + ".xlsx")
                          dir = v.replace('\\','/')
                          webbrowser.open(dir)
                  
                      


if __name__ == "__main__":
    firstgui=MyFirstGui()
    firstgui.mainloop()
