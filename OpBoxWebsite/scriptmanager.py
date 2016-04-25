from glob import glob
import subprocess, os
import settings

class ScriptManager:

    script_dir = settings.SCRIPTS_DIR
    exclude = ["logger.py", "scriptmanager.py", "__init__.py"]
    current_script_name = None

    @staticmethod
    def getSource(script):
        """
        gets the source code of the given script
        """
        with open(ScriptManager.script_dir + script, 'r') as f:
                return f.read()

    @staticmethod
    def getScripts():
        """
        returns list of user defined scripts
        """
        scripts = [os.path.basename(s) for s in glob(ScriptManager.script_dir + "*.py")]
        return [s for s in scripts if not s in ScriptManager.exclude]

    @staticmethod
    def run(script):
        """
        runs the given script and prints all output to the end of the logfile.
        """
        with open(ScriptManager.script_dir + "script_queue", 'w') as f:
                f.write(script)
