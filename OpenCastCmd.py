def process(cmdlist):

    # Verify that this is meant for OPENCAST
    if 'OPENCAST ' in cmdlist[0:9]:

        # remove'OPENCAST ' from string
        cmdlist = cmdlist[9:]
        cmdlist = cmdlist.split("::")

        # pars cmdlist into new array
        _cmdlist = []
        for cmd in cmdlist:

            # remove parenthesis and split into cmd and arguments lists
            cmdarr = cmd.split('(', 1)
            cmdarr[1] = cmdarr[1][:-1]

            # split arguments string into array of arguments
            cmdarr[1] = cmdarr[1].split(',')

            # render arguments into usable data types
            if cmdarr[1][0]:
                _arg = []
                for arg in cmdarr[1]:
                    _arg.append(eval(arg))
                cmdarr[1] = _arg
            else:
                cmdarr[1] = []

            _cmdlist.append(cmdarr)

        return _cmdlist
