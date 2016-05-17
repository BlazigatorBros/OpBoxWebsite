from django.http import HttpResponse
from django.shortcuts import render
from scripts.logger import Logger
from scriptmanager import ScriptManager
from django.shortcuts import redirect
import scripts.blazigator as blazigator
import urllib
import settings
import inspect
import ast
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

def moduleView(request):

    auth_check = auth(request)
    if auth_check:
        return auth_check

    modTree = dict()
    modTree["name"] = "Blazigator"
    modTree["doc"] = blazigator.__doc__

    #assumption: members start with lower-case, classes start with upper-case
    safe_member_keys = [key for key in blazigator.__dict__.keys()
                if not (key.startswith("__") 
                        or inspect.isclass(blazigator.__dict__[key])
                        or inspect.ismodule(blazigator.__dict__[key])
                )
        ]

    getFunTree = lambda obj: [{"name": f, "doc": getattr(obj, f).__doc__}
                                for f in dir(obj) 
                                if (callable(getattr(obj, f))
                                        and not f.startswith("__")
                                )
        ]

    safe_members = [{"name": key,
                "doc": blazigator.__dict__[key].__doc__,
                "functions": getFunTree(blazigator.__dict__[key])}
                for key in safe_member_keys
              ]

    modTree["members"] = safe_members

    context = {
        "cameras" : settings.CAMERA_URLS,
        "modTree" : modTree
    }

    return render(request, 'OpBoxWebsite/ModuleView.html', context)

def runFunction(request, module_key, function_key):

    auth_check = auth(request)
    if auth_check:
        return auth_check

    #assumption: members start with lower-case, classes start with upper-case
    safe_member_keys = [key for key in blazigator.__dict__.keys()
                if not (key.startswith("__") 
                        or inspect.isclass(blazigator.__dict__[key])
                        or inspect.ismodule(blazigator.__dict__[key])
                )
        ]

    if not module_key in safe_member_keys:
        return HttpResponse("naw bro", status =403)

    module = blazigator.__dict__[module_key]
    safe_function_keys = [f for f in dir(module) 
                                if (callable(getattr(module, f))
                                        and not f.startswith("__")
                                )
        ]

    if not function_key in safe_function_keys:
        return HttpResponse("naw bro", status =403)

    ScriptManager.current_script_name = "None.py"
    ScriptManager.run("None.py")

    args = ast.literal_eval(urllib.unquote(request.GET['args']))
    if args:
            return HttpResponse(getattr(module, function_key)(args))
    else:
            return HttpResponse(getattr(module, function_key)())

def home(request):

    context = {
        "cameras" : settings.CAMERA_URLS,
        "log_title": ScriptManager.current_script_name
    }

    return render(request, 'OpBoxWebsite/home.html', context)
