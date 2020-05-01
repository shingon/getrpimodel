from __future__ import absolute_import
import sys
from . import getrpimodel

usage = 'Usage: python {} [--s]'.format(__file__)

if len(sys.argv) == 1:
  print(getrpimodel.model())
elif len(sys.argv) == 2:
  if sys.argv[1] == '--s':
    print(getrpimodel.model_strict())
  else:
    print(usage)
else:
  print(usage)
