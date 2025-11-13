from pythonforandroid.recipe import Recipe

class HarfbuzzPatchedRecipe(Recipe):
    version = "5.3.1"
    url = f"https://github.com/harfbuzz/harfbuzz/archive/refs/tags/{version}.tar.gz"

    def get_recipe_env(self, arch=None, **kwargs):
        env = super().get_recipe_env(arch, **kwargs)

        # Diretório onde o freetype foi compilado
        freetype_build = self.get_recipe('freetype', self.ctx).get_build_dir(arch.arch)
        freetype_include = f"{freetype_build}/include"

        # Inclui o caminho do freetype no include path e corrige warnings
        env["CFLAGS"] += f" -I{freetype_include} -Wno-error=cast-function-type-strict"
        env["CXXFLAGS"] += f" -I{freetype_include} -Wno-error=cast-function-type-strict"
        env["LDFLAGS"] += f" -L{freetype_build}/objs/.libs"
        env["PKG_CONFIG_PATH"] = f"{freetype_build}/objs"

        return env

recipe = HarfbuzzPatchedRecipe()
