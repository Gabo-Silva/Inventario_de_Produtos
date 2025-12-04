# Importando minhas funções.
import gerenciador
while True:
    # Chamando a função que irá fazer o menu.
    res_usuario = gerenciador.menu('Adicionar Produtos', 'Listar Todos os Produtos',
                                   'Buscar Produtos', 'Atualizar Informações', 'Remover Produtos', 'Ver Valor Total do Estoque', 'Sair')
    # Dependendo da função escolhida pelo usuário, um bloco de comando será ativado e sua respectiva função será chamada.
    if res_usuario == 1:
        gerenciador.adicionar()
    elif res_usuario == 2:
        gerenciador.exibir()
    elif res_usuario == 3:
        gerenciador.buscar()
    elif res_usuario == 4:
        gerenciador.atualizar()
    elif res_usuario == 5:
        gerenciador.excluir()
    elif res_usuario == 6:
        gerenciador.valor_total_estoque()
    elif res_usuario == 7:
        break
# Fim.
print('-' * 50)
print('OBRIGADO POR USAR O MEU GERENCIADOR DE PRODUTOS'.center(50))
print('-' * 50)
