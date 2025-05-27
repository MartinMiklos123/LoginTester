import sys
from loginAutomationTest import Tester

loginTester = Tester()


def helper():
    print("Usage:")
    print(" *python run.py [json_file]")
    print(" *python run.py [username] [password]")


def main():
    loginTester.connect()
    args = sys.argv
    match len(args):
        case 2:
            loginTester.test_from_json(args[1])
        case 3:
            loginTester.test(args[1], args[2]).stdout()
        case _:
            helper()


if __name__ == "__main__":
    main()
