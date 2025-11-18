import os
from pythonforandroid.recipes.matplotlib import MatplotlibRecipe

class FixedMatplotlibRecipe(MatplotlibRecipe):
    need_stl_shared = True
   
    patches = []

    def get_recipe_env(self, arch=None, **kwargs):
        env = super().get_recipe_env(arch, **kwargs)
        env["MPLBACKEND"] = "Agg"
        env["MATPLOTLIBRC"] = os.path.join(os.getcwd(), "matplotlibrc")
        env["USE_OPENMP"] = "0"  # Mantido para evitar erros de compilação C/C++
        return env

    name = "matplotlib"

recipe = FixedMatplotlibRecipe()
