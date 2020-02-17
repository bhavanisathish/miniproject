# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 18:17:39 2020

pip install mysql-connector

@author: Bhavani
"""

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
                self._frame.grid(row=0,column=3,sticky='N')
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
            self.b1.grid(row=9,column=0,padx=10,pady=50)
            self.b2=ttk.Button(self,text="RESET",style = 'W.TButton')
            self.b2.grid(row=9,column=2,padx=100,pady=50)
            
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
       
class pageOne(tk.Frame):
              def __init__(self,master):
                             
                             #self.configure(background='powderblue')
                             tk.Frame.__init__(self,master)
                             #self.windows_item = self.canvas.create_window(0,0, window=self, anchor=tk.NW)
 
                             lable1=ttk.Label(self,text="Start page",font=("Times 30 italic"),background="powderblue")
                             lable1.grid(row=0,column=1,padx=10,pady=90)
                             bb1=ttk.Button(self,text="TC generation",style = 'L.TButton',command=lambda: master.switch_frame(transferspecify))
                             bb1.grid(row=1,column=1,sticky='W')
                            
                             bb2=ttk.Button(self,text="Edit",style = 'L.TButton',command=lambda: master.switch_frame(editspecify))
                             bb2.grid(row=3,column=1,sticky='W',pady=50)
                             bb4=ttk.Button(self,text="Insert Record",style = 'L.TButton',command=lambda: master.switch_frame(newreg))
                             bb4.grid(row=4,column=1,sticky='W',pady=50)
                             
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
                    
                             #self.configure(background='powderblue')
                    tk.Frame.__init__(self,master)
                    #self.windows_item = self.canvas.create_window(0,0, window=self, anchor=tk.NW)
 
                    #tk.Frame.__init__(self, master)
                    
                    
                    #self._rootwindow.bind('<Configure>', self.onResize)
                    self.configure(background='powderblue')
                    db.execute("select *from studentdetails where reg_number='%s'"%(setvar))
                    e=db.fetchone()
                    self.labe=ttk.Label(self,text="EDIT",font=("Times 10 italic"),background="powderblue")
                    self.labe.grid(row=0,column=0,sticky='W')
                    
                    self.l1=ttk.Label(self,text="Name Of The Candidate",font=("Times 10 italic"),background="powderblue")
                    self.l1.grid(row=1,column=0,sticky='W',pady=5)
                    self.ll1=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll1.grid(row=1,column=1,sticky='W')
                    self.e1=ttk.Entry(self,font=("Times 10 italic"))
                    self.e1.grid(row=1,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e1.insert(0,e[0])
                    self.l2=ttk.Label(self,text="Roll Number",font=("Times 10 italic"),background="powderblue")
                    self.l2.grid(row=2,column=0,sticky='W')
                    self.ll2=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll2.grid(row=2,column=1,sticky='W')
                    self.e2=ttk.Entry(self,font=("Times 10 italic"))
                    self.e2.grid(row=2,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e2.insert(0,e[2])
                    self.l3=ttk.Label(self,text="Father's Name",font=("Times 10 italic"),background="powderblue")
                    self.l3.grid(row=3,column=0,sticky='W')
                    self.ll3=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll3.grid(row=3,column=1,sticky='W')
                    self.e3=ttk.Entry(self,font=("Times 10 italic"))
                    self.e3.grid(row=3,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e3.insert(0,e[3])
                    self.l4=ttk.Label(self,text="Nationality",font=("Times 10 italic"),background="powderblue")
                    self.l4.grid(row=4,column=0,sticky='W')
                    self.ll4=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll4.grid(row=4,column=1,sticky='W')
                    self.e4=ttk.Entry(self,font=("Times 10 italic"))
                    self.e4.grid(row=4,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e4.insert(0,e[4])
                    self.l5=ttk.Label(self,text="Religion",font=("Times 10 italic"),background="powderblue")
                    self.l5.grid(row=5,column=0,sticky='W')
                    self.ll5=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll5.grid(row=5,column=1,sticky='W')
                    self.e5=ttk.Entry(self,font=("Times 10 italic"))
                    self.e5.grid(row=5,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e5.insert(0,e[5])
                    self.l6=ttk.Label(self,text="Caste",font=("Times 10 italic"),background="powderblue")
                    self.l6.grid(row=6,column=0,sticky='W')
                    self.ll6=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll6.grid(row=6,column=1,sticky='W')
                    self.e6=ttk.Entry(self,font=("Times 10 italic"))
                    self.e6.grid(row=6,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e6.insert(0,e[6])
                    self.l7=ttk.Label(self,text="Community",font=("Times 10 italic"),background="powderblue")
                    self.l7.grid(row=7,column=0,sticky='W')
                    self.ll7=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll7.grid(row=7,column=1,sticky='W')
                    self.e7=ttk.Entry(self,font=("Times 10 italic"))
                    self.e7.grid(row=7,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e7.insert(0,e[7])
                    self.l8=ttk.Label(self,text="Sex",font=("Times 10 italic"),background="powderblue")
                    self.l8.grid(row=8,column=0,sticky='W')
                    self.ll8=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll8.grid(row=8,column=1,sticky='W')
                    self.e8=ttk.Entry(self,font=("Times 10 italic"))
                    self.e8.grid(row=8,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e8.insert(0,e[8])
                    self.l9=ttk.Label(self,text="Date Of Birth",font=("Times 10 italic"),background="powderblue")
                    self.l9.grid(row=9,column=0,sticky='W')
                    self.ll9=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll9.grid(row=9,column=1,sticky='W')
                    self.e9=ttk.Entry(self,font=("Times 10 italic"))
                    self.e9.grid(row=9,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e9.insert(0,e[9])
                    self.l10=ttk.Label(self,text="Course Of Study",font=("Times 10 italic"),background="powderblue")
                    self.l10.grid(row=10,column=0,sticky='W')
                    self.ll10=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll10.grid(row=10,column=1,sticky='W')
                    self.e10=ttk.Entry(self,font=("Times 10 italic"))
                    self.e10.grid(row=10,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e10.insert(0,e[10])
                    self.l11=ttk.Label(self,text="Branch Of Study",font=("Times 10 italic"),background="powderblue")
                    self.l11.grid(row=11,column=0,sticky='W')
                    self.ll11=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll11.grid(row=11,column=1,sticky='W')
                    self.e11=ttk.Entry(self,font=("Times 10 italic"))
                    self.e11.grid(row=11,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e11.insert(0,e[11])
                    self.l12=ttk.Label(self,text="Admitted On",font=("Times 10 italic"),background="powderblue")
                    self.l12.grid(row=12,column=0,sticky='W')
                    self.ll12=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll12.grid(row=12,column=1,sticky='W')
                    self.e12=ttk.Entry(self,font=("Times 10 italic"))
                    self.e12.grid(row=12,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e12.insert(0,e[12])
                    self.l13=ttk.Label(self,text="Receipt Number",font=("Times 10 italic"),background="powderblue")
                    self.l13.grid(row=13,column=0,sticky='W',pady=5)
                    self.ll13=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll13.grid(row=13,column=1,sticky='W',pady=5,padx=30)
                    self.e13=ttk.Entry(self,font=("Times 10 italic"))
                    self.e13.grid(row=13,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e13.insert(0,e[13])
                    self.l14=ttk.Label(self,text="Receipt Date",font=("Times 10 italic"),background="powderblue")
                    self.l14.grid(row=14,column=0,sticky='W')
                    self.ll14=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll14.grid(row=14,column=1,sticky='W')
                    self.e14=ttk.Entry(self,font=("Times 10 italic"))
                    self.e14.grid(row=14,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e14.insert(0,e[14])
                    self.l15=ttk.Label(self,text="Mother Tongue",font=("Times 10 italic"),background="powderblue")
                    self.l15.grid(row=15,column=0,sticky='W')
                    self.ll15=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll15.grid(row=15,column=1,sticky='W')
                    self.e15=ttk.Entry(self,font=("Times 10 italic"))
                    self.e15.grid(row=15,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e15.insert(0,e[15])
                    self.l16=ttk.Label(self,text="Name Of State ",font=("Times 10 italic"),background="powderblue")
                    self.l16.grid(row=16,column=0,sticky='W')
                    self.ll16=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll16.grid(row=16,column=1,sticky='W')
                    self.e16=ttk.Entry(self,font=("Times 10 italic"))
                    self.e16.grid(row=16,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e16.insert(0,e[16])
                    self.l17=ttk.Label(self,text="Present address",font=("Times 10 italic"),background="powderblue")
                    self.l17.grid(row=17,column=0,sticky='W')
                    self.ll17=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll17.grid(row=17,column=1,sticky='W')
                    self.e17=ttk.Entry(self,font=("Times 10 italic"))
                    self.e17.grid(row=17,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e17.insert(0,e[17])
                    self.l18=ttk.Label(self,text=" City",font=("Times 10 italic"),background="powderblue")
                    self.l18.grid(row=18,column=0,sticky='W',pady=5)
                    self.ll18=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll18.grid(row=18,column=1,sticky='W',pady=5,padx=30)
                    self.e18=ttk.Entry(self,font=("Times 10 italic"))
                    self.e18.grid(row=18,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e18.insert(0,e[18])
                    self.l19=ttk.Label(self,text="District",font=("Times 10 italic"),background="powderblue")
                    self.l19.grid(row=19,column=0,sticky='W')
                    self.ll19=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll19.grid(row=19,column=1,sticky='W')
                    self.e19=ttk.Entry(self,font=("Times 10 italic"))
                    self.e19.grid(row=19,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e19.insert(0,e[19])
                    self.l20=ttk.Label(self,text="Cell Number",font=("Times 10 italic"),background="powderblue")
                    self.l20.grid(row=20,column=0,sticky='W')
                    self.ll20=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll20.grid(row=20,column=1,sticky='W')
                    self.e20=ttk.Entry(self,font=("Times 10 italic"))
                    self.e20.grid(row=20,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e20.insert(0,e[20])
                    self.l21=ttk.Label(self,text="Aadhar Number",font=("Times 10 italic"),background="powderblue")
                    self.l21.grid(row=21,column=0,sticky='W')
                    self.ll21=ttk.Label(self,text="  :  ",background="powderblue")
                    self.ll21.grid(row=21,column=1,sticky='W')
                    self.e21=tk.Entry(self,font=("Times 10 italic"))
                    self.e21.grid(row=21,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.e21.insert(0,e[21])
                    self.la22=ttk.Label(self,text="T.C.No",font=("Times 10 italic"),background="powderblue")
                    self.la22.grid(row=22,column=0,sticky='W')
                    self.lla22=ttk.Label(self,text="  :  ",background="powderblue")
                    self.lla22.grid(row=22,column=1,sticky='W')
                    self.ea22=ttk.Entry(self,font=("Times 10 italic"))
                    self.ea22.grid(row=22,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.ea22.insert(0,e[22])
                    self.la23=ttk.Label(self,text="Issued ON",font=("Times 10 italic"),background="powderblue")
                    self.la23.grid(row=23,column=0,sticky='W')
                    self.lla23=ttk.Label(self,text="  :  ",background="powderblue")
                    self.lla23.grid(row=23,column=1,sticky='W',)
                    self.ea23=ttk.Entry(self,font=("Times 10 italic"))
                    self.ea23.grid(row=23,column=2,sticky='W',padx=5,pady=5,ipady=5)
                    self.ea23.insert(0,e[23])
                    self.la24=ttk.Button(self,style = 'W.TButton',text="SUBMIT",command=self.callme)
                    self.la24.grid(row=24,column=2,sticky='E')
                    self.button19=ttk.Button(self,text="<-",style = 'B.TButton',command=lambda: master.switch_frame(transferspecify))
                    self.button19.grid(row=24,column=0,sticky='W')
                    
                    #button19=tk.Button(self,text="<-",style = 'B.TButton',command=lambda: master.switch_frame(editspecify))
                    #button19.grid(row=23,column=0,sticky='W')
                    
    
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
                labe=tk.Label(self,text="REGISTER")
                labe.grid(row=0,column=0,sticky='W')
                global name,regno,rollno,taluk,father,nation,religion,caste,community,sex,dob,course,branch,admiton,receiptno,mothertongue,state,address,city,district,cellno,aadharno,tcno,issuedon
                self.l1=tk.Label(self,text="Name Of The Candidate",bg="powderblue")
                self.l1.grid(row=1,column=0,sticky='W',pady=5)
                self.ll1=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll1.grid(row=1,column=1,sticky='W')
                self.e1=tk.Entry(self,width=40,bg='white')
                self.e1.grid(row=1,column=2,sticky='W',columnspan=60)
                
                self.l2=tk.Label(self,text="Reg Number",bg="powderblue",)
                self.l2.grid(row=2,column=0,sticky='W')
                self.ll2=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll2.grid(row=2,column=1,sticky='W')
                self.e2=tk.Entry(self,width=40,bg='white')
                self.e2.grid(row=2,column=2,sticky='W')
                
                self.l3=tk.Label(self,text="Roll Number",bg="powderblue")
                self.l3.grid(row=3,column=0,sticky='W')
                self.ll3=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll3.grid(row=3,column=1,sticky='W')
                self.e3=tk.Entry(self,width=40,bg='white')
                self.e3.grid(row=3,column=2,sticky='W')
                
                self.l4=tk.Label(self,text="Father's Name",bg="powderblue")
                self.l4.grid(row=4,column=0,sticky='W')
                self.ll4=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll4.grid(row=4,column=1,sticky='W')
                self.e4=tk.Entry(self,width=40,bg='white')
                self.e4.grid(row=4,column=2,sticky='W')
            
                self.l5=tk.Label(self,text="Nationality",bg="powderblue")
                self.l5.grid(row=5,column=0,sticky='W')
                self.ll5=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll5.grid(row=5,column=1,sticky='W')
                self.e5=tk.Entry(self,width=40,bg='white')
                self.e5.grid(row=5,column=2,sticky='W')
                
                self.l6=tk.Label(self,text="Religion",bg="powderblue")
                self.l6.grid(row=6,column=0,sticky='W')
                self.ll6=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll6.grid(row=6,column=1,sticky='W')
                self.e6=tk.Entry(self,width=40,bg='white')
                self.e6.grid(row=6,column=2,sticky='W')
                
                self.l7=tk.Label(self,text="Caste",bg="powderblue")
                self.l7.grid(row=7,column=0,sticky='W')
                self.ll7=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll7.grid(row=7,column=1,sticky='W')
                self.e7=tk.Entry(self,width=40,bg='white')
                self.e7.grid(row=7,column=2,sticky='W')
                
                self.l8=tk.Label(self,text="Community",bg="powderblue")
                self.l8.grid(row=8,column=0,sticky='W')
                self.ll8=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll8.grid(row=8,column=1,sticky='W')
                self.e8=tk.Entry(self,width=40,bg='white')
                self.e8.grid(row=8,column=2,sticky='W')
                
                self.l9=tk.Label(self,text="Sex",bg="powderblue")
                self.l9.grid(row=9,column=0,sticky='W')
                self.ll9=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll9.grid(row=9,column=1,sticky='W')
                self.e9=tk.Entry(self,width=40,bg='white')
                self.e9.grid(row=9,column=2,sticky='W')
                
                self.l10=tk.Label(self,text="Date Of Birth",bg="powderblue")
                self.l10.grid(row=10,column=0,sticky='W')
                self.ll10=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll10.grid(row=10,column=1,sticky='W')
                self.e10=tk.Entry(self,width=40,bg='white')
                self.e10.grid(row=10,column=2,sticky='W')
                
                self.l11=tk.Label(self,text="Course Of Study",bg="powderblue")
                self.l11.grid(row=11,column=0,sticky='W')
                self.ll11=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll11.grid(row=11,column=1,sticky='W')
                self.e11=tk.Entry(self,width=40,bg='white')
                self.e11.grid(row=11,column=2,sticky='W')
                
                self.l12=tk.Label(self,text="Branch Of Study",bg="powderblue")
                self.l12.grid(row=12,column=0,sticky='W')
                self.ll12=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll12.grid(row=12,column=1,sticky='W')
                self.e12=tk.Entry(self,width=40,bg='white')
                self.e12.grid(row=12,column=2,sticky='W')
                
                self.l13=tk.Label(self,text=" Admitted On",bg="powderblue")
                self.l13.grid(row=13,column=0,sticky='W',pady=5)
                self.ll13=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll13.grid(row=13,column=1,sticky='W',pady=5,padx=30)
                self.e13=tk.Entry(self,width=40,bg='white')
                self.e13.grid(row=13,column=2,sticky='W',pady=5)
                
                self.l14=tk.Label(self,text="Receipt Number",bg="powderblue")
                self.l14.grid(row=14,column=0,sticky='W')
                self.ll14=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll14.grid(row=14,column=1,sticky='W')
                self.e14=tk.Entry(self,width=40,bg='white')
                self.e14.grid(row=14,column=2,sticky='W')
                
                self.l15=tk.Label(self,text="Receipt Date",bg="powderblue")
                self.l15.grid(row=15,column=0,sticky='W')
                self.ll15=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll15.grid(row=15,column=1,sticky='W')
                self.e15=tk.Entry(self,width=40,bg='white')
                self.e15.grid(row=15,column=2,sticky='W')
                
                self.l16=tk.Label(self,text="Mother Tongue",bg="powderblue")
                self.l16.grid(row=16,column=0,sticky='W')
                self.ll16=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll16.grid(row=16,column=1,sticky='W')
                self.e16=tk.Entry(self,width=40,bg='white')
                self.e16.grid(row=16,column=2,sticky='W')
                
                self.l17=tk.Label(self,text="Name Of State",bg="powderblue")
                self.l17.grid(row=17,column=0,sticky='W')
                self.ll17=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll17.grid(row=17,column=1,sticky='W')
                self.e17=tk.Entry(self,width=40,bg='white')
                self.e17.grid(row=17,column=2,sticky='W')
                
                self.l18=tk.Label(self,text="Present address ",bg="powderblue")
                self.l18.grid(row=18,column=0,sticky='W',pady=5)
                self.ll18=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll18.grid(row=18,column=1,sticky='W',pady=5,padx=30)
                self.e18=tk.Entry(self,width=40,bg='white')
                self.e18.grid(row=18,column=2,sticky='W',pady=5)
                
                self.l19=tk.Label(self,text="Taluk ",bg="powderblue")
                self.l19.grid(row=19,column=0,sticky='W')
                self.ll19=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll19.grid(row=19,column=1,sticky='W')
                self.e19=tk.Entry(self,width=40,bg='white')
                self.e19.grid(row=19,column=2,sticky='W')
                
                self.l20=tk.Label(self,text="City",bg="powderblue")
                self.l20.grid(row=20,column=0,sticky='W')
                self.ll20=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll20.grid(row=20,column=1,sticky='W')
                self.e20=tk.Entry(self,width=40,bg='white')
                self.e20.grid(row=20,column=2,sticky='W')
                
                self.l21=tk.Label(self,text="District",bg="powderblue")
                self.l21.grid(row=21,column=0,sticky='W')
                self.ll21=tk.Label(self,text="  :  ",bg="powderblue")
                self.ll21.grid(row=21,column=1,sticky='W')
                self.e21=tk.Entry(self,width=40,bg='white')
                self.e21.grid(row=21,column=2,sticky='W')
            
                self.la22=tk.Label(self,text="Cell Number",bg="powderblue")
                self.la22.grid(row=22,column=0,sticky='W')
                self.lla22=tk.Label(self,text="  :  ",bg="powderblue")
                self.lla22.grid(row=22,column=1,sticky='W')
                self.ea22=tk.Entry(self,width=40,bg='white')
                self.ea22.grid(row=22,column=2,sticky='W')
                
                self.la23=tk.Label(self,text="Aadhar Number",bg="powderblue")
                self.la23.grid(row=23,column=0,sticky='W')
                self.lla23=tk.Label(self,text="  :  ",bg="powderblue")
                self.lla23.grid(row=23,column=1,sticky='W')
                self.ea23=tk.Entry(self,width=40,bg='white')
                self.ea23.grid(row=23,column=2,sticky='W')
                
                 
                self.la24=tk.Label(self,text="T.C.No",bg="powderblue")
                self.la24.grid(row=24,column=0,sticky='W')
                self.lla24=tk.Label(self,text="  :  ",bg="powderblue")
                self.lla24.grid(row=24,column=1,sticky='W')
                self.ea24=tk.Entry(self,width=40,bg='white')
                self.ea24.grid(row=24,column=2,sticky='W')
                 
                self.la25=tk.Label(self,text=" Issued ON",bg="powderblue")
                self.la25.grid(row=25,column=0,sticky='W')
                self.lla25=tk.Label(self,text="  :  ",bg="powderblue")
                self.lla25.grid(row=25,column=1,sticky='W')
                self.ea25=tk.Entry(self,width=40,bg='white')
                self.ea25.grid(row=25,column=2,sticky='W')
                 
               
                
                self.la224=tk.Button(self,bg="dodgerblue",activebackground='paleturquoise',text="REGISTER",width=15,height=1,command=self.call)
                self.la224.grid(row=26,column=2,sticky='E')
                
                self.but=tk.Button(self,bg="dodgerblue",activebackground='paleturquoise',text="<-",width=10,command=lambda: master.switch_frame(pageOne))
                self.but.grid(row=26,column=0,sticky='W')
          
                
              def call(self):
                
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
                        frame =tk.Frame(master)        
                        frame.pack()
                        self.var = tk.IntVar() 
                
                        self.checkbutton = tk.Checkbutton(frame, text="Hello Checkbutton",
                                                       command=self.say_hello, variable=self.var)
                        self.checkbutton.pack()
                        #
                        self.button = tk.Button(frame, text="QUIT", fg="red", command=frame.quit)
                        self.button.pack()      
                            
                  def say_hello(self):
                        '''
                         Function Bounded to Checkbutton in command parameter, every click
                         either check or un-check print the current state of the checkbutton
                        '''        
                        print("State Changed:", self.var.get())
    
                    

if __name__ == "__main__":
    firstgui=MyFirstGui()
    firstgui.mainloop()
