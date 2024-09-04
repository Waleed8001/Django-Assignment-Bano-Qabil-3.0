import sys
from io import StringIO

def send(code):
    # create file-like string to capture output
    codeOut = StringIO()
    codeErr = StringIO()
    print("Start")
    
    h = code
    
    my_code_with_error = """
    print("Hello world!")
    print(avfsd)  # error -> printing a variable that does not exist.
    """

    print("Executing code...")
    # capture output and errors
    sys.stdout = codeOut
    sys.stderr = codeErr

    try:
        exec(h)  # this works fine
    # exec(my_code_with_error)  # as soon as there is an error, it crashes silently.
    except:
        e = codeErr.getvalue()
    # restore stdout and stderr
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    print("Finished code execution.")
    e = codeErr.getvalue()
    o = codeOut.getvalue()
    
    codeOut.close()
    codeErr.close()
    return {"Error":e,"Output":o}
    