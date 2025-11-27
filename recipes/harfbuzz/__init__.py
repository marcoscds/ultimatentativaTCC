import os
from pythonforandroid.recipes.harfbuzz import HarfbuzzRecipe
from pythonforandroid.util import current_directory
import sh


class HarfbuzzRecipe(HarfbuzzRecipe):
    name = "harfbuzz"

    def get_recipe_env(self, arch=None, **kwargs):
        env = super().get_recipe_env(arch, **kwargs)

        # Flags para ignorar erros bobos do Clang/NDK
        no_error_flags = (
            " -Wno-error"
            " -Wno-error=unused-but-set-variable"
            " -Wno-error=deprecated-declarations"
            " -Wno-error=cast-function-type-strict"
            " -Wno-error=incompatible-pointer-types"
            " -Wno-error=implicit-function-declaration"
        )

        # FreeType paths
        freetype_recipe = self.get_recipe("freetype", self.ctx)
        freetype_build_dir = freetype_recipe.get_build_dir(arch.arch)

        include_paths = (
            f" -I{freetype_build_dir}/include"
            f" -I{freetype_build_dir}/include/freetype2"
        )

        # CFLAGS (C code)
        env["CFLAGS"] = (
            env.get("CFLAGS", "")
            + " -fPIC"
            + include_paths
            + no_error_flags
        )

        # CXXFLAGS (C++ code)
        env["CXXFLAGS"] = (
            env.get("CXXFLAGS", "")
            + " -fPIC -std=c++17"
            + include_paths
            + no_error_flags
        )

        # LDFLAGS (linker)
        env["LDFLAGS"] = (
            env.get("LDFLAGS", "")
            + f" -L{freetype_build_dir}/objs/.libs"
        )

        env["PKG_CONFIG_PATH"] = f"{freetype_build_dir}/objs"

        return env

    def build_arch(self, arch):
        env = self.get_recipe_env(arch)
        cpu_count = self.ctx.cpu_count

        with current_directory(self.get_build_dir(arch.arch)):
            sh.make("-j", str(cpu_count), _env=env) 
            sh.make("install", f"DESTDIR={arch.dist_dir}", _env=env)

        self.install_headers(arch)


recipe = HarfbuzzRecipe()
