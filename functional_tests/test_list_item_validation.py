from .base import FunctionalTest
import time

class ItemValidationTest(FunctionalTest):
    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')
    def test_cannot_add_empty_list_items(self):
        # edith goes to the home page and accidentally tries to submit an 
        # empty list item
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # the homepage refeshes, and an error message saying the list can't
        # be blank
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # tries again with some text for the item, now works!
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # she decides to submit a second blank list item
        self.get_item_input_box().send_keys('\n')
        # receives a similar warning
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")
        # she corrects it by filling in some text   
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
 
    def test_cannot_add_duplicate_items(self):
        # edith goes to the home page and start a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')

        # she accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy wellies\n')
        
        # she sees a helpful error message
        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this in your list")       
    def test_error_messages_are_created_on_input(self):
        # edith starts a new list that causes validation error
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        # she starts typing inbox to clear the error
        self.get_item_input_box().send_keys('a')
        time.sleep(10)
 
        # she is pleased to see that the error messages disappear
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())  
          


