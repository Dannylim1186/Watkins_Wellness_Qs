import pytest
import sys

def run_tests():
    args = [
        "--html=report.html",
        "--self-contained-html",
        "-v", #for verbose output
        "tests/"
    ]
    sys.exit(pytest.main(args))

if __name__ == "__main__":
    run_tests()
