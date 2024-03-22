import flet as ft  # importar
import datetime

def main(pagina):  # criar a função principal/main
    texto = ft.Text('MentorChat')

    chats = {}  # Dicionário para armazenar os chats de cada usuário

    chat_atual = None  # Para manter o controle do chat atualmente em exibição

    # Função para mudar o chat atual
    def mudar_chat(usuario):
        global chat_atual
        chat_atual = chats.get(usuario, None)
        if chat_atual:
            chat_area.content = [texto, ft.Spacer(height=20)] + chat_atual.controls

    # Layout da janela
    chat_area = ft.Column()  # Definindo a área de chat

    # Função para criar botões de usuário e atribuir a função mudar_chat
    def criar_botao_usuario(usuario):
        botao_usuario = ft.ElevatedButton(usuario, on_click=lambda evt, user=usuario: mudar_chat(user))
        return botao_usuario

    lista_chats = ft.Column()  # Criar uma coluna para adicionar botões de usuário dinamicamente

    # Função para atualizar a lista de chats
    def atualizar_lista_chats():
        lista_chats.content = [criar_botao_usuario(usuario) for usuario in chats.keys()]

    layout = ft.Row([
        ft.Column([
            ft.Text("Chats"),
            lista_chats
        ]),
        chat_area  # Esta área será usada para exibir o chat atual
    ])

    def enviar_mensagem_tunel(mensagem):
        print(mensagem)
        # adicionar a mensagem no chat
        texto_mensagem = ft.Text(f"{mensagem}")
        chat_atual.controls.append(texto_mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        print('Send message')
        data_hora_atual = datetime.datetime.now()
        data_atual = data_hora_atual.strftime("%d/%m/%y")
        hora_atual = data_hora_atual.strftime("%H:%M")
        pagina.pubsub.send_all(f'[{hora_atual}, {data_atual}] {nome_usuario.value}:  {campo_mensagem.value}')
        # limpar campo mensagem
        campo_mensagem.value = ''
        pagina.update()

    campo_mensagem = ft.TextField(label='Type your message', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Send', on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])

    def entrar_chat(evento):
        print("Join chat")
        data_hora_atual = datetime.datetime.now()
        data_atual = data_hora_atual.strftime("%d/%m/%y")
        hora_atual = data_hora_atual.strftime("%H:%M")
        # fechar o popup
        popup.open = False
        # tirar o botão iniciar chat
        pagina.remove(botao_iniciar)
        # tirar o título hashzap
        pagina.remove(texto)
        # criar o chat
        pagina.add(layout)
        chat_atual = ft.Column()  # Criar o chat para o usuário atual
        chats[nome_usuario.value] = chat_atual  # Adicionar ao dicionário de chats
        atualizar_lista_chats()  # Atualizar a lista de chats com o novo usuário
        pagina.pubsub.send_all(f"[{hora_atual}, {data_atual}] {nome_usuario.value} joined the chat")
        # colocar o campo de digitar mensagem
        # criar o botão de enviar
        pagina.add(linha_enviar)
        pagina.update()

    titulo_popup = ft.Text("Welcome to MentorChat!")
    nome_usuario = ft.TextField(label="Type your name", on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton("Join Chat", on_click=entrar_chat)
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar],
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()  # para atualizar o visual da página sem que o usuário precise apertar f5

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER)  # criar o app chamando a função principal