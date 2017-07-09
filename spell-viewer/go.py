#!/usr/bin/env python

import os, subprocess

subprocess.check_call('python {} . --metasource spell-viewer.meta.html'.format(os.path.join('..', 'crangen', 'generate.py')), shell=True)
