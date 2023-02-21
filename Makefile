# Do not modify this file.  It is used by the autograder.

cmd = python
dir_check = lib/tests
ext ?= pyc

all:

lab%:
	$(cmd) ./$(dir_check)/chk_$@.$(ext)
