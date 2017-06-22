from lab.models.box import Box


class ReceiveBox():
    
    def __init_(self,box= None):
        self.box = box
        
    def is_box_valid(self):
        return isinstance(self.box, Box)
    
    def receiveBox(self):
        if isinstance(self.box, Box):
            self.box.accept_box = True
            return self.box.accept_box
        return False