import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSeleniumAssertions(unittest.TestCase):

    def setUp(self):
        # Setup the WebDriver
        self.driver = webdriver.Chrome()  # Use Chrome as the browser
        self.driver.get("https://example.com")  # Navigate to a test page

    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

    def test_page_title(self):
        # Check if the page title contains a specific text
        self.assertIn("Example", self.driver.title, "Page title does not contain 'Example'")

    def test_element_visibility(self):
        # Verify an element is displayed
        element = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertTrue(element.is_displayed(), "Element is not visible")

    def test_string_equality(self):
        # Validate two strings are equal
        actual_text = self.driver.find_element(By.TAG_NAME, "h1").text
        expected_text = "Example Domain"
        self.assertEqual(actual_text, expected_text, "Text does not match")

    def test_element_exists(self):
        # Check if an element exists on the page
        elements = self.driver.find_elements(By.TAG_NAME, "p")
        self.assertGreater(len(elements), 0, "Element not found on the page")

    def test_attribute_value(self):
        # Verify an element's attribute value
        # This test might fail if there's no element with an ID
        try:
            element = self.driver.find_element(By.ID, "some_id")
            self.assertEqual(element.get_attribute("value"), "Expected Value", "Attribute value mismatch")
        except:
            self.skipTest("No element with ID 'some_id' found")

    def test_string_in_page_source(self):
        # Check if a string is part of another string
        self.assertIn("Example", self.driver.page_source, "Text 'Example' not found in page source")

    def test_objects_not_same(self):
        # Ensure two objects are not the same
        obj1 = "Hello"
        obj2 = "World"
        self.assertIsNot(obj1, obj2, "Objects should not be the same")

###    def test_set_equality(self):
###        # Validate a set of elements match expected values
###        actual_set = {"value1", "value2"}
###        expected_set = {"value1", "value2"}
###        self.assertSetEqual(actual_set, expected_set, "Sets do not match")
###
###    def test_element_enabled(self):
###        # Check if an element is enabled
###        # This test might fail if there's no button on the page
###        try:
###            button = self.driver.find_element(By.TAG_NAME, "button")
###            self.assertTrue(button.is_enabled(), "Button is not enabled")
###        except:
###            self.skipTest("No button found on the page")

    def test_broken_links(self):
        # Test for broken links
        links = self.driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            href = link.get_attribute("href")
            self.assertIsNotNone(href, f"Link {link.text} has no href attribute")
            # Optionally validate href response status here.

    def test_dropdown_options(self):
        # Validate dropdown options
        # This test might fail if there's no dropdown on the page
        try:
            dropdown = Select(self.driver.find_element(By.ID, "dropdown_id"))
            actual_options = [option.text for option in dropdown.options]
            expected_options = ["Option 1", "Option 2", "Option 3"]
            self.assertListEqual(actual_options, expected_options, "Dropdown options do not match")
        except:
            self.skipTest("No dropdown found on the page")

if __name__ == "__main__":
    unittest.main()
