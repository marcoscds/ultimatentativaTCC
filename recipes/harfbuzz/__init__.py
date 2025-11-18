import os
from pythonforandroid.recipes.harfbuzz import HarfbuzzRecipe
from pythonforandroid.util import current_directory, shprint
import sh

# Esta receita herda da receita Harfbuzz padrão do p4a,
# para garantir que todos os passos de compilação (configure, make) sejam executados.

class HarfbuzzFixRecipe(HarfbuzzRecipe):
    """
    Receita customizada para Harfbuzz que injeta flags de compilação
    para desativar o erro -Werror (treat warnings as errors), resolvendo
    falhas no NDK devido a variáveis não utilizadas (unused-but-set-variable).
    """
    # Sobrescreve o nome da receita, forçando o p4a a usá-la
    name = 'harfbuzz'

    def build_arch(self, arch):
        # Pega as variáveis de ambiente base da receita padrão
        env = self.get_recipe_env(arch)

        # A sua lista completa de flags para mitigar erros de NDK
        no_error_flags = (
            " -Wno-error"
            " -Wno-error=unused-but-set-variable"
            " -Wno-error=deprecated-declarations"
            " -Wno-error=cast-function-type-strict"
        )

        # --- CORREÇÃO CRÍTICA: INJETAR FLAGS DE COMPILAÇÃO ---
        # Adiciona as flags de mitigação às variáveis CFLAGS e CXXFLAGS
        env['CFLAGS'] = env.get('CFLAGS', '') + no_error_flags
        env['CXXFLAGS'] = env.get('CXXFLAGS', '') + no_error_flags
        # ----------------------------------------------------

        with current_directory(self.get_build_dir(arch.arch)):
            # Chama a compilação (make) com o ambiente modificado
            shprint(sh.make, '-j', str(self.cpu_count), _env=env)

            # Instalação padrão (herdada)
            shprint(sh.make, 'install', _env=env)

            # Limpeza e instalação final (herdada)
            self.install_headers(arch)


# O p4a espera que a variável de entrada tenha o mesmo nome da receita (harfbuzz)
recipe = HarfbuzzFixRecipe()
