from fbs_runtime.application_context import ApplicationContext

import sys

from forms.general import MainWindow


class AppContext(ApplicationContext):
    def run(self):
        window = MainWindow()
        window.show()
        return self.app.exec_()


if __name__ == '__main__':
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)
