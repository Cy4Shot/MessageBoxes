import platform
from tempfile import TemporaryDirectory
from subprocess import run, PIPE

def message_box(title, content, args=''):
    """Creats a message box. WINDOWS USERS ONLY!

    Parameters:
    title (string): Title of the message box.
    content (string): Content of the message box.
    args (string): VB arguments for message box (DEFAULT = '').
    """
    if platform.system() == 'Windows':
        with TemporaryDirectory() as temp_dir:
            with open(temp_dir + '\\data.vbs', 'w') as f:
                f.write('x=MsgBox("'+content+'", '+str(args)+', "'+title + '")\nSet fso = CreateObject ("Scripting.FileSystemObject")\nSet stdout = fso.GetStandardStream (1)\nstdout.WriteLine x')
            result = run('wscript //nologo ' + temp_dir + '\\data.vbs', stdout=PIPE, stderr=PIPE, universal_newlines=True)
            return int(result.stdout)
    else:
        raise(OSError("Wrong Operating System: Must be Windows"))