from modules.NotesStorage import NotesStorage


class NotesService:
    def __init__(self, storage: NotesStorage):
        self.storage = storage

    def add(self, note):
        return self.storage.add(note)

    def averageOf(self, name):
        allNotes = self.storage.getAllNotesOf(name)
        numOfNotes = len(allNotes)
        if numOfNotes == 0:
            return 0
        return sum(allNotes) / numOfNotes

    def clear(self):
        return self.storage.clear()
