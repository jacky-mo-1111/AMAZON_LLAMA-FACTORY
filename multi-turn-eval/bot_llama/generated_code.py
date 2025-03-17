import os

# Set file permissions to 755 (rwxr-x)
os.chmod('path/to/file', 0o755)

import pathlib

# Set file permissions to 755 (rwxr-x)
pathlib.Path('path/to/file').chmod(0o755)

$ ls -l /var/log
-r--r--r-- 1 root root 12345678 Mar 12 14:30 log_file.log

$ getfacl /var/log/log_file.log
# file: /var/log/log_file.log
# owner: root
# group: root
user::r--
group::r--
other::r--

$ getent group server_user
server_user:x:1001:server_user

$ chmod o+w /var/log/log_file.log
$ chown server_user:server_group /var/log/log_file.log

$ touch /var/log/log_file.log.new
$ ls -l /var/log
-rw-r--r-- 1 server_user server_group 0 Mar 12 14:35 log_file.log.new