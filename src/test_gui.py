from Tkinter import *
import ScrolledText as scrolledtext
import subprocess
import os

from resume_education_model import Resume_Education as education
from resume_work_experience_model import Resume_Work_Experience as work_experience

education_obj =  education()
work_experience_obj = work_experience()

window = Tk()

Personal_Details_Layer = Frame(window, width=100, height=50)
Personal_Details_Layer.place(x=10,y=0)

Education_Layer = Frame(window, width=100, height=50)
Education_Layer.place(x=10,y=250)

Generate_Button_Layer = Frame(window, width=30, height=20)
Generate_Button_Layer.place(x=10,y=700)



Personal_Title = Label(Personal_Details_Layer, text="Personal Details")
Title = Label(Personal_Details_Layer, text="Title")
Title_box = Entry(Personal_Details_Layer, width = 20)
First_Name = Label(Personal_Details_Layer, text="First Name")
First_Name_box = Entry(Personal_Details_Layer, width = 20)
Middle_Name = Label(Personal_Details_Layer, text="Middle Name")
Middle_Name_box = Entry(Personal_Details_Layer, width = 20)
Last_Name = Label(Personal_Details_Layer, text="Last Name")
Last_Name_box = Entry(Personal_Details_Layer, width = 20)

Address1 = Label(Personal_Details_Layer, text="Address1")
Street_name = Entry(Personal_Details_Layer, width = 20)
Street_number = Entry(Personal_Details_Layer, width = 20)

Address2 = Label(Personal_Details_Layer, text="Address2")
Postal_code = Entry(Personal_Details_Layer, width = 20)
City = Entry(Personal_Details_Layer, width = 20)

Country = Label(Personal_Details_Layer, text="Country")
Country_box = Entry(Personal_Details_Layer, width = 20)

Education_Title = Label(Education_Layer, text="Education Details")
#Education_box = scrolledtext.ScrolledText(Education_Layer,width=100,height=20)
Grad_Month = Label(Education_Layer, text="Graduation Month")
Grad_Month_box = Entry(Education_Layer, width = 20)

Grad_Year = Label(Education_Layer, text="Graduation Year")
Grad_Year_box = Entry(Education_Layer, width = 5)

Degree = Label(Education_Layer, text="Degree")
Degree_box = Entry(Education_Layer, width = 5)

Subject = Label(Education_Layer, text="Subject")
Subject_box = Entry(Education_Layer, width = 20)

University = Label(Education_Layer, text="University")
University_box = Entry(Education_Layer, width = 50)

Location = Label(Education_Layer, text="Location")
Location_box = Entry(Education_Layer, width = 40)

thesis = Label(Education_Layer, text="Thesis")
thesis_box = Entry(Education_Layer, width = 50)

advisor = Label(Education_Layer, text="Advisor")
advisor_box = Entry(Education_Layer, width = 40)





def create_latex_document():
    f = open("res/gen_latex.tex","w")
    f.write("\\input{header}\n")
    f.write("\\begin{document}\n")
    f.write("\\pagestyle{empty}\n")
    f.write("\\font \\fb=\'\'[cmr10]\'\'\n")
    f.write("\\par{\t\\centering\n")
    f.write("\t{\n\t\t \\Huge "+ str(First_Name_box.get())+ " " +"\\textsc{"+str(Last_Name_box.get()) +"}\n")
    f.write("\t}\\bigskip\n\\par}\n")

    f.write("\\section{Education}\n")
    f.write("\\begin{tabular}{rl}\n")
    f.write(education_obj.generateEducationEntry())
    f.write("\\end{tabular}\n")
    f.write("\\end{document}\n")

def compose_education_section():
    education_obj.addEducationInfo(str(Grad_Month_box.get()),str(Grad_Year_box.get()),str(Degree_box.get()),str(Subject_box.get()),str(University_box.get()),str(Location_box.get()),str(thesis_box.get()),str(advisor_box.get()))


def run_xelatex_for_document(filename):
    os.system("cd res && xelatex "+str(filename))


def generate_pdf_document():
    compose_education_section()
    create_latex_document()
    run_xelatex_for_document("gen_latex.tex")

btn = Button(Generate_Button_Layer, text="Generate PDF Document", command=generate_pdf_document)


def load_gui():
    window.title("Gen_Sample_Resume")
    window.configure(background="white")
    window.geometry('1024x768')

    Personal_Details_Layer.configure(background="white")
    Education_Layer.configure(background="white")
    Generate_Button_Layer.configure(background="white")

    Personal_Title.grid(column=0, row=0)
    Personal_Title.configure(background="white")
    Title.grid(column=0, row=2)
    Title.configure(background="white")
    Title_box.grid(column=1, row=2)
    First_Name.grid(column=0, row=3)
    First_Name.configure(background="white")
    First_Name_box.grid(column=1, row=3)
    Middle_Name.grid(column=0, row=4)
    Middle_Name.configure(background="white")
    Middle_Name_box.grid(column=1, row=4)
    Last_Name.grid(column=0, row=5)
    Last_Name.configure(background="white")
    Last_Name_box.grid(column=1, row=5)

    Address1.grid(column=0,row=6)
    Street_name.grid(column=1,row=6)
    Street_number.grid(column=2,row=6)
    Address1.configure(background="white")
    Address2.grid(column=0,row=7)
    Postal_code.grid(column=1,row=7)
    City.grid(column=2,row=7)
    Address2.configure(background="white")
    Country.grid(column=0,row=8)
    Country.configure(background="white")
    Country_box.grid(column=1,row=8)

    Education_Title.grid(column=0, row=0)
    Education_Title.configure(background="white")
    #Education_box.grid(column=0, row=1)
    Grad_Month.grid(column=0, row=1)
    Grad_Month.configure(background="white")
    Grad_Month_box.grid(column=1, row=1)

    Grad_Year.grid(column=0, row=2)
    Grad_Year.configure(background="white")
    Grad_Year_box.grid(column=1, row=2)

    Degree.grid(column=0, row=3)
    Degree.configure(background="white")
    Degree_box.grid(column=1, row=3)

    Subject.grid(column=0, row=4)
    Subject.configure(background="white")
    Subject_box.grid(column=1, row=4)

    University.grid(column=0, row=5)
    University.configure(background="white")
    University_box.grid(column=1, row=5)

    Location.grid(column=0, row=6)
    Location.configure(background="white")
    Location_box.grid(column=1, row=6)

    thesis.grid(column=0, row=7)
    thesis.configure(background="white")
    thesis_box.grid(column=1, row=7)

    advisor.grid(column=0, row=8)
    advisor.configure(background="white")
    advisor_box.grid(column=1, row=8)

    btn.grid(column=0, row=0)

    window.mainloop()



if __name__ == '__main__':
    load_gui()
