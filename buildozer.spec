[app]

# (str) Title of your application
title = Game Automation

# (str) Package name
package.name = gameautomation

# (str) Package domain (needed for android/ios packaging)
package.domain = com.gameautomation

# (str) Source code where the main.py live
source.dir = .

# (str) Main entry point
source.main = overlay_app.py

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
# Note: numpy and pytesseract can be problematic - may need to build without them first
requirements = python3,kivy,plyer,pyjnius,android,pillow

# (str) Custom source folders for requirements
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,ACCESSIBILITY_SERVICE,SYSTEM_ALERT_WINDOW

# (int) Target Android API, should be as high as possible.
android.api = 30

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Service
#android.service_class_name = org.kivy.android.PythonService

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (list) Android additional libraries to copy into libs/armeabi
#android.add_jars = foo.jar,bar.jar
#android.add_jars = path/to/more/*.jar

# (list) Android additional libraries to copy into libs/armeabi-v7a
#android.add_jars = foo.jar,bar.jar
#android.add_jars = path/to/more/*.jar

# (list) Android additional libraries to copy into libs/arm64-v8a
#android.add_jars = foo.jar,bar.jar
#android.add_jars = path/to/more/*.jar

# (list) Android additional libraries to copy into libs/x86
#android.add_jars = foo.jar,bar.jar
#android.add_jars = path/to/more/*.jar

# (list) Android additional libraries to copy into libs/mips
#android.add_jars = foo.jar,bar.jar
#android.add_jars = path/to/more/*.jar

# (list) Android additional libraries to copy into libs/x86_64
#android.add_jars = foo.jar,bar.jar
#android.add_jars = path/to/more/*.jar

# (list) Android additional libraries to copy into libs/mips64
#android.add_jars = foo.jar,bar.jar
#android.add_jars = path/to/more/*.jar

# (bool) Indicate whether the screen should stay on
# Don't forget to add the WAKE_LOCK permission if you set this to True
#android.wakelock = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
#android.library_references =

# (list) Android shared libraries which will be added to the APK
#android.uses_library =

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libs symlink
#android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
arch = arm64-v8a
