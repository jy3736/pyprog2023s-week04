# Do not modify this file, unless you know what you are doing!

CMD = python
DIR_HW = src
DIR_CHECK = ../../lib/tests
THIS_DIR = $(lastword $(subst /, ,$(CURDIR)))
ext ?= pyc

all: check

check:
	$(CMD) $(DIR_CHECK)/chk_$(THIS_DIR).$(ext)
