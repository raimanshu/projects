class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is : {self.name}")
        print(f"Train is : {self.train}")

raimanshuApplication = RailwayForm()
raimanshuApplication.name = "Himanshu"
raimanshuApplication.train = "Rajdhani Express"

raimanshuApplication.printData()