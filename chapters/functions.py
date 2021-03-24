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