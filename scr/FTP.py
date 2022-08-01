from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from daemon import runner
import os
import sys

ip = '192.168.1.66' #sys.argv[2]
port = '8021' #sys.argv[3]
ftpDir = '/sdcard' #sys.argv[4]

class FTP():
    def __init__(self, ip, port, ftpDir):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/null'
        self.stderr_path = '/dev/null'
        self.pidfile_path = '$PREFIX/tmp/foo.pid'
        self.pidfile_timeout = 5
        self.ftpDir = ftpDir
        self.ip = ip
        self.port = port
    def run(self):
        os.system('python -m pyftpdlib -p 8021 -d /sdcard -w')


        #authorizer = DummyAuthorizer()
        #authorizer.add_anonymous(self.ftpDir, perm=('r', 'w'))
        #handler = FTPHandler
        #handler.authorizer = authorizer
        #server = FTPServer(self.ip, self.port, handler)
        #server.serve_forever()

app = FTP(ip, port, ftpDir)
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()