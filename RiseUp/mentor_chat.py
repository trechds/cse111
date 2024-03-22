import flet as ft # importar
import datetime

def main(pagina): # criar a função principal/main
    texto = ft.Text('MentorChat')

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
         print(mensagem)
         # adicionar a mensagem no chat
         texto_mensagem = ft.Text(f"{mensagem}")
         chat.controls.append(texto_mensagem)
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
            pagina.add(chat)
            pagina.pubsub.send_all(f"[{hora_atual}, {data_atual}] {nome_usuario.value} joined the chat")
            # colocar o campo de diggitar mensagem
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
        pagina.update() # para atualizar o visual da página sem que o usuário precise apertar f5

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)


ft.app(target=main, view=ft.WEB_BROWSER) # criar o app chamando a função principal