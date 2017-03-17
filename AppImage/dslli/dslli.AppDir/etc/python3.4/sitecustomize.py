import sys,os
if sys.version_info[0] < 3:
    prefix = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(sys.path[0]))))
    sys.path = [ prefix+s for s in sys.path if not s.startswith(prefix) ]
