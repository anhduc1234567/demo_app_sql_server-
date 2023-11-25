class NameError(Exception):
    def __init__(self,main,message = ' '):
        super().__init__(message)
        self.main = main
        self.message = message

    def __str__(self):
        return f'NameError: {self.message} {self.main}'

class BirthError(Exception):
    def __init__(self,main,message = ' '):
        super().__init__(message)
        self.main = main
        self.message = message

    def __str__(self):
        return f'BirthError: {self.message} {self.main}'

class EmailError(Exception):
    def __init__(self,main,message = ' '):
        super().__init__(message)
        self.main = main
        self.message = message

    def __str__(self):
        return f'EmailError: {self.message} {self.main}'
class GpaError(Exception):
    def __init__(self,main,message = ' '):
        super().__init__(message)
        self.main = main
        self.message = message

    def __str__(self):
        return f'GpaError: {self.message} {self.main}'

class AddressError(Exception):
    def __init__(self,main,message = ' '):
        super().__init__(message)
        self.main = main
        self.message = message

    def __str__(self):
        return f'AddressError: {self.message} {self.main}'