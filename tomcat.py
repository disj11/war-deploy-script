import subprocess


class Tomcat(object):
    def __init__(self, catalina_home):
        self.catalina_home = catalina_home

    def _get_startup_sh(self):
        return '%s/bin/startup.sh' % self.catalina_home

    def _get_shutdown_sh(self):
        return '%s/bin/shutdown.sh' % self.catalina_home

    def start(self):
        print('Starting Tomcat...')
        sh = self._get_startup_sh()
        subprocess.call([sh])

    def stop(self):
        print('Stopping Tomcat...')
        sh = self._get_shutdown_sh()
        subprocess.call([sh])

