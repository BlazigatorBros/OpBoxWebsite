from django.http import HttpResponse
from django.shortcuts import render
from scripts.logger import Logger
from scriptmanager import ScriptManager
from django.shortcuts import redirect
import settings
import os

DEFAULT_SCRIPT = """import blazigator, logger

my_logger = logger.Logger()
my_logger.log(blazigator.op_box.debug())"""

ip_whitelist = ["10.16.114.89"]

def auth(request):
    if request.user.is_superuser:
        return None
    else:
        return redirect("/admin")

def scripts(request):

    context = {
        "scripts" : ScriptManager.getScripts(),
        "log_title": ScriptManager.current_script_name
    }

    auth_check = auth(request)
    if auth_check:
        return auth_check
    return render(request, 'OpBoxWebsite/scripts.html', context)

def logs(request, title):

    if title == "None.log":
        return HttpResponse("No script currently running")

    auth_check = auth(request)
    if auth_check:
        return auth_check

    logfile = Logger.log_dir + title

    try:
        with open(logfile, 'r') as f:
            return HttpResponse(f.read())
    except Exception, e:
        return HttpResponse(str(e))

def run(request, title):

    auth_check = auth(request)
    if auth_check:
        return auth_check

    ScriptManager.current_script_name = title
    ScriptManager.run(title)
    return redirect("/scripts")

def edit(request, title):

    auth_check = auth(request)
    if auth_check:
        return auth_check

    context = {
        "default_script" : DEFAULT_SCRIPT,
        "title" : title,
        "content":ScriptManager.getSource(title)
    }

    return render(request, 'OpBoxWebsite/edit.html', context)

def write(request, title):

    auth_check = auth(request)
    if auth_check:
        return auth_check

    #make sure this is a .py
    if not title.endswith(".py"):
        title += ".py"

    #get script path
    script_path = ScriptManager.script_dir + title

    #write new source to file
    with open(script_path, 'w+') as f:
        f.write(request.POST['src'])

    return HttpResponse("swag")

def rm(request, title):

    auth_check = auth(request)
    if auth_check:
        return auth_check

    logfile = Logger.log_dir + title + ".log"
    script_path = ScriptManager.script_dir + title

    if not title in ScriptManager.exclude:
        if os.path.isfile(logfile): os.remove(logfile)
        if os.path.isfile(script_path): os.remove(script_path)

    if ScriptManager.current_script_name == title:
        ScriptManager.current_script_name = "None"

    return redirect('/scripts')

def manualOverride(request):

    auth_check = auth(request)
    if auth_check:
        return auth_check

    #todo: rexec, or manualy parse instead of being lazy.
    exec("blazigator." + request.GET["src"])
    return HttpResponse("swag")

def home(request):

    context = {
        "cameras" : settings.CAMERA_URLS,
        "log_title": ScriptManager.current_script_name
    }

    return render(request, 'OpBoxWebsite/home.html', context)
