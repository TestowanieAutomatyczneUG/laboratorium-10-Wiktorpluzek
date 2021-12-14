import unittest
from assertpy import assert_that
from modules.Note import Note

class NoteTest(unittest.TestCase):
    def test_get_Name(self):
        note = Note("spr", 4)
        assert_that(note.get_name()).is_equal_to("spr")

    def test_get_Note(self):
        note = Note("spr", 4)
        assert_that(note.get_note()).is_equal_to(4)

    def test_get_Note_Lower(self):
        note = Note("spr", 2)
        assert_that(note.get_note()).is_equal_to(2)

    def test_get_Note_Upper(self):
        note = Note("spr", 6)
        assert_that(note.get_note()).is_equal_to(6)
    def test_get_Name_empty(self):
        self.assertRaises(Exception, Note, "", 3)

    def test_get_Name_none(self):
        self.assertRaises(Exception, Note, None, 3)

    def test_get_Note_too_low(self):
        self.assertRaises(Exception, Note, "testowanie", 1)

    def test_get_Note_too_high(self):
        self.assertRaises(Exception, Note, "testowanie", 7)