



from exporting_module import myfunc

#! here we get the name exporing_module means the file is run from exporting module

#if we do this here then the file present in exporting modules runs here 
# and created a __pycache__
#__pycache__ stores Python bytecode files (.pyc) to improve execution speed.


# Finds exporting_module.py
# 2️⃣ Compiles it to bytecode
# 3️⃣ Saves that bytecode as .pyc
# 4️⃣ Stores it inside __pycache__

# 👉 That’s why __pycache__ is created at import time, not only when running a file directly.


# Bytecode is an intermediate compiled form of Python code executed by the Python Virtual Machine.

# LOAD_CONST   1 (5)
# STORE_NAME   0 (a)
# LOAD_CONST   2 (6)
# STORE_NAME   1 (b)
# LOAD_NAME    2 (print)
# LOAD_NAME    0 (a)
# LOAD_NAME    1 (b)
# BINARY_ADD
# CALL_FUNCTION 1

#! 👉This is bytecode, not 010101.print(__name__)