from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # edith goes to the home page and accidentally tries to submit an 
        # empty list item

        # the homepage refeshes, and an error message saying the list can't
        # be blank

        # tries again with some text for the item, now works!
        # she decides to submit a second blank list item
        # receives a similar warning
        # she corrects it by filling in some text   
        self.fail("write me!") 




