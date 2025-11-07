from pythonforandroid.recipe import Recipe

class HarfbuzzPatchedRecipe(Recipe):
    version = "5.3.1"
    url = f"https://github.com/harfbuzz/harfbuzz/archive/refs/tags/{version}.tar.gz"

    def get_recipe_env(self, arch=None, **kwargs):
        env = super().get_recipe_env(arch, **kwargs)
        env["CFLAGS"] += " -Wno-error=cast-function-type-strict"
        env["CXXFLAGS"] += " -Wno-error=cast-function-type-strict"
        return env

recipe = HarfbuzzPatchedRecipe()
