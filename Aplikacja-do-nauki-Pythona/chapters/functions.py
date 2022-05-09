import subprocess


def exec_user_input(user_input):
    # write input to file
    with open('/exec_code/file.py', 'w', newline='', encoding='utf-8') as f:
        f.truncate(0)
        f.write(user_input)

    try:
        # text=True leaves Windows, which commonly is configured with whatever code page makes sense for the geography where it was sold;
        result = subprocess.check_output(args=['python3', '/exec_code/file.py'], user="code-exec", stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        str_output = str(e.output)
        return str_output.replace('file.py', 'Code Mirror')
    return result
