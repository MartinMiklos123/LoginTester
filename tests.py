from loginAutomationTest import Tester

loginTester = Tester().connect()


def run_tests():
    # TESTS for wrong username

    print("Testing for wrong username...")

    username_tests = [("xm", "password1234_"),
                      ("user name", "password1234_"),
                      ("user@name", "password1234_"),
                      ("user!", "password1234_"),
                      ("user         name", "pass")]
    for user in username_tests:
        username, password = user
        loginTester.test(username, password).stdout()

    print("------------------------------------------")

    # TESTS for wrong password

    print("Testing for wrong password")

    password_tests = [("xmiklos1", "p"),
                      ("xbrun", "password"),
                      ("test123", "password12345632132321"),
                      ("admin123", ""),
                      ("admin123", "mypass")]
    for user in password_tests:
        username, password = user
        loginTester.test(username, password).stdout()

    print("------------------------------------------")

    # TESTS for registered user, but wrong password

    user_tests = [("xmiklos1", "password123456"),
                  ("xmiklos1", "password_password_")]

    print("Testing for registered user with wrong password")

    for user in user_tests:
        username, password = user
        loginTester.test(username, password).stdout()

    print("------------------------------------------")

    # TESTS for successful login

    print("Testing for successful login")

    user_tests = [("xmiklos1", "password1234_"),
                  ("xmiklos12421", "password1234_")
                  ]

    for user in user_tests:
        username, password = user
        loginTester.test(username, password).stdout()

    # run tests from json

    loginTester.test_from_json("tests.json")




if __name__ == "__main__":
    run_tests()
