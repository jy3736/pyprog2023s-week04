# Do not modify this file.  It is used by the autograder.

cmd = python
dir_check = tools

all:

lab%:
	$(cmd) ./$(dir_check)/chk_$@.py
