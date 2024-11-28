import io
import sys
from dog import Dog

class TestDog:
    def test_is_class(self):
        '''is a class with the name "Dog".'''
        fido = Dog(name="Fido")
        assert(type(fido) == Dog)
        
    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if name is empty.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        dog = Dog(name="")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n"

    def test_name_string(self):
        '''prints "Name must be string between 1 and 25 characters." if name is not a string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Dog(name=123)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n"

    def test_name_under_25(self):
        '''prints "Name must be string between 1 and 25 characters." if name is more than 25 characters.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Dog(name="What do dogs do on their day off? Can't lie around - that's their job.")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n"

    def test_valid_name(self):
        '''saves name if it is a string between 1 and 25 characters.'''
        fido = Dog(name="Fido")
        assert(fido.name == "Fido")

    def test_breed_not_in_list(self):
        '''prints "Breed must be in list of approved breeds." if breed is not in the approved list.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Dog(name="Fido", breed="Human")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Breed must be in list of approved breeds.\n"

    def test_breed_in_list(self):
        '''saves breed if it is in the approved breed list.'''
        fido = Dog(name="Fido", breed="Pug")
        assert(fido.breed == "Pug")
