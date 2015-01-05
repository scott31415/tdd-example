from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
 
    def test_can_start_a_list_and_retrieve_it_later(self):
        # check the home page
        self.browser.get('http://localhost:8000')
        
        # the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('hi').text
        self.assertIn('To-Do', header_text)

        # invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        ) 

        # type "buy point cards" into a text box
        inputbox.send_keys('Buy Peacock feathers')

        # when hitting enter, the page updates
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
                any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # still a text box inviting to add another item
        self.fail('Finish the test!') 

        # the page updates again, now both items on the list

        # will the site remembers the list?

        # visit the URL and check the list is still there

        # happy

if __name__ == '__main__':
    unittest.main(warnings='ignore')

browser.quit()



