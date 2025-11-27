[app]

title = Antenas

package.name = antenasapp
package.domain = org.marcosdonato

# (str) Source code where the main.py live
source.dir = .

source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

requirements = python3==3.10.14,kivy==2.3.0,matplotlib==3.5.3,freetype,libpng,numpy,pillow,requests,harfbuzz

icon.filename = icone.png

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
android.presplash_color = #F6F6F6

# (list) Permissions
android.permissions = INTERNET,BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,BLUETOOTH_SCAN,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK / AAB will support.
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.private_storage = True
android.accept_sdk_license = True
android.archs = arm64-v8a
android.allow_backup = True


# (str) python-for-android branch to use
p4a.branch = master
p4a.bootstrap = sdl2
p4a.local_recipes = ./recipes


[buildozer]

log_level = 2
warn_on_root = 1
