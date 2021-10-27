import os
import shutil
import sys
import time

import backup
import file_selector
import tomcat


if __name__ == '__main__':
    catalina_home = os.getenv('CATALINA_HOME')
    if catalina_home is None:
        sys.exit('CATALINA_HOME is not defined.')

    print('___________________________________________')
    print('{:3d}. {:30s}'.format(1, 'deploy'))
    print('{:3d}. {:30s}'.format(2, 'rollback'))
    print('{:3d}. {:30s}'.format(0, 'exit'))
    print('___________________________________________')

    selected = int(input('Please select a number: '))
    if selected == 3:
        exit()

    service_name = input('Please input service name: ')
    directory = './wars' if selected == 1 else './backup'
    deploy_file = file_selector.FileSelector(directory).select('Please select a deployment file: ')

    webapps = '%s/webapps' % catalina_home
    webapps_file_selector = file_selector.FileSelector(webapps)
    for backup_file in webapps_file_selector.get_files():
        answer = input('Do you want to backup %s file? [Y/n]: ' % backup_file)
        if answer != 'n' or answer != 'N':
            filename, file_ext = os.path.splitext(backup_file)
            dest = './backup/%s_%s%s' % (filename, time.strftime("%Y%m%d%H%M%S"), file_ext)
            backup.Backup(os.path.join(webapps, backup_file), dest).start()

    catalina_script = tomcat.Tomcat(catalina_home)
    catalina_script.stop()

    for remove_file in webapps_file_selector.get_all():
        answer = input('Do you want to remove %s file? [y/N]: ' % remove_file)
        if answer == 'y' or answer == 'Y':
            rm_file = os.path.join(webapps, remove_file)
            print('rm %s' % rm_file)
            if os.path.isfile(rm_file):
                os.remove(rm_file)
            else:
                shutil.rmtree(rm_file)

    deploy_file_name, deploy_file_ext = os.path.splitext(deploy_file)
    deploy_path = os.path.join(webapps, '%s%s' % (service_name, deploy_file_ext))

    print('cp %s %s' % (deploy_file, deploy_path))
    shutil.copy(deploy_file, deploy_path)
    catalina_script.start()
