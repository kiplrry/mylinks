

class Action():
    id = None
    name = None

    def __init__(self) -> None:
        pass



class Create(Action):
    def __init__(self, cls, *args, **kwargs):
        return cls(*args, **kwargs)

class Read(Action):
    pass

class Update(Action):
    pass

class Delete(Action):
    pass



@
def create()

admin, user
owner, viewer