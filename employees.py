# Create a class that contains information about employees of a company 
# and define methods to get employee name, job title, and start date.

class Company(object):

    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date

    def getName(self):
        return self.name

    def getJobTitle(self):
        return self.title

    def getStartDate(self):
        return self.start_date

new_company = Company("Cool Guys, Inc.", "Manager of Awesome", "9/9/99")

my_name = new_company.getName()
my_job_title = new_company.getJobTitle()
my_start_date = new_company.getStartDate()

print ("{0} Employee Info:\n  {1} hired {2}".format(my_name, my_job_title, my_start_date))

    # Add the remaining methods to fill the requirements above