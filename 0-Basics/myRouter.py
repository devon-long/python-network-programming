class MyRouter(object):
    "This class describes the characteristics of a router."

    # Constructor
    def __init__(self, router_name, model, serial_no, ios):
        self.router_name = router_name
        self.model = model
        self.serial_no = serial_no
        self.ios = ios

    def print_router(self, manufacture_date):
        print("The router name is: ", self.router_name)
        print("The router model is: ", self.model)
        print("The serial number is: ", self.serial_no)
        print("The IOS version is: ", self.ios)
        print("The model and date combined: ", self.model + manufacture_date)
