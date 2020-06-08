import pandas as pd
import os
##################################################################################################
def non_empty(fpath):
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0
##################################################################################################
def addrow():  #function for adding row in the table
    choose=int(input("select 1 for bba or 2 for bsc : "))
    if choose==1:                               
        student = non_empty('studentBBA.txt')   #text file for storing BBA student data
        grades = non_empty('gradesBBA.txt')     #text file for storing BBA student grades and attendance data
        Name = str(input("Add name of student = "))
        gender=str(input("Add gender(M/F) of student = "))
#taking details from user
        BAM_Grade=float(input("BAM CGPA = "))
        BAM_Attendance=float(input("BAM Attendance = "))
        FoAM_Grade=float(input("FoAM CGPA = "))
        FoAM_Attendance=float(input("FoAM Attendance = "))             
        if  student == False:
            F = pd.DataFrame({'roll_no':[1],'NAME':[Name],'gender':[gender]})            
            F.to_csv('studentBBA.txt',index=False, header=True)
            print(F)    
        else:
            F = pd.read_csv('studentBBA.txt', sep=",", header=None)            
            F = F.append(pd.Series([F.shape[0]+1, Name, gender]),ignore_index=True)
            F.to_csv('studentBBA.txt',index=False, header=False)
            print(F)            ###saving header name in the file if it is empty and appending the values to the columns as entered by user and assigning roll no. automatically
            
        if  grades == False:
            F = pd.DataFrame({'roll_no':[1],'BAM_Grade':[BAM_Grade],'BAM_Attendance':[BAM_Attendance],'FoAM_Grade':[FoAM_Grade],'FoAM_Attendance':[FoAM_Attendance]})
            
            F.to_csv('gradesBBA.txt',index=False, header=True)
            print(F)
        else:
            F = pd.read_csv('gradesBBA.txt', sep=",", header=None)
            
            F = F.append(pd.Series([F.shape[0]+1, BAM_Grade, BAM_Attendance, FoAM_Grade, FoAM_Attendance]),ignore_index=True)
            F.to_csv('gradesBBA.txt',index=False, header=False)
            print(F)
        print("Student enrolled!!!")
    if choose==2:
        studentbsc = non_empty('studentBSC.txt')
        gradesbsc = non_empty('gradesBSC.txt')
        Name = str(input("Add  name of student = "))
        gender=str(input("Add gender(M/F)  = "))

        IPL_Grade=float(input("IPL CGPA = "))
        IPL_Attendance=float(input("IPL Attendance = "))
        TSD_Grade=float(input("TSD CGPA= "))
        TSD_Attendance=float(input("TSD Attendance = "))             

        if  studentbsc == False:
            F = pd.DataFrame({'roll_no':[50],'NAME':[Name],'gender':[gender]})
            
            F.to_csv('studentBSC.txt',index=False, header=True)
            print(F)
        else:
            F = pd.read_csv('studentBSC.txt', sep=",", header=None)
            
            F = F.append(pd.Series([F.shape[0]+50, Name, gender]),ignore_index=True)
            F.to_csv('studentBSC.txt',index=False, header=False)
            print(F)
        if  gradesbsc == False:
            F = pd.DataFrame({'roll_no':[50],'IPL_Grade':[IPL_Grade],'IPL_Attendance':[IPL_Attendance],'TSD_Grade':[TSD_Grade],'TSD_Attendance':[TSD_Attendance]})
            
            F.to_csv('gradesBSC.txt',index=False, header=True)
            print(F)
        else:
            F = pd.read_csv('gradesBSC.txt', sep=",", header=None)
            
            F = F.append(pd.Series([F.shape[0]+50, IPL_Grade, IPL_Attendance, TSD_Grade, TSD_Attendance]),ignore_index=True)
            F.to_csv('gradesBSC.txt',index=False, header=False)
            print(F)
        print("student enrolled!!!")
####################################################################################
#limitation: * BBA students hAve roll no. less than 50
#            * BSC students starts from roll no. 50
#            * user will have to enter correct details
#            * two corses are there in BBA and BSC
##########################################################################################
def viewdata():   ##viewing students data 
    print('All BBA students : ')
    F1 = pd.read_csv('studentBBA.txt', sep=",")
    F2 = pd.read_csv('gradesBBA.txt', sep=",",header=0)
    F=pd.concat([F2,F1['NAME']], axis=1)
    print(F)
    print('All BSc students :  ')
    G1 = pd.read_csv('studentBSC.txt', sep=",")
    G2 = pd.read_csv('gradesBSC.txt', sep=",",header=0)
    G=pd.concat([G2,G1['NAME']], axis=1)    #concatenating students data with their grades
    print(G)
##########################################################################################
def coursedata():
    print('Enter 1 to view all courses details data of selected student ')     #to view specific students course detail
    print('Enter 2 to view specific course data of student')
    d= int(input('please select your choice :  '))
    if d==1:
     b=int(input('Enter roll_no of student  : '))
     if b<=49:
         F1 = pd.read_csv('studentBBA.txt', sep=",",header=0)
         F2 = pd.read_csv('gradesBBA.txt', sep=",",header=0)
         F=pd.concat([F2,F1['NAME']], axis=1)           #concatenating two tables
         print(F.loc[F2['roll_no']==b])                 #retrieving the specific roll no. row from the concatenated table
     elif b>49:
         F1 = pd.read_csv('studentBSC.txt', sep=",",header=0)
         F2 = pd.read_csv('gradesBSC.txt', sep=",",header=0)
         F=pd.concat([F2,F1['NAME']], axis=1)
         print(F.loc[F2['roll_no']==b])
         
    elif d==2 :

      b=int(input('Enter roll_no of student  : '))
      if b<=49:             #for roll No. less than 50 i e for BBA students
          print('To get details of BAM course enter BAM  :  ')
          print('To get details of FoAM course enter FoAM  :  ')
          course=str(input('select course   :  '))
          if course == 'BAM'or'bam':              
             F1 = pd.read_csv('studentBBA.txt', sep=",",header=0)
             F2 = pd.read_csv('gradesBBA.txt', sep=",",header=0)
             F=pd.concat([F1['roll_no'],F1['NAME'],F2['BAM_Grade'],F2['BAM_Attendance']], axis=1)
             print(F.loc[F2['roll_no']==b])

          elif course == 'FoAM'or'foam'or'FOAM':
             F1 = pd.read_csv('studentBBA.txt', sep=",",header=0)
             F2 = pd.read_csv('gradesBBA.txt', sep=",",header=0)
             F=pd.concat([F1['roll_no'],F1['NAME'],F2['FoAM_Grade'],F2['FoAM_Attendance']], axis=1)
             print(F.loc[F2['roll_no']==b])

      else:
          print('To get details of IPL course enter IPL :  ')
          print('To get details of TSD course enter TSD :  ')
          course=str(input('Select course   :  '))

          if course == 'IPL'or'ipl':              
             F1 = pd.read_csv('studentBSC.txt', sep=",",header=0)
             F2 = pd.read_csv('gradesBSC.txt', sep=",",header=0)
             F=pd.concat([F1['roll_no'],F1['NAME'],F2['IPL_Grade'],F2['IPL_Attendance']], axis=1)
             print(F.loc[F2['roll_no']==b])
          elif course == 'TSD'or'tsd':
             F1 = pd.read_csv('studenbsct.txt', sep=",",header=0)
             F2 = pd.read_csv('gradescbsc.txt', sep=",",header=0)
             F=pd.concat([F1['roll_no'],F1['NAME'],F2['TSD_Grade'],F2['TSD_Attendance']], axis=1)
             print(F.loc[F2['roll_no']==b])
    else :
     print('please enter the choice')
     return coursedata()
###############################################################################   
def tracka():
    option = int(input('please enter 1 for tracking Attendance or 2 for tracking grades  :  '))
    if option==1:
        b=int(input('Enter roll_no of student  : '))
        if b<=49:
            F1 = pd.read_csv('studentBBA.txt', sep=",",header=0)
            F2 = pd.read_csv('gradesBBA.txt', sep=",",header=0)
            F=pd.concat([F1['roll_no'],F1['NAME'],F2['BAM_Attendance'],F2['FoAM_Attendance']], axis=1)
            print(F.loc[F2['roll_no']==b])                          # showing table with the given roll no. and the attendance in both the courses
            G= F2.loc[F2['roll_no']==b]
            T=(G.BAM_Attendance +G.FoAM_Attendance)/2               #taking average of all the attendance
            print('overall Attendance of student with roll no. ',b, ' is ')
            print(T)
        else:
            F1 = pd.read_csv('studentBSC.txt', sep=",",header=0)
            F2 = pd.read_csv('gradesBSC.txt', sep=",",header=0)
            F=pd.concat([F1['roll_no'],F1['NAME'],F2['IPL_Attendance'],F2['TSD_Attendance']], axis=1)
            print(F.loc[F2['roll_no']==b])
            G= F2.loc[F2['roll_no']==b]
            T=(G.IPL_Attendance +G.TSD_Attendance)/2
            print('overall Attendance of student with roll no. ',b, ' is ')
            print(T)
    if option==2:
        b=int(input('enter roll_no of student  : '))
        if b<=49:
            F1 = pd.read_csv('studentBBA.txt', sep=",",header=0)
            F2 = pd.read_csv('gradesBBA.txt', sep=",",header=0)
            F=pd.concat([F1['roll_no'],F1['NAME'],F2['BAM_Grade'],F2['FoAM_Grade']], axis=1)
            print(F.loc[F2['roll_no']==b])
            G= F2.loc[F2['roll_no']==b]
            T=(G.BAM_Grade +G.FoAM_Grade)/2
            print('overall CGPA of student with roll no. ',b, ' is ')
            print(T)
        else:
            F1 = pd.read_csv('studentBSC.txt', sep=",",header=0)
            F2 = pd.read_csv('gradesBSC.txt', sep=",",header=0)
            F=pd.concat([F1['roll_no'],F1['NAME'],F2['IPL_Grade'],F2['TSD_Grade']], axis=1)
            print(F.loc[F2['roll_no']==b])
            G= F2.loc[F2['roll_no']==b]
            T=(G.IPL_Grade +G.TSD_Grade)/2
            print('overall CGPA of student with roll no. ',b, ' is ')
            print(T)
            

####################################################################################

def update():
    print('Enter 1 to update Attendance')           ##taking input from 
    print('Enter 2 to update grades')
    select = int(input('please select your choice  :    '))
    if select==1:
        x=int(input('Enter roll no. of student  : '))    
        if x<=49 :
         print('Enter BAM to update BAM course  :  ')
         print('Enter FoAM to update FoAM course  :  ')
         y=str(input('Enter course : '))
         z=float(input('Enter new Attendance : ')) 
         if y== 'BAM'or 'bam':                    
                F = pd.read_csv('gradesBBA.txt', sep=",",header = 0)
                c=F.roll_no==x                          ## assigning c as the roll no. column of the grades table
                y= 'BAM_Attendance'                 
                F.at[c,y]=z                             ##command to update c value presesnt in y column by the value of z
                F.to_csv('gradesBBA.txt',index=False,header=True)
                print('updated Attendance in the table ----->')
                print(F)
         elif y== 'FoAM'or'FOAM'or'foam':           #taking input in all the forms whether in                  
                F = pd.read_csv('gradesBBA.txt', sep=",",header = 0)
                c=F.roll_no==x
                y='FoAM_Attendance'
                F.at[c,y]=z   
                F.to_csv('gradesBBA.txt',index=False,header=True)
                print('updated Attendance in the table ----->')
                print(F)
        else:
         print('enter IPL to update IPL course  :  ')
         print('enter TSD to update TSD course  :  ')
         y=str(input('enter course : '))
         z=float(input('enter new Attendance : '))
         if y=='IPL'or'ipl':               
                F = pd.read_csv('gradesBSC.txt', sep=",",header = 0)
                c=F.roll_no==x
                y='IPL_Attendance'
                F.at[c,y]=z   
                F.to_csv('gradesBSC.txt',index=False,header=True)
                print('updated Attendance in the table ----->')
                print(F)
         if y=='TSD'or'tsd':               
                F = pd.read_csv('gradesBSC.txt', sep=",",header = 0)
                c=F.roll_no==x
                y='TSD_Attendance'
                F.at[c,y]=z   
                F.to_csv('gradesBSC.txt',index=False,header=True)
                print('updated Attendance in the table ----->')
                print(F)            
    if select==2:
        x=int(input('enter roll no. of student  : '))    
        if x<=49 :
         print('Enter BAM to update BAM course  :  ')
         print('Enter FoAM to update FoAM course  :  ')
         y=str(input('Enter course : '))
         z=float(input('Enter new Attendance : '))

         if y== 'IPL'or'ipl':                    
                F = pd.read_csv('gradesBBA.txt', sep=",",header = 0)
                c=F.roll_no==x
                y='IPL_Attendance'
                F.at[c,y]=z   
                F.to_csv('gradesBBA.txt',index=False,header=True)
                print('updated grade in the table ----->')
                print(F)
         if y== 'TSD'or'tsd':                    
                F = pd.read_csv('gradesBBA.txt', sep=",",header = 0)
                c=F.roll_no==x
                y='TSD_Attendance'
                F.at[c,y]=z   
                F.to_csv('gradesBBA.txt',index=False,header=True)
                print('updated grade in the table ----->')
                print(F)
                

        else:
         print('Enter IPL to update IPL course  :  ')
         print('Enter TSD to update TSD course  :  ')
         y=str(input('Enter course : '))
         z=float(input('Enter new Attendance : '))

         if y== 'IPL'or'ipl':                    
                F = pd.read_csv('gradesBSC.txt', sep=",",header = 0)
                c=F.roll_no==x
                y='IPL_Attendance'
                F.at[c,y]=z   
                F.to_csv('gradesBSC.txt',index=False,header=True)
                print('updated grade in the table ----->')
                print(F)
         if y== 'TSD'or'tsd':                    
                F = pd.read_csv('gradesBSC.txt', sep=",",header = 0)
                c=F.roll_no==x
                y='TSD_Attendance'
                F.at[c,y]=z   
                F.to_csv('gradesBSC.txt',index=False,header=True)
                print('updated grade in the table ----->')
                print(F)
##############################################################################        
def delete():
    x=int(input ('student roll no. : '))
    if x<=49:        
        F = pd.read_csv('studentBBA.txt', sep=",",header=0)
        F = F[F.roll_no != x]    #to delete the row with given roll no.
        F.to_csv('studentBBA.txt',index=False)
        print(F)
        F = pd.read_csv('gradesBBA.txt', sep=",", header=0)
        F = F[F.roll_no != x]
        F.to_csv('gradesBBA.txt',index=False)
        print(F)
    else:
        F = pd.read_csv('studentBSC.txt', sep=",",header=0)
        F = F[F.roll_no != x]
        F.to_csv('studentBSC.txt',index=False)
        print(F)
        F = pd.read_csv('gradesBSC.txt', sep=",", header=0)
        F = F[F.roll_no != x]
        F.to_csv('gradesBSC.txt',index=False)
        print(F)
##########################################################################################
def report():               ##fucnction to give annual performance of student 
    x= int(input('Enter roll no of student : '))
    S1= pd.read_csv('studentBBA.txt', sep=",",header=0)
    S2=pd.read_csv('studentBSC.txt', sep=",",header=0)
    def name(y):         ##retreiving name of student from roll no. based on the program
        if x<49:
            y=S1.loc[S1['roll_no'] == x, ['NAME']]
            return y
        else:
            y=S2.loc[S2['roll_no'] == x, ['NAME']]
            return y

    def program(x):     #selecting program of student
            if x<49:
             y=("BBA")
             return(y)
            else:
             y=("BSc")
             return(y)
            
    
    def attand(x):      #calculating overall attendance
     if x<=49:
            
            F2 = pd.read_csv('gradesBBA.txt', sep=",",header=0)
            G= F2.loc[F2['roll_no']==x]
            T=(G.BAM_Attendance +G.FoAM_Attendance)/2
            return(T)
     else:
            F2 = pd.read_csv('gradesBSC.txt', sep=",",header=0)
            G= F2.loc[F2['roll_no']==x]
            T=(G.IPL_Attendance +G.TSD_Attendance)/2
            return(T)
    def grade(x):       ##calculating overall grade
        if x<=49:
            F2 = pd.read_csv('gradesBBA.txt', sep=",",header=0)
            G= F2.loc[F2['roll_no']==x]
            T=((G.BAM_Grade +G.FoAM_Grade)/2)
            return(T)
        else:
            F2 = pd.read_csv('gradesBSC.txt', sep=",",header=0)
            G= F2.loc[F2['roll_no']==x]
            T=(G.IPL_Grade +G.TSD_Grade)/2
            return(T)
    
    print('-----------------------------------------------')
    print('--------------ANNUAL PERFORMANCE---------------')
    print('---------------PROGRAM : ',program(x),'-----------------')
    print(name(x))
    print('----------------------------------roll no.= ',x)
    print('---OVERALL Attendance--------------------------')
    print(attand(x))
    print('---OVERALL CGPA--------------------------------')
    print(grade(x))
    print('-----------------------------------------------')

##########################################################################################
            #first user interface screen of the program
print('-----------------------------------------------')
print('--------------STUDENT MANAGEMENT---------------')
print('--------------------SYSTEM---------------------')
print('-----------------------------------------------')
print(' select from the options                   ')
print(' Enter 1 to enroll new student with course details          ')
print(' Enter 2 to view all student personal data          ')
print(' Enter 3 to view student course data from roll no.          ')
print(' Enter 4 to track Attendance & grades of student by their roll no.          ')
print(' Enter 5 to update Attendance & grades of student          ')
print(' Enter 6 to delete student data ')       
print(' Enter 7 to see annual performance of student ')       
enter = int(input('enter : '))
if enter == 1 :
        addrow()
        main()
if enter == 2:
        viewdata()
        main()
if enter == 3:
        coursedata()
        main()
if enter == 4:
        tracka()
        main()
if enter == 5:
        update()
        main()
if enter == 6:
        delete()
        main()
if enter == 7:
        report()
        main()
else:
        print("please select one option")
###########################################################################################################
        
def main():
    enter=input('type Y to start again : ')#running the program again
    if enter == 'Y'or 'y':
        stdmanage()
    elif enter!= 'Y'or 'y' :
        print('bye')


#############################################################################################################
