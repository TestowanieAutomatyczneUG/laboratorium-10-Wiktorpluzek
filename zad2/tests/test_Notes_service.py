from modules.NotesStorage import NotesStorage
from modules.NotesService import NotesService
from modules.Note import Note
from unittest.mock import *
from unittest import TestCase

class test_NotesService(TestCase):
    def setUp(self):
        self.storage = NotesStorage()
        self.storage.add = Mock(name='add')
        self.storage.clear = Mock(name='clear')
        self.storage.getAllNotesOf = Mock(name='getAllNotesOf')

    def test_NotesService_add(self):
        self.storage.add.return_value = True
        service = NotesService(self.storage)
        self.assertEqual(service.add(Note("spr", 4)), True)

    def test_NotesService_add_None(self):
        self.storage.add.return_value = True
        service = NotesService(self.storage)
        self.assertRaises(Exception, service.add, None)

    def test_NotesService_add_emptyObject(self):
        self.storage.add.return_value = True
        service = NotesService(self.storage)
        self.assertRaises(Exception, service.add, {})

    def test_NotesService_add_emptyList(self):
        self.storage.add.return_value = True
        service = NotesService(self.storage)
        self.assertRaises(Exception, service.add, [])

    def test_NotesService_averageOf(self):
        self.storage.getAllNotesOf.return_value = [5, 4, 3, 3, 2, 2, 2]
        service = NotesService(self.storage)
        self.assertEqual(service.averageOf("spr"), 3)

    def test_NotesService_averageOf_empty(self):
        self.storage.getAllNotesOf.return_value = []
        service = NotesService(self.storage)
        self.assertFalse(service.averageOf(0))

    def test_NotesService_averageOf_float(self):
        self.storage.getAllNotesOf.return_value = [5, 4, 2]
        service = NotesService(self.storage)
        self.assertAlmostEqual(service.averageOf("spr"), 3.666, 2)

    def test_NotesService_clear(self):
        self.storage.clear.return_value = []
        service = NotesService(self.storage)
        self.assertFalse(service.clear())

    def tearDown(self):
        self.storage = None
