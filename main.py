import subprocess


def message():
    message = (
        "\n\nCertifique-se de ter o seu token do GitHub em mãos, pois será usado futuramente.\n"
        "Caso não tenha, acesse o link https://github.com/ e siga os passos abaixo:\n"
        "1. Clique na sua foto de perfil no canto superior direito da página.\n"
        "2. Clique em 'Settings'.\n"
        "3. No menu lateral esquerdo, clique em 'Developer settings'.\n"
        "4. No menu lateral esquerdo, clique em 'Personal access tokens'.\n"
        "5. Após isso, clicar em Tokens (classic)"
        "6. Clique em 'Generate new token e Generate new token (classic)'.\n"
        "7. Preencha o campo 'Note' com um nome para o token e modifique a barra de 'Expiration' para 'No expiration'.\n"
        "8. Selecione as permissões necessárias para o seu token (se não souber o que são essas permissões, não selecione nenhuma!).\n"
        "9. Clique em 'Generate token'.\n"
        "10. Copie o token gerado e guarde-o em um local seguro.\n"
    )

    print(message)


def get_credentials():
    name = input("Informe o nome que você definiu na sua conta do GitHub: ")
    email = input("Informe o email cadastrado no GitHub: ")
    token = input("Informe o token do GitHub: ")

    return name, email, token


def generate_shell_script(name: str, email: str, token: str):
    subprocess.run("sudo apt update", shell=True)
    subprocess.run("sudo apt upgrade", shell=True)

    subprocess.run("sudo apt install git", shell=True)

    # Configurações de identidade
    subprocess.run(f'git config --global user.name "{name}"', shell=True)
    subprocess.run(f'git config --global user.email "{email}"', shell=True)

    # Para definir o nome do ramo padrão como 'main'
    subprocess.run("git config --global init.defaultBranch main", shell=True)

    # Criando o alias chamado 'tree' para depois usar como: git tree
    subprocess.run(
        'git config --global alias.tree "log --oneline --graph --decorate --all"',
        shell=True,
    )

    # Deixando a estratégia de rebase como padrão para o git pull
    subprocess.run("git config --global pull.rebase true", shell=True)

    # Salvando as credenciais do GitHub
    subprocess.run(f"git config --global github.token {token}", shell=True)
    subprocess.run("git config --global credential.helper store", shell=True)


def first_clone():
    print("\n\nUm repositório exemplo está sendo clonado para o seu computador.\n\n")

    subprocess.run("git clone https://github.com/lucascraupp/lucascraupp", shell=True)


message()
name, email, token = get_credentials()
generate_shell_script(name, email, token)
first_clone()
