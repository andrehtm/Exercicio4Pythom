# passo 1: botão de iniciar chat
# passo 2: pop up para entrar no site
# passo 3: quando iniciar o chat
    # 3.1 mensagem de quem entrou no chat
    # 3.2 visualizar campo e botao para digitar e enviar as mensagens
# passo 4: a cada mensagem enviada
    # nome: texto da mensagem

# Para criação de páginas/apps utilizaremos a biblioteca flet, sendo utilizado basicamente em 3 etapas
    # importar a biblioteca, criação de função (main) para a página principal, no final do projeto utilizar "flet.app(target= função main criada)" para executar 

import flet as ft

def main(pagina):
    texto = ft.Text("SoundLess Chat")

    chat = ft.Column()

    nome_usuario = ft.TextField(label="Escreva seu nome")

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            #adicionar mensagem
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem}: entrou no chat", size=12, italic=True, color=ft.colors.LIGHT_GREEN))
        pagina.update()

    #interação no túnel
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value, "tipo": "mensagem"})
        #limpar o campo de mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite sua mensagem")
    botao_enviarmensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_popup(evento):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        #adicionar o chat
        pagina.add(chat)
        #fechar o popup
        popup.open=False
        #remover o botão de iniciar chat
        pagina.remove(botao_iniciar)
        #criar o campo de mensagem e botão de enviar em uma linha
        pagina.add(ft.Row(
                   [campo_mensagem, botao_enviarmensagem]))

        pagina.remove(texto)
        pagina.update()


    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao SoundLess Chat"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)]
    )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)
   
   
   
   
    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER, port=13000)
#192.168.1.16