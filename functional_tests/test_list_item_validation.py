from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # edith goes to the home page and accidentally tries to submit an 
        # empty list item
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # the homepage refeshes, and an error message saying the list can't
        # be blank
        error = self.browser.find_element_by_css_selector('.has_error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # tries again with some text for the item, now works!
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # she decides to submit a second blank list item
        self.browser.find_element_by_id('id_new_item').send_keys('\n')
        # receives a similar warning
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has_error')
        self.assertEqual(error.text, "You can't have an empty list item")
        # she corrects it by filling in some text   
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')




