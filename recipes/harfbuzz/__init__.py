from pythonforandroid.recipe import AutoconfRecipe

class HarfbuzzFixedRecipe(AutoconfRecipe):
    version = "8.0.1"
    url = "https://github.com/harfbuzz/harfbuzz/releases/download/{version}/harfbuzz-{version}.tar.xz"

    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)

        # DESATIVA O WERROR QUE MATA O SEU BUILD
        env["CFLAGS"] = env.get("CFLAGS", "") + " -Wno-error"
        env["CXXFLAGS"] = env.get("CXXFLAGS", "") + " -Wno-error -Wno-unused-but-set-variable"

        return env

recipe = HarfbuzzFixedRecipe()
