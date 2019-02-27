#!/bin/bash

# run with a cronjob

# will scan directories recursively for rar files, and unrar them in the same directory.
# will skip if rar has already been extracted.
find /path/to/dir/with/rar -name '*.rar' -execdir unrar e -o- {} \;
find /path/to/other/dir/with/rar -name '*.rar' -execdir unrar e -o- {} \;
