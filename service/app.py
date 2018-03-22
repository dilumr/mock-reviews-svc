
# This indirection handles most of the ugly issues with python import
# breakages when running a script in a package.

from reviews.service import main

if __name__ == "__main__":
    main()
