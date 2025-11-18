import os
from pythonforandroid.recipes.harfbuzz import HarfbuzzRecipe
from pythonforandroid.util import current_directory, shprint
import sh


class HarfbuzzFixRecipe(HarfbuzzRecipe):
    name = 'harfbuzz'

    def get_recipe_env(self, arch=None, **kwargs):
        env = super().get_recipe_env(arch, **kwargs)

        # Ignorar Werror
        no_error_flags = (
            " -Wno-error"
            " -Wno-error=unused-but-set-variable"
            " -Wno-error=deprecated-declarations"
            " -Wno-error=cast-function-type-strict"
            " -Wno-error=incompatible-pointer-types"
        )

        env['CFLAGS'] = env.get('CFLAGS', '') + " -fPIC" + no_error_flags
        env['CXXFLAGS'] = env.get('CXXFLAGS', '') + " -fPIC -std=c++17" + no_error_flags

        # FreeType
        freetype_recipe = self.get_recipe('freetype', self.ctx)
        freetype_build_dir = freetype_recipe.get_build_dir(arch.arch)

        env["CFLAGS"] += f" -I{freetype_build_dir}/include -I{freetype_build_dir}/include/freetype2"
        env["CXXFLAGS"] += f" -I{freetype_build_dir}/include -I{freetype_build_dir}/include/freetype2"
        env["LDFLAGS"] += f" -L{freetype_build_dir}/objs/.libs"

        env["PKG_CONFIG_PATH"] = f"{freetype_build_dir}/objs"

        return env

    def build_arch(self, arch):
        env = self.get_recipe_env(arch)

        with current_directory(self.get_build_dir(arch.arch)):
            shprint(sh.make, '-j', str(self.cpu_count), _env=env)
            shprint(sh.make, 'install', f"DESTDIR={arch.dist_dir}", _env=env)

        self.install_headers(arch)


recipe = HarfbuzzFixRecipe()
