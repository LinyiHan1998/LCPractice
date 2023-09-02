class Limit:
    def get_limit():
        pass

class Product:
    def __init__(self,name) -> None:
        pass
    def __del__(self):
        pass
    def track(self):
        pass

class UserLimitExceeded:
    def __init__(self,name,limit) -> None:
        return "Product {} cannot be created. Maximum {} products allowed".format(name,limit)