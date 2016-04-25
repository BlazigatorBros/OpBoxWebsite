import os, __main__
import inspect
from time import gmtime, strftime

class Logger:
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    log_dir = os.path.join(BASE_DIR, "logs/")

    @staticmethod
    def timestamp():
        return '[' + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + '] '

    def __init__(self, logfile=None):
        if not logfile:
            self.logfile = Logger.log_dir + os.path.basename(__main__.__file__) + ".log"
        else:
            self.logfile = logfile

        if not os.path.exists(self.logfile):
            open(self.logfile, 'w').close()

    def log(self, line):

        with open(self.logfile, 'a') as f:
            f.write(Logger.timestamp() + str(line) +'\n')

    def clear(self):
        open(self.logfile, 'w').close()
