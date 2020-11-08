import platform
from tempfile import TemporaryDirectory
from subprocess import run, PIPE

wrapper = {
    1: True,
    2: None,
    3: False,
    4: True,
    5: None,
    6: True,
    7: False
}

def message_box(title, content, args=''):
    if platform.system()=='Windows':
        with TemporaryDirectory() as temp_dir:
            open(temp_dir+'\\data.vbs','w').write('x=MsgBox("'+content+'",'+str(args)+',"'+title+'")\nSet fso=CreateObject("Scripting.FileSystemObject")\nSet stdout=fso.GetStandardStream(1)\nstdout.WriteLine x')
            return wrapper[int(run('wscript //nologo '+temp_dir+'\\data.vbs',stdout=PIPE).stdout)]
    else:
        raise(OSError("Wrong Operating System, Must be Windows"))