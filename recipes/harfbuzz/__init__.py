from pythonforandroid.recipe import AutotoolsRecipe

class HarfbuzzPatchedRecipe(AutotoolsRecipe):
    version = "5.3.1"
    url = f"https://mirror.ghproxy.com/https://github.com/harfbuzz/harfbuzz/archive/refs/tags/{version}.tar.gz"



    def get_recipe_env(self, arch=None, **kwargs):
        env = super().get_recipe_env(arch, **kwargs)

        # Remove qualquer -Werror herdado
        env["CFLAGS"] = env.get("CFLAGS", "").replace("-Werror", "")
        env["CXXFLAGS"] = env.get("CXXFLAGS", "").replace("-Werror", "")

        # Ignora warnings específicos
        flags = "-Wno-error -Wno-error=unused-but-set-variable -Wno-error=cast-function-type-strict"
        env["CFLAGS"] += f" {flags}"
        env["CXXFLAGS"] += f" {flags}"

        # Caminhos do freetype
        freetype_build = self.get_recipe('freetype', self.ctx).get_build_dir(arch.arch)
        freetype_include = f"{freetype_build}/include"
        freetype_include2 = f"{freetype_build}/include/freetype2"

        env["CFLAGS"] += f" -I{freetype_include} -I{freetype_include2}"
        env["CXXFLAGS"] += f" -I{freetype_include} -I{freetype_include2}"

        # Linkagem com freetype
        env["LDFLAGS"] += f" -L{freetype_build}/objs/.libs"
        env["PKG_CONFIG_PATH"] = f"{freetype_build}/objs"

        return env

recipe = HarfbuzzPatchedRecipe()
