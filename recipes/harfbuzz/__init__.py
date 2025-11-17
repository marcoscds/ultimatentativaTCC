from pythonforandroid.recipe import Recipe

class HarfbuzzPatchedRecipe(Recipe):
    version = "2.6.4"
    url = f"https://github.com/harfbuzz/harfbuzz/archive/refs/tags/{version}.tar.gz"
    depends = ["freetype", "libpng"]

    def get_recipe_env(self, arch=None, **kwargs):
        env = super().get_recipe_env(arch, **kwargs)

        # Flags essenciais
        env["CFLAGS"] += " -fPIC"
        env["CXXFLAGS"] += " -fPIC -std=c++17"

        # Diretórios do FreeType
        freetype_build = self.get_recipe('freetype', self.ctx).get_build_dir(arch.arch)
        env["CFLAGS"] += f" -I{freetype_build}/include -I{freetype_build}/include/freetype2"
        env["CXXFLAGS"] += f" -I{freetype_build}/include -I{freetype_build}/include/freetype2"

        # Link com FreeType
        env["LDFLAGS"] += f" -L{freetype_build}/objs/.libs"
        env["PKG_CONFIG_PATH"] = f"{freetype_build}/objs"

        return env

recipe = HarfbuzzPatchedRecipe()
