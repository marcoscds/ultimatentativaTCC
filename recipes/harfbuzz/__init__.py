from pythonforandroid.recipe import Recipe

class HarfbuzzPatchedRecipe(Recipe):
    version = "5.3.1"
    url = f"https://github.com/harfbuzz/harfbuzz/archive/refs/tags/{version}.tar.gz"

    def get_recipe_env(self, arch=None, **kwargs):
        env = super().get_recipe_env(arch, **kwargs)

        # Ignora warnings que estão travando o build
        flags = "-Wno-error -Wno-error=unused-but-set-variable -Wno-error=cast-function-type-strict"
        env["CFLAGS"] += f" {flags}"
        env["CXXFLAGS"] += f" {flags}"

        # Diretório onde o freetype foi compilado
        freetype_build = self.get_recipe('freetype', self.ctx).get_build_dir(arch.arch)
        freetype_include = f"{freetype_build}/include"
        freetype_include2 = f"{freetype_build}/include/freetype2"

        # Inclui ambos os caminhos do freetype
        env["CFLAGS"] += f" -I{freetype_include} -I{freetype_include2}"
        env["CXXFLAGS"] += f" -I{freetype_include} -I{freetype_include2}"

        # Link com FreeType
        env["LDFLAGS"] += f" -L{freetype_build}/objs/.libs"
        env["PKG_CONFIG_PATH"] = f"{freetype_build}/objs"

        return env

        return env

recipe = HarfbuzzPatchedRecipe()
