import discord
from discord import app_commands

id_do_servidor =  1011364280240705596 #Coloque aqui o ID do seu servidor

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False #Nós usamos isso para o bot não sincronizar os comandos mais de uma vez

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #Checar se os comandos slash foram sincronizados 
            await tree.sync(guild = discord.Object(id=id_do_servidor)) # Você também pode deixar o id do servidor em branco para aplicar em todos servidores, mas isso fará com que demore de 1~24 horas para funcionar.
            self.synced = True
        print(f"Entramos como {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'fundador', description='dono') #Comando específico para seu servidor
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Estevam Rodrigues", ephemeral = True) 
  

aclient.run('MTAxMTY2Nzc2MDY3NTMwNzY3MQ.Gdx3yw.7uWU7D_401sXU-YuFhgPws1ovl9jg3186EcUmI')
 
 # Bot hospeado no replit, código desitado a quem precisar e para alimentar meu perfil.
 # Para rodar o bot, é preciso vincular a vonta do dd no Discord Desenvolvedor, criar o bot por lá e fazer com que ele entre no servidor e após isso
 # rodar esse código no Replit, lembrando que o id_do_servidor é o ID do seu servidor em questão e o aclient.run('exemplo') é a chave de acesso
 # do seu bot.
