[app]
title = Caracterizador de Antenas
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy,numpy,matplotlib==3.7.2,pillow,pyjnius,requests

p4a.local_recipes = recipes 
p4a.branch = develop
p4a.bootstrap = sdl2
p4a.python_version = 3.10
p4a.extra_env_vars = CFLAGS=-std=c++17


android.archs = arm64-v8a,armeabi-v7a 
android.api = 33
android.minapi = 26
android.ndk = 26b


icon.filename = icone.png
orientation = portrait
fullscreen = 0

android.permissions = BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_SCAN,BLUETOOTH_CONNECT,ACCESS_COARSE_LOCATION,ACCESS_FINE_LOCATION,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET

android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
