# CAUTION: THIS SCRIPT WILL DELETE ALL MIGRATION FILES
# PLEASE BACKUP MIGRATIONS FILES BEFORE DELETE OR TAKE NECESSARY ACTIONS

import os

from registration_proj import settings

pass_code = 'please rethink before running this code'
input_pass_code = str(input('Enter pass code: '))

if input_pass_code == pass_code:
    for root, subFolders, files in os.walk(settings.BASE_DIR):
        for f in files:
            if 'migrations' in root and not f.startswith('__'):
                os.remove(root+'/'+f)
