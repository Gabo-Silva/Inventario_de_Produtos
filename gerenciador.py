def criarTabela():
    # Criação do banco de dados e da tabela.
    import sqlite3
    conexao = sqlite3.connect('estoque.db')
    cursor = conexao.cursor()
    cursor.execute(''' create table if not exists produtos (
                   id integer primary key not null,
                   nome varchar(100) unique not null,
                   categoria varchar(100) not null,
                   quantidade integer unsigned not null,
                   preco decimal(10, 2) not null
                );
''')


def continuar(msg):
    # Função que somente pode retornar os valores S ou N).
    while True:
        try:
            res = str(input(msg).strip().upper())
        # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
        except KeyboardInterrupt:
            print('\nERRO! OPÇÃO INVÁLIDA')
            print('-' * 50)
        # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
        except EOFError:
            print('ERRO! OPÇÃO INVÁLIDA')
            print('-' * 50)
        else:
            # Caso a variável "res" não seja S ou N, uma mensagem de erro será exibida.
            if res not in ('S', 'N'):
                print('ERRO! OPÇÃO INVÁLIDA')
                print('-' * 50)
            # Caso tudo ocorra bem, a variável "res" será retornada.
            else:
                return res


def leiaInt(msg):
    while True:
        try:
            num = str(input(msg).strip())
        # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
        except KeyboardInterrupt:
            print('\nERRO! NÚMERO INVÁLIDO')
            print('-' * 50)
        # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
        except EOFError:
            print('ERRO! NÚMERO INVÁLIDO')
            print('-' * 50)
        else:
            # Caso o parâmetro "msg" for igual ao texto colocado no if abaixo, esse bloco de comando será ativado.
            if msg == 'Nova Quantidade em Estoque: ':
                # Caso a variável "num" não contenha somente números ou o número seja menor do que 0, uma mensagem de erro será exibida.
                if num.isnumeric() == False or int(num) < 0:
                    print('ERRO! NÚMERO INVÁLIDO')
                    print('-' * 50)
                else:
                    # Caso tudo ocorra bem, a variável "num" será retornada sendo um valor inteiro.
                    return int(num)
            # Caso a variável "num" não contenha somente números ou o número seja menor do que 1, uma mensagem de erro será exibida.
            elif num.isnumeric() == False or int(num) < 1:
                print('ERRO! NÚMERO INVÁLIDO')
                print('-' * 50)
            else:
                # Caso o parâmetro "msg" for igual ao texto colocado no if abaixo, esse bloco de comando será ativado.
                if msg == 'Digite sua escolha: ':
                    # Caso a variável "num" for igual a 1 ou 2, a variável "num" será retornada sendo um valor inteiro.
                    if int(num) == 1 or int(num) == 2:
                        return int(num)
                    # Caso a variável "num" não seja 1 ou 2, uma mensagem de erro será exibida.
                    else:
                        print('ERRO! OPÇÃO INVÁLIDA')
                        print('-' * 50)
                else:
                    # Variável "num" será retornada sendo um valor inteiro.
                    return int(num)


def leiaStr(msg):
    while True:
        # Caso o parâmetro "msg" for igual ao texto colocado no if abaixo, esse bloco de comando será ativado.
        if msg == 'Nome do Produto':
            try:
                nome_do_produto = str(input(f'{msg}: ').strip().title())
            # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
            except KeyboardInterrupt:
                print('\nERRO! NOME INVÁLIDO')
                print('-' * 50)
            # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
            except EOFError:
                print('ERRO! NOME INVÁLIDO')
                print('-' * 50)
            else:
                # Se a variável "nome_do_produto" não tiver nenhuma caractere, uma mensagem de erro será exibida.
                if len(nome_do_produto) == 0:
                    print('ERRO! NOME INVÁLIDO')
                    print('-' * 50)
                # Caso tudo ocorra bem, a variável "nome_do_produto" será retornada.
                else:
                    return nome_do_produto
        # Caso o parâmetro "msg" for igual ao texto colocado no elif abaixo, esse bloco de comando será ativado.
        elif msg == 'Categoria do Produto':
            try:
                categoria_do_produto = str(input(f'{msg}: ').strip().title())
                # Transforma a variável "categoria_do_produto" em uma lista.
                categoria_sem_espacos = categoria_do_produto.split()
            # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
            except KeyboardInterrupt:
                print('\nERRO! CATEGORIA INVÁLIDA')
                print('-' * 50)
            # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
            except EOFError:
                print('ERRO! CATEGORIA INVÁLIDA')
                print('-' * 50)
            else:
                # Junta toda a lista em uma única string. Caso todas as caracteres sejam letras do alfabeto, a variável "categoria_do_produto" será retornada.
                if ''.join(categoria_sem_espacos).isalpha():
                    return categoria_do_produto
                # Caso alguma caractere não seja uma letra do alfabeto, uma mensagem de erro será exibida.
                else:
                    print('ERRO! CATEGORIA INVÁLIDA')
                    print('-' * 50)


def leiaFloat(msg):
    while True:
        try:
            preco_do_produto = float(input(msg))
            # Faz uma lista com a variável "preco_do_produto" usando o ponto como separador.
            separador_decimal = str(preco_do_produto).split('.')
        # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
        except KeyboardInterrupt:
            print('\nERRO! VALOR INVÁLIDO')
            print('-' * 50)
        # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
        except EOFError:
            print('ERRO! VALOR INVÁLIDO')
            print('-' * 50)
        # Caso o usuário coloque algum valor indevido, uma mensagem de erro será exibida.
        except ValueError:
            print('ERRO! VALOR INVÁLIDO')
            print('-' * 50)
        else:
            # Se a parte decimal tive mais de 2 caracteres ou a variável "preco_do_produto" for menor do que 0 ou a parte inteira tive mais de 8 caracteres, uma mensagem de erro será exibida.
            if len(separador_decimal[1]) > 2 or preco_do_produto < 0 or len(separador_decimal[0]) > 8:
                print('ERRO! VALOR INVÁLIDO')
                print('-' * 50)
            # Caso tudo ocorra bem, a variável "preco_do_produto" será retornada.
            else:
                return preco_do_produto


def menu(* opcoes):
    # Criação do banco de dados e da tabela.
    criarTabela()
    # Menu principal.
    print('-' * 50)
    print('Inventário de Produtos'.center(50))
    print('-' * 50)
    for indice, op in enumerate(opcoes):
        print(f'{indice + 1} - {op}')
    print('-' * 50)
    while True:
        # Recebendo a opção que o usuário deseja.
        res_opcao = leiaInt('Escolha uma opção: ')
        # Se a opção escolhida for maior que a lista de opções, uma mensagem de erro será exibida.
        if res_opcao > len(opcoes):
            print('ERRO! NÚMERO INVÁLIDO')
            print('-' * 50)
        # Caso tudo ocorra bem, a variável "res_opcao" será retornada.
        else:
            return res_opcao


def adicionar():
    while True:
        import sqlite3
        # Se conectando com o banco de dados.
        conexao = sqlite3.connect('estoque.db')
        cursor = conexao.cursor()
        print('-' * 50)
        print('NOVO PRODUTO'.center(50))
        print('-' * 50)
        # Recebendo as informações do produto.
        nome = leiaStr('Nome do Produto')
        print('-' * 50)
        quantidade = leiaInt('Quantidade em Estoque: ')
        print('-' * 50)
        preco = leiaFloat('Preço do Produto: R$')
        print('-' * 50)
        categoria = leiaStr('Categoria do Produto')
        print('-' * 50)
        # Adicionando a informações na tabela.
        cursor.execute(
            f'insert into produtos (nome, quantidade, preco, categoria) values ("{nome}", "{quantidade}", "{preco}", "{categoria}")')
        conexao.commit()
        print('CADASTRO CONCLUÍDO'.center(50))
        print('-' * 50)
        # Variável que recebe a resposta se o usuário quer continuar ou não.
        continuar_res = continuar('Quer Continuar[S/N]? ')
        # Caso não, o banco de dados será fechado e a função se encerrará.
        if continuar_res == 'N':
            conexao.close()
            break


def exibir():
    import sqlite3
    # Se conectando com o banco de dados.
    conexao = sqlite3.connect('estoque.db')
    cursor = conexao.cursor()
    # Pegando todos os registros feitos.
    cursor.execute('select * from produtos')
    # Se não ouver nenhum registro, esse bloco de comando será ativado.
    if len(cursor.fetchall()) == 0:
        print('-' * 50)
        print('NENHUM PRODUTO CADASTRADO'.center(50))
        return print('-' * 50)
    else:
        # Pegando todos os registros feitos novamente.
        cursor.execute('select * from produtos')
        print('-' * 50)
        print('Listagem dos Produtos'.center(50))
        print('-' * 50)
        # Apresentando as informações de cada registro.
        for produto in cursor.fetchall():
            print(f'ID: {produto[0]}')
            print(f'NOME: {produto[1]}')
            print(f'CATEGORIA: {produto[2]}')
            print(f'QUANTIDADE: {produto[3]}')
            print(f'PREÇO: R${produto[4]:.2f}')
            print('-' * 50)
        while True:
            # Variável que recebe a resposta se o usuário quer sair.
            res_continuar = continuar('Sair[S]? ')
            # Se a resposta for "S", o banco de dados será fechado e a função se encerrará.
            if res_continuar == 'S':
                conexao.close()
                break
            # Caso a resposta seja qualquer coisa que não seja "S", uma mensagem de erro será exibida.
            else:
                print('ERRO! OPÇÃO INVÁLIDA')
                print('-' * 50)


def buscar():
    import sqlite3
    # Se conectando com o banco de dados.
    conexao = sqlite3.connect('estoque.db')
    cursor = conexao.cursor()
    # Pegando todos os registros feitos.
    cursor.execute('select * from produtos')
    # Se não ouver nenhum registro, esse bloco de comando será ativado.
    if len(cursor.fetchall()) == 0:
        print('-' * 50)
        print('NENHUM PRODUTO CADASTRADO'.center(50))
        return print('-' * 50)
    else:
        while True:
            # Variável que será responsavel por contar as pessoas ou categorias que forem achadas.
            cont_achados = 0
            print('-' * 50)
            print('PESQUISADOR DE PRODUTOS'.center(50))
            print('-' * 50)
            try:
                # Nome ou categoria do produto que será procurado.
                nome_do_item = str(
                    input('Digite o nome ou a categoria do produto: ').strip().title())
            # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
            except KeyboardInterrupt:
                print('\nERRO! PRODUTO INEXISTENTE')
                print('-' * 50)
            # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
            except EOFError:
                print('ERRO! PRODUTO INEXISTENTE')
                print('-' * 50)
            else:
                # Pegando todos os registros feitos novamente.
                cursor.execute('select * from produtos')
                print('-' * 50)
                for nome in cursor.fetchall():
                    # Se o nome do produto registrado for igual ao nome do produto digitado pelo usuário ou alguma categoria registrada for igual ao nome da categoria digitada pelo usuário, será exibido as informações do produto.
                    if nome[1] == nome_do_item or nome[2] == nome_do_item:
                        print(f'ID: {nome[0]}')
                        print(f'NOME: {nome[1]}')
                        print(f'CATEGORIA: {nome[2]}')
                        print(f'QUANTIDADE: {nome[3]}')
                        print(f'PREÇO: R${nome[4]:.2f}')
                        print('-' * 50)
                        # A variável "cont_achados" ganha +1 pra cada produto ou categoria registrado igual ao nome do produto ou categoria digitado pelo usuário.
                        cont_achados += 1
                # Se a variável "cont_achados" for igual a 0, esse bloco de comando será ativado.
                if cont_achados == 0:
                    print('ERRO! PRODUTO INEXISTENTE')
                    print('-' * 50)
            finally:
                # Variável que recebe a resposta se o usuário quer continuar ou não.
                continuar_res = continuar('Quer Continuar[S/N]? ')
                # Caso não, o banco de dados será fechado e a função se encerrará.
                if continuar_res == 'N':
                    conexao.close()
                    break


def atualizar():
    import sqlite3
    # Se conectando com o banco de dados.
    conexao = sqlite3.connect('estoque.db')
    cursor = conexao.cursor()
    # Pegando todos os registros feitos.
    cursor.execute('select * from produtos')
    # Se não ouver nenhum registro, esse bloco de comando será ativado.
    if len(cursor.fetchall()) == 0:
        print('-' * 50)
        print('NENHUM PRODUTO CADASTRADO'.center(50))
        return print('-' * 50)
    else:
        while True:
            # Variável que será responsavel por contar as pessoas que foram achadas.
            cont_achados = 0
            # Variável que será responsavel por contar os ids que forem achados.
            cont_achados_id = 0
            print('-' * 50)
            print('ATUALIZAR PRODUTOS'.center(50))
            print('-' * 50)
            try:
                # Nome do produto que será procurado.
                nome_produto_atualizar = str(
                    input('Qual produto você deseja atualizar? ').strip().title())
            # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
            except KeyboardInterrupt:
                print('\nERRO! PRODUTO INEXISTENTE')
                print('-' * 50)
            # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
            except EOFError:
                print('ERRO! PRODUTO INEXISTENTE')
                print('-' * 50)
            else:
                # Pegando todos os registros feitos novamente.
                cursor.execute('select * from produtos')
                print('-' * 50)
                for produto in cursor.fetchall():
                    # Se o nome do produto registrado for igual ao nome do produto digitado pelo usuário, será exibido as informações do produto.
                    if produto[1] == nome_produto_atualizar:
                        print(f'ID: {produto[0]}')
                        print(f'NOME: {produto[1]}')
                        print(f'CATEGORIA: {produto[2]}')
                        print(f'QUANTIDADE: {produto[3]}')
                        print(f'PREÇO: R${produto[4]:.2f}')
                        print('-' * 50)
                        # A variável "cont_achados" ganha +1 pra cada produto registrado igual ao nome do produto digitado pelo usuário.
                        cont_achados += 1
                # Se a variável "cont_achados" for igual a 0, esse bloco de comando será ativado.
                if cont_achados == 0:
                    print('ERRO! PRODUTO INEXISTENTE')
                    print('-' * 50)
                else:
                    while True:
                        # Recebendo o ID do produto que será atualizado.
                        id_produto = leiaInt(
                            'Digite o ID do produto que deseja atualizar: ')
                        # Pegando todos os registros feitos novamente.
                        cursor.execute('select * from produtos')
                        for produto in cursor.fetchall():
                            # Se algum id registrado for igual o id digitado pelo usuário e se o nome de produto registrado também for igual ao nome do produto digitado pelo usuário, esse bloco de comando será ativado.
                            if produto[0] == id_produto and produto[1] == nome_produto_atualizar:
                                cont_achados_id += 1
                        # Se a variável "cont_achados_id" for igual a 0, esse bloco de comando será ativado.
                        if cont_achados_id == 0:
                            print('ERRO! NÚMERO INVÁLIDO')
                            print('-' * 50)
                        else:
                            print('-' * 50)
                            print(
                                'O que você deseja alterar?\n[1] Quantidade\n[2] Preço')
                            print('-' * 50)
                            # Resposta do que o usuário deseja atualizar.
                            res_alteracao = leiaInt('Digite sua escolha: ')
                            print('-' * 50)
                            # Se a resposta for 1, a quantidade será alterada.
                            if res_alteracao == 1:
                                nova_informação = leiaInt(
                                    'Nova Quantidade em Estoque: ')
                                # Atualizandor a informação.
                                cursor.execute(
                                    f'update produtos set quantidade = "{nova_informação}" where id = "{id_produto}"')
                            # Se a resposta for 2, o preço será alterado.
                            elif res_alteracao == 2:
                                nova_informação = leiaFloat(
                                    'Novo Preço do Produto: R$')
                                # Atualizandor a informação.
                                cursor.execute(
                                    f'update produtos set preco = "{nova_informação}" where id = "{id_produto}"')
                            # Mensagem de conclusão.
                            print('-' * 50)
                            print('PRODUTO ATUALIZADO COM SUCESSO'.center(50))
                            conexao.commit()
                            print('-' * 50)
                            break
            finally:
                # Variável que recebe a resposta se o usuário quer continuar ou não.
                continuar_res = continuar('Quer Continuar[S/N]? ')
                # Caso não, o banco de dados será fechado e a função se encerrará.
                if continuar_res == 'N':
                    conexao.close()
                    break


def excluir():
    import sqlite3
    # Se conectando com o banco de dados.
    conexao = sqlite3.connect('estoque.db')
    cursor = conexao.cursor()
    # Pegando todos os registros feitos.
    cursor.execute('select * from produtos')
    # Se não ouver nenhum registro, esse bloco de comando será ativado.
    if len(cursor.fetchall()) == 0:
        print('-' * 50)
        print('NENHUM PRODUTO CADASTRADO'.center(50))
        return print('-' * 50)
    else:
        while True:
            # Variável que será responsavel por contar as pessoas que foram achadas.
            cont_achados = 0
            # Variável que será responsavel por contar os ids que forem achados.
            cont_achados_id = 0
            print('-' * 50)
            print('EXCLUIR PRODUTOS'.center(50))
            print('-' * 50)
            try:
                # Nome do produto que será procurado.
                nome_produto_excluir = str(
                    input('Qual produto você deseja excluir? ').strip().title())
            # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
            except KeyboardInterrupt:
                print('\nERRO! PRODUTO INEXISTENTE')
                print('-' * 50)
            # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
            except EOFError:
                print('ERRO! PRODUTO INEXISTENTE')
                print('-' * 50)
            else:
                # Pegando todos os registros feitos novamente.
                cursor.execute('select * from produtos')
                print('-' * 50)
                for produto in cursor.fetchall():
                    # Se o nome do produto registrado for igual ao nome do produto digitado pelo usuário, será exibido as informações do produto.
                    if produto[1] == nome_produto_excluir:
                        print(f'ID: {produto[0]}')
                        print(f'NOME: {produto[1]}')
                        print(f'CATEGORIA: {produto[2]}')
                        print(f'QUANTIDADE: {produto[3]}')
                        print(f'PREÇO: R${produto[4]:.2f}')
                        print('-' * 50)
                        # A variável "cont_achados" ganha +1 pra cada produto registrado igual ao nome do produto digitado pelo usuário.
                        cont_achados += 1
                # Se a variável "cont_achados" for igual a 0, esse bloco de comando será ativado.
                if cont_achados == 0:
                    print('ERRO! PRODUTO INEXISTENTE')
                    print('-' * 50)
                else:
                    while True:
                        # Recebendo o ID do produto que será excluído.
                        id_produto = leiaInt(
                            'Digite o ID do produto que deseja excluir: ')
                        # Pegando todos os registros feitos novamente.
                        cursor.execute('select * from produtos')
                        for produto in cursor.fetchall():
                            # Se algum id registrado for igual o id digitado pelo usuário e se o nome de produto registrado também for igual ao nome do produto digitado pelo usuário, esse bloco de comando será ativado.
                            if produto[0] == id_produto and produto[1] == nome_produto_excluir:
                                cont_achados_id += 1
                        # Se a variável "cont_achados_id" for igual a 0, esse bloco de comando será ativado.
                        if cont_achados_id == 0:
                            print('ERRO! NÚMERO INVÁLIDO')
                            print('-' * 50)
                        else:
                            # Deletando o produto da tabela.
                            cursor.execute(
                                f'delete from produtos where id= "{id_produto}"')
                            # Mensagem de conclusão.
                            print('-' * 50)
                            print('PRODUTO EXCLUÍDO COM SUCESSO'.center(50))
                            conexao.commit()
                            print('-' * 50)
                            break
            finally:
                # Pegando todos os registros feitos novamente.
                cursor.execute('select * from produtos')
                # Se não ouver nenhum registro, esse bloco de comando será ativado.
                if len(cursor.fetchall()) == 0:
                    conexao.close()
                    print('-' * 50)
                    print('NENHUM PRODUTO CADASTRADO'.center(50))
                    print('-' * 50)
                    break
                else:
                    # Variável que recebe a resposta se o usuário quer continuar ou não.
                    continuar_res = continuar('Quer Continuar[S/N]? ')
                    # Caso não, o banco de dados será fechado e a função se encerrará.
                    if continuar_res == 'N':
                        conexao.close()
                        break


def valor_total_estoque():
    import sqlite3
    # Se conectando com o banco de dados.
    conexao = sqlite3.connect('estoque.db')
    cursor = conexao.cursor()
    # Pegando todos os registros feitos.
    cursor.execute('select * from produtos')
    # Se não ouver nenhum registro, esse bloco de comando será ativado.
    if len(cursor.fetchall()) == 0:
        print('-' * 50)
        print('NENHUM PRODUTO CADASTRADO'.center(50))
        return print('-' * 50)
    else:
        soma = 0
        # Pegando todos os registros feitos novamente.
        cursor.execute('select * from produtos')
        print('-' * 50)
        print('VALOR TOTAL DO ESTOQUE'.center(50))
        print('-' * 50)
        for produto in cursor.fetchall():
            # Calculando o valor da mercadoria.
            valor_produto = produto[3] * produto[4]
            # Calculando o valor do estoque.
            soma += valor_produto
            # Apresentando as informações de cada registro.
            print(f'ID: {produto[0]}')
            print(f'NOME: {produto[1]}')
            print(f'CATEGORIA: {produto[2]}')
            print(f'QUANTIDADE: {produto[3]}')
            print(f'PREÇO: R${produto[4]:.2f}')
            print(f'VALOR TOTAL DO PRODUTO: R${valor_produto:.2f}')
            print('-' * 50)
        # Apresentando o valor total do estoque.
        print(f'VALOR TOTAL DO ESTOQUE: R${soma:.2f}')
        print('-' * 50)
        while True:
            # Variável que recebe a resposta se o usuário quer sair.
            continuar_res = continuar('Sair[S]? ')
            # Se a resposta for "S", o banco de dados será fechado e a função se encerrará.
            if continuar_res == 'S':
                conexao.close()
                break
            # Caso não, o banco de dados será fechado e a função se encerrará.
            else:
                print('ERRO! OPÇÃO INVÁLIDA')
                print('-' * 50)
