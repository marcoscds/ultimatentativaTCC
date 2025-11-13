from pythonforandroid.recipe import Recipe

class HarfbuzzPatchedRecipe(Recipe):
    version = "5.3.1"
    url = f"https://github.com/harfbuzz/harfbuzz/archive/refs/tags/{version}.tar.gz"
    depends = ["freetype", "libpng"]

    def get_recipe_env(self, arch=None, **kwargs):
        env = super().get_recipe_env(arch, **kwargs)

        # Desativa warnings tratados como erro
        cflags_fix = "-Wno-error -Wno-error=unused-but-set-variable -Wno-error=deprecated-declarations -Wno-error=cast-function-type-strict"
        env["CFLAGS"] = env.get("CFLAGS", "") + " " + cflags_fix
        env["CXXFLAGS"] = env.get("CXXFLAGS", "") + " " + cflags_fix

        # Diretórios do freetype (linkagem e includes)
        freetype_build = self.get_recipe('freetype', self.ctx).get_build_dir(arch.arch)
        freetype_includes = [
            f"-I{freetype_build}/include",
            f"-I{freetype_build}/include/freetype2"
        ]
        env["CFLAGS"] += " " + " ".join(freetype_includes)
        env["CXXFLAGS"] += " " + " ".join(freetype_includes)
        env["LDFLAGS"] += f" -L{freetype_build}/objs/.libs"
        env["PKG_CONFIG_PATH"] = f"{freetype_build}/objs"

        # Garante compatibilidade de build
        env["CPPFLAGS"] = env.get("CPPFLAGS", "") + " -fPIC -std=c++17"

        return env

recipe = HarfbuzzPatchedRecipe()
