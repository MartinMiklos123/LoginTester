# Login Automation Test with Selenium

This project demonstrates an automated login testing system using a local HTML login form and Python with Selenium WebDriver

## Requirements :
1) Selenium - pip install selenium
2) Python 3.7+
3) ChromeDriver installed & added to PATH
4) Google Chrome
## Features :
1) Local html website for testing
2) validation of single username and password
3) validation from json file
## How to run:
1) clone the directory
2) run python -m http.server 8000 in the directory
## Usage:
1) python3 run.py [json file] -> validates usernames and passwords in given json file
2) python3 run.py [username] [password] -> validates single username and single password
3) python3 tests_login.py -> from tests directory, runs already prepared tests


