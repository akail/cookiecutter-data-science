import sys

REQUIRED_PYTHON = "python3"

def main():
    system_major = sys.version_info.major

    if system_major == 2:
        raise ValueError("Python version not supported by this project. Found: Python {}".format(
            sys.version
        ))

    # TODO: Check for minor version greater than 3.7 AAK 2019-12-11
    # TODO: Check for required packages AAK 2019-12-11
    


    print(">>> Development environment passes all tests!")


if __name__ == '__main__':
    main()
