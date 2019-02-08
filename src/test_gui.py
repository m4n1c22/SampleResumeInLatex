from Tkinter import *
import ScrolledText as scrolledtext

window = Tk()
Personal_Title = Label(window, text="Personal Details")
Title = Label(window, text="Title")
Title_box = Entry(window, width = 20)
First_Name = Label(window, text="First Name")
First_Name_box = Entry(window, width = 20)
Middle_Name = Label(window, text="Middle Name")
Middle_Name_box = Entry(window, width = 20)
Last_Name = Label(window, text="Last Name")
Last_Name_box = Entry(window, width = 20)
Education_Title = Label(window, text="Education Details")
Education_box = scrolledtext.ScrolledText(window,width=100,height=20)

def create_latex_document():
    pass


def generate_pdf_document():
    print "hello" + " " +  First_Name_box.get() + " " + Middle_Name_box.get() + " " + Last_Name_box.get()

btn = Button(window, text="Generate PDF Document", command=generate_pdf_document)


def load_gui():
    window.title("Gen_Sample_Resume")
    window.configure(background="white")
    window.geometry('1024x768')



    Personal_Title.grid(column=0, row=0)
    Personal_Title.configure(background="white")
    Title.grid(column=0, row=1)
    Title.configure(background="white")
    Title_box.grid(column=1, row=1)
    First_Name.grid(column=0, row=2)
    First_Name.configure(background="white")
    First_Name_box.grid(column=1, row=2)
    Middle_Name.grid(column=0, row=3)
    Middle_Name.configure(background="white")
    Middle_Name_box.grid(column=1, row=3)
    Last_Name.grid(column=0, row=4)
    Last_Name.configure(background="white")
    Last_Name_box.grid(column=1, row=4)

    Education_Title.grid(column=0, row=7)
    Education_Title.configure(background="white")
    Education_box.grid(column=1, row=7)
    btn.grid(column=0, row=12)

    window.mainloop()



if __name__ == '__main__':
    load_gui()
