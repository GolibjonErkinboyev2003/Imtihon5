class Trip:
    def __init__(self, start_address, end_address):
        self.start_address = start_address
        self.end_address = end_address
    
    def __str__(self):
        return f"{str(self.start_address)}, {str(self.end_address)}"
