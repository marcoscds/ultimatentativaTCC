[app]
# Nome do aplicativo
title = Caracterizador de Antenas
package.name = myapp
package.domain = org.test

# Fonte
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Requisitos
requirements = python3,kivy,numpy,matplotlib==3.6.3,pillow,pyjnius,requests,freetype,libpng,harfbuzz

# Recipes locais
p4a.local_recipes = ./recipes

# Ícone
icon.filename = icon.png

# Configurações do Android
android.archs = arm64-v8a,armeabi-v7a
android.api = 33
android.minapi = 26
android.sdk = 33
android.ndk = 27b
android.bootstrap = sdl2

# Outras configs
orientation = portrait
fullscreen = 0
