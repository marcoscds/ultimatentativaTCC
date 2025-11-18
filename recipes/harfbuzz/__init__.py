from pythonforandroid.recipe import Recipe

class HarfbuzzPatchedRecipe(Recipe):
    name = "harfbuzz"  # OBRIGATÓRIO para sobrescrever a receita padrão
    version = "2.6.4"
    url = f"https://github.com/harfbuzz/harfbuzz/archive/refs/tags/{version}.tar.gz"

    depends = ["freetype", "libpng"]

    def get_recipe_env(self, arch=None, **kwargs):
        env = super().get_recipe_env(arch, **kwargs)

        # Configurações essenciais para compilar com NDK moderno
        env["CFLAGS"] += " -fPIC"
        env["CXXFLAGS"] += " -fPIC -std=c++17"

        # Ignore warnings que matam o build
        no_error_flags = (
            "-Wno-error "
            "-Wno-error=unused-but-set-variable "
            "-Wno-error=deprecated-declarations "
            "-Wno-error=cast-function-type-strict"
        )

        env["CFLAGS"] += " " + no_error_flags
        env["CXXFLAGS"] += " " + no_error_flags

        # Diretórios do FreeType compilado pelo p4a
        freetype_build = self.get_recipe('freetype', self.ctx).get_build_dir(arch.arch)

        env["CFLAGS"] += f" -I{freetype_build}/include -I{freetype_build}/include/freetype2"
        env["CXXFLAGS"] += f" -I{freetype_build}/include -I{freetype_build}/include/freetype2"

        # Linkagem correta com FreeType
        env["LDFLAGS"] += f" -L{freetype_build}/objs/.libs"

        # pkg-config para Harfbuzz detectar FreeType
        env["PKG_CONFIG_PATH"] = f"{freetype_build}/objs"

        return env


recipe = HarfbuzzPatchedRecipe()
