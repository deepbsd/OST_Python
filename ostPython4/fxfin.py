#!/usr/bin/env python3

class LocalError(Exception):
    def __init__(self, msg):
        self.args = (msg, )
        self.msg = msg
    def __str__(self):
        return self.msg

def fxfin(where):
    "Demonstrate exceptions in various places."
    try:
        if where == "try":
            raise LocalError("LocalError in try")
        raise ValueError("ValueError in try")
    except (ValueError, LocalError) as e:
        print("Caught", e)
        if where == "except":
            raise LocalError("LocalError in except")
        print("Exception not raised in except")
    finally:
        print("Running finalization")
        if where == "finally":
            raise LocalError("LocalError in finally")
        print("Exception not raised in finally")

for where in "try", "except", "finally":
    print("---- Exception in %s ----" % where)
    try:
        fxfin(where)
    except Exception as e:
        print("!!!", e, "raised")
    else:
        print("+++ No exception raised +++")




