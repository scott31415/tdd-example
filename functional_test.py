from selenium import webdriver
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
        self.fail('Finish the test!') 

        # invited to enter a to-do item straight away
 
        # type "buy point cards" into a text box

        # when hitting enter, the page updates

        # still a text box inviting to add another item

        # the page updates again, now both items on the list

        # will the site remembers the list?

        # visit the URL and check the list is still there

        # happy

if __name__ == '__main__':
    unittest.main(warnings='ignore')

browser.quit()


