#
#
#       \file       :         resume_education_model.py
#
#

class Resume_Education:
    def __init__(self, grad_month="", grad_year="", degree_name="", subject="", university="", location="", thesis="",advisor=""):
        self.addEducationInfo(grad_month, grad_year, degree_name, subject, university, location, thesis, advisor)

    def addEducationInfo(self, grad_month="", grad_year="", degree_name="", subject="", university="", location="", thesis="",advisor=""):
        self.__grad_month = grad_month
        self.__grad_year = grad_year
        self.__degree_name = degree_name
        self.__subject = subject
        self.__university = university
        self.__location = location
        self.__thesis = thesis
        self.__advisor = advisor

    def generateEducationEntry(self):
        education_entry = "\\textsc{"+self.__grad_month+"} "+ self.__grad_year +" & " + self.__degree_name + " in \\textsc{" + self.__subject + "},\\\\& \\textbf{"+self.__university+"}, "+ self.__location + "\\\\ & Thesis:" + self.__thesis + "\\\\& Advisor: " + self.__advisor + "\n"
        return education_entry
