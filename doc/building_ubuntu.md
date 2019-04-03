# Building for Ubuntu (and possibly for other distributions)

## Requirements

Our main requirement is to have Python 3 interpreter installed (preferably 3.5
because of build system inconsistencies). Also, you have to have installed
`gcc` or `clang` toolchain.

This is easily done on Ubuntu/Debian Linux using:
```bash
user@host $ sudo apt-get install build-essentials python3-dev python3-pip
```

Basically, `apt-get` will install all dependencies we need to properly build our
application.

## pip requirements

For the development purposes, `Pipenv` was used. However, if you would like to
use `pip`, spawn virtual environment in the directory of the repo and run the
following:

```
(venv) $ pip install pyqt5 fbs pyinstaller
```

That command will install all needed requirements for our building environment.

After that, run `fbs run` to run the application directly, or `fbs freeze` to
build the executable.