Tip
In the previous video we used help() and dir() inside an interactive Python shell:

>>> dir(str)

Please note that if you want to get the output of help and dir from a normal .py file, you have to use a print function, otherwise the .py file will not return any output when executed:

print(dir(str))

That is because the Python interactive shell uses a print function implicitly, so you don't have to type it in, but this is not the case when the code is inside .py files.

You should also use a print function when you are coding in the Udemy exercise interface.