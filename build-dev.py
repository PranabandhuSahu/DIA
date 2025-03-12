import os
import subprocess
import time
import shutil

CURRENT_DIRECTORY = os.getcwd()
directories = os.listdir(CURRENT_DIRECTORY)
NON_ANGULAR_DIRS = ['resources','static', 'templates', 'weights', 'venv', 'env', '__pycache__','uploads','DIA2','.github']
ANGULAR_PROJECT_PATH = ""
DIST_PATH = ""
DIST_ASSETS_PATH = ""

for directory in directories:
    if "." not in directory and directory not in NON_ANGULAR_DIRS:
        ANGULAR_PROJECT_PATH = os.path.join(CURRENT_DIRECTORY,directory)
        print('ANGULAR_PROJECT_PATH',ANGULAR_PROJECT_PATH)
        DIST_PATH = os.path.join(ANGULAR_PROJECT_PATH, 'dist', 'dia')
        DIST_ASSETS_PATH = os.path.join(DIST_PATH, 'assets')
FLASK_STATIC_PATH = os.path.join(CURRENT_DIRECTORY, 'static')
FLASK_TEMPLATES_PATH = os.path.join(CURRENT_DIRECTORY, 'templates')

dir_exists = True

if dir_exists:
    try:
        subprocess.run(('cd ' + ANGULAR_PROJECT_PATH + ' && ng build --base-href /static/ --output-hashing=all &'), shell=True)
        time.sleep(50)
        for f in os.listdir(FLASK_STATIC_PATH):
          os.remove(os.path.join(FLASK_STATIC_PATH, f))
        print('Begin Transferring files')
        try:
            files = os.listdir(DIST_PATH)
            print('files',files)
        except Exception as e1:
            print(e1)
        static_files = ""
        html_files = ""
        for file in files:
            if '.js' in file or '.js.map' in file or '.ico' in file or '.css' in file or '.jpg' in file or '.woff' in file or '.woff2' in file :
                static_files = file
                print(DIST_PATH + '/' + static_files, FLASK_STATIC_PATH + '/' + static_files)
                (shutil.move(DIST_PATH + '/' + static_files, FLASK_STATIC_PATH + '/' + static_files))
                try:
                    if os.path.exists(DIST_PATH + '/' + static_files):
                       os.remove(DIST_PATH + '/' + static_files)
                except Exception as e1:
                    print('DIST PATH',e1)
            if '.html' in file:
                html_files = file
                if os.path.exists(FLASK_TEMPLATES_PATH + '\\' + html_files):
                  os.remove(FLASK_TEMPLATES_PATH + '\\' + html_files)
                print(DIST_PATH + '\\' + html_files, FLASK_TEMPLATES_PATH + '\\' + html_files)
                (shutil.move(DIST_PATH + '\\' + html_files, FLASK_TEMPLATES_PATH + '\\' + html_files))
                if os.path.exists(DIST_PATH + '\\' + html_files):
                  os.remove(DIST_PATH + '\\' + html_files)

        files = os.listdir(DIST_ASSETS_PATH)
        for file in files:
          if '.js' in file or '.png' in file or '.mp4' in file or '.mov' in file:
            static_files = file
            print(DIST_ASSETS_PATH + '\\' + static_files, FLASK_STATIC_PATH + '\\' + static_files)
            (shutil.move(DIST_ASSETS_PATH + '\\' + static_files, FLASK_STATIC_PATH + '\\' + static_files))
            if os.path.exists(DIST_ASSETS_PATH + '\\' + static_files):
              os.remove(DIST_ASSETS_PATH + '\\' + static_files)
    except Exception as e:
        dir_exists = False
        print(e)
