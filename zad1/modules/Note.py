class Note:

    def __init__(self, name, note):
        if type(name) is not str:
            raise Exception()
        else:
            if name == "":
                raise Exception()
            else:
                self.name = name

        if type(note) in [float, int]:
            if 2 <= note <= 6:
                self.note = note
            else:
                raise ValueError()
        else:
            raise TypeError()

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note
