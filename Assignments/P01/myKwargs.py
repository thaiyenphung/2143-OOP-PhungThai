def MyKwargs(argv):
    # list of simple flags or plain arguments
    args = []  
    
    # dictionary of keyword arguments (key:value) like year:2020
    kargs = {}  

    for arg in argv:
        # check for keyword pair
        if ":" in arg:
            # split the argument at the first colon into key and value
            key, val = arg.split(":", 1)  
            kargs[key] = val
        else:
            # strip the leading dashes 
            # if someone runs the command with dashes (like `--search`), 
            # remove the dashes so we just get `search``
            args.append(arg.strip("-"))

    return args, kargs