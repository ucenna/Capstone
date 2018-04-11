def process(cmd):
    if 'OPENCAST ' in cmd[0:9]:
        cmd = cmd[9:]
        return cmd
