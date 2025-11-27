[app]

title = Antenas
package.name = antenasapp
package.domain = org.elaineinacio

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# Aqui usamos as versões estáveis + tuas receitas customizadas
requirements = python3==3.10.14, \
               kivy==2.3.0, \
               matplotlibfix, \
               freetype, \
               libpng, \
               numpy, \
               pillow, \
               requests, \
               harfbuzzfix

orientation = portrait
fullscreen = 0

android.presplash_color = #F6F6F6

android.permissions = INTERNET, \
                       BLUETOOTH, \
                       BLUETOOTH_ADMIN, \
                       BLUETOOTH_CONNECT, \
                       BLUETOOTH_SCAN, \
                       ACCESS_FINE_LOCATION, \
                       ACCESS_COARSE_LOCATION, \
                       WRITE_EXTERNAL_STORAGE, \
                       READ_EXTERNAL_STORAGE

android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a
android.private_storage = True
android.accept_sdk_license = True
android.allow_backup = True

# Usa bootstrap SDL2 (padrão do P4A para Kivy)
p4a.bootstrap = sdl2

# Usa versão estável do p4a (master pode quebrar builds)
p4a.branch = stable

# Teus recipes customizados
p4a.local_recipes = ./recipes


[buildozer]
log_level = 2
warn_on_root = 1
