from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json


class Tester:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.error_message = None

    def connect(self):
        """
        Opens the local login page in the browser

        :return: self - the current Tester instance
        """

        self.driver.get("http://localhost:8000/index.html")
        return self

    def test(self, username, password):
        """
        Tests the login form with the provided username and password
        Fills login fields, submits the form and checks for success or
        message error

        :param username: username to test
        :param password: password to test
        :return: self - the current Tester instance
        """

        self.driver.find_element(By.ID, "username").send_keys(username)

        self.driver.find_element(By.ID, "password").send_keys(password)

        self.driver.find_element(By.ID, "login").click()

        if "redirect" in self.driver.current_url:
            self.error_message = "success"

            # redirect back to login page after successful login

            self.driver.get("http://localhost:8000/index.html")

            return self

        # wait until error message loads
        time.sleep(1)

        error_message = self.driver.find_element(By.ID, "error-message")

        self.error_message = error_message.text

        return self

    def test_from_json(self, test_file):

        """
        Runs tests from file
        :param test_file: json file
        :return: None
        """

        if test_file.split(".")[1] != "json":
            raise IOError("test file must be in json format")

        with open(test_file, "r") as f:
            file = json.load(f)

        for case in file:
            username = case["username"]
            password = case["password"]
            expected = case["expected"]
            message = self.test(username, password).get_message()
            try:
                assert expected == message
            except AssertionError:
                print(f"Wrong result for [username: {username}, password: {password}]")
                print(f"expected: [{expected}], but got instead [{message}]")

    def stdout(self):
        """
        prints the last error or success message to the console

        :return: None
        """

        print(self.error_message)

    def get_message(self):

        """
        Returns the last recorded message from login attempt

        :return: The message from the login page (error or success)
        """

        return self.error_message
