class Employee:
    def __init__(self,tname,tcode,tbs):
        self.teacher_name=tname
        self.teacher_code=tcode
        self.teacher_basic=tbs


    def calculate(self):
        if self.teacher_basic<10000:
            self.teacher_da=self.teacher_basic*0.2
            self.teacher_hra=self.teacher_basic*0.25
            self.teacher_pf=self.teacher_basic*0.05
        else:
            self.teacher_da = self.teacher_basic * 0.1
            self.teacher_hra = self.teacher_basic * 0.15
            self.teacher_pf = self.teacher_basic * 0.03
        self.teacher_ns=self.teacher_basic+self.teacher_da+self.teacher_hra-self.teacher_pf

    def display(self):
        print("Name       :", self.teacher_name)
        print("Empcode     :", self.teacher_code)
        print("Basic Salary :", self.teacher_basic)
        print("DA            :", self.teacher_da)
        print("HRA           :", self.teacher_hra)
        print("PF            :", self.teacher_pf)
        print("Net Salary     :", self.teacher_ns)
class teacher(Employee):
    def _init_(self,name,code,bse,dept):
        Empolye._init_(self,name,code,bse)
        self.department=dept
        self.student=[]
    def make_attendance(self,n):
        self.count=n
        print("enter the attendance rollno wise(1-present/0-absent)")
        for i in range(0,n):
            att=int(input())
            self.student.append(att)
    def display_attendance(self):
        print("list of present student")
        for i in range(0,self.count):
            if self.student[i]==1:
                i+=1
                print('   ',i)
        print("list of absent student")
        for i in range(0,self.count):
            if self.student[i]==0:
                i+=1
                print('    ',i)
    def display(self):
        print("Name       :", self.teacher_name)
        print("Empcode     :", self.techer_code)
        print("Basic Salary :", self.techer_basic)
        print("DA            :", self.techer_da)
        print("HRA           :", self.techer_hra)
        print("PF            :", self.techer_pf)
        print("Net Salary     :", self.techer_ns)
teacher_list=[]
m=int(input("count of teacher"))
for i in range(0,m):
    name=input("enter the teacher name :")
    code=input("enter the code of teacher :")
    bse=int(input("enter the basic salary :"))
    dept=input("enter the department :")
    no=int(input("enter the number of student "))
    obj=teacher(name,code,bse,dept)
    obj.make_attendance(no)
    obj.calculate()
    teacher_list.append(obj)
for i in range(0,m):
    teacher_list[i].display()
    teacher_list[i].display_attendance()