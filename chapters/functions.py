import subprocess


def exec_user_input(user_input):
    # encode the code
    f = open('file.py', 'w', newline='', encoding='utf-8')
    f.truncate(0)
    f.write(user_input)
    f.close()

    try:
        # text=True leaves Windows, which commonly is configured with whatever code page makes sense for the geography where it was sold;
        result = subprocess.check_output(args=['python', 'file.py'], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        str_output = str(e.output)
        return str_output.replace('file.py', 'Code Mirror')
    return result
'''
import sys
from io import StringIO
import contextlib
import traceback
import logging


def exec_function(user_input):

    try:
        compile(user_input, '<stdin>', 'eval')
    except SyntaxError:
        return exec
    return eval


def exec_user_input(user_input):

    try:
        retval = exec_function(user_input)(user_input)
    except Exception as e:
        return e
    if retval is not None:
        print('Out: %s' % retval)
        return retval
    else:
        with stdoutIO() as s:
            try:
                exec(user_input)
            except:
                print('Something wrong with the code')

            return s.getvalue()


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old
'''