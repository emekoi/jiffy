#!/usr/bin/python2.7

import os, sys, platform, string

if len(sys.argv) != 2:
  print "usage: ./test.py FILENAME"
  exit()

opt = {
  "compiler"  : "gcc",
  "output"    : os.path.basename(sys.argv[1]).replace(".c", ".exe" if os.name == "nt" else ""),
  "source"    : " ".join([ sys.argv[1] ]),
  "link"      : "",
  "flags"     : " ".join([ "-O3", "-Wall", "-Wextra", "--std=c99", "-fno-strict-aliasing" ]),
}

template = "$compiler -o bin/$output $source $link $flags"
os.system(string.Template(template).substitute(opt))
