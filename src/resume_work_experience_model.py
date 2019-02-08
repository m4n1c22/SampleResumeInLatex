#
#
#       \file       :         resume_work_experience_model.py
#
#

class Resume_Work_Experience:
    def __init__(self, from_date="", to_date="", position="", organization="", location="", team_name="", tasks=""):
        self.addWorkExperienceInfo(from_date, to_date, position, organization, location, team_name, tasks)

    def addWorkExperienceInfo(self,from_date="", to_date="", position="", organization="", location="", team_name="", tasks=""):
        self.__from_date = from_date
        self.__to_date = to_date
        self.__position = position
        self.__organization = organization
        self.__location = location
        self.__team_name = team_name
        self.__tasks = tasks


    def generateWorkExperienceEntry(self):
        work_experience_entry = "\\textsc{From "+self.__from_date+" - "+ self.__to_date + "} "+ self.__grad_year +" & " + self.__position + " at \\textsc{" + self.__organization + "},"+ self.__location + "\\\\&\\emph{"+self.__team_name+"}"+"\\\\&\\footnotesize{"+self.__tasks+"}"+"\\\\\\multicolumn{2}{c}{} \\\\"
        return work_experience_entry
