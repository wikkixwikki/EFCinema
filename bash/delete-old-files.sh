#!/bin/bash
# setup cronjob to run this script periodically
# deletes all files and folders in specified directories after "-mtime -n" number of days.
find /path/to/dir/with/files/to/watch -maxdepth 1 -mtime +7 -exec rm -R {} \;
find /other/path/to/dir/with/file/to/watch -maxdepth 1 -mtime +7 -exec rm -R {} \;
