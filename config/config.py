BOT_TOKEN: str = "OTIxNDUzMzY2MDc5NTIwODA5.YbzIUg.OVDMSc-M4_KuIcvL5oBYVV5M6rY"
SPOTIFY_ID: str = "gclarobatista"
SPOTIFY_SECRET: str = "dg.l.goncalo"

BOT_PREFIX = "!"

EMBED_COLOR = 0x4dd4d0  #replace after'0x' with desired hex code ex. '#ff0188' >> '0xff0188'

SUPPORTED_EXTENSIONS = ('.webm', '.mp4', '.mp3', '.avi', '.wav', '.m4v', '.ogg', '.mov')

MAX_SONG_PRELOAD = 5  #maximum of 25

COOKIE_PATH = "/config/cookies/cookies.txt"

GLOBAL_DISABLE_AUTOJOIN_VC = False

VC_TIMEOUT = 600 #seconds
VC_TIMOUT_DEFAULT = True  #default template setting for VC timeout true= yes, timeout false= no timeout
ALLOW_VC_TIMEOUT_EDIT = True  #allow or disallow editing the vc_timeout guild setting


STARTUP_MESSAGE = "Starting Bot..."
STARTUP_COMPLETE_MESSAGE = "Startup Complete"

NO_GUILD_MESSAGE = 'Vinde pá adega!'
USER_NOT_IN_VC_MESSAGE = "Queres ouvir um contiga, vinde pá adega!"
WRONG_CHANNEL_MESSAGE = "Error: Please use configured command channel"
NOT_CONNECTED_MESSAGE = "Deves pensar que te deixo as chaves da adega para entrares sozinho e me secares a cuba!"
ALREADY_CONNECTED_MESSAGE = "Já estou nessa adega!"
CHANNEL_NOT_FOUND_MESSAGE = "Não conheço essa adega!"
DEFAULT_CHANNEL_JOIN_FAILED = "Não estou em condições para entrar na minha adega preferida!"
INVALID_INVITE_MESSAGE = "O piruças rasgou-me o postal de convite!"

ADD_MESSAGE= "Se queres que vá cantar para outra freguesia, carrega [aqui]" #brackets will be the link text

INFO_HISTORY_TITLE = "Cantigas Tocadas:"
MAX_HISTORY_LENGTH = 10
MAX_TRACKNAME_HISTORY_LENGTH = 15

SONGINFO_UPLOADER = "Uploader: "
SONGINFO_DURATION = "Duração: "
SONGINFO_SECONDS = "s"
SONGINFO_LIKES = "Likes: "
SONGINFO_DISLIKES = "Dislikes: "
SONGINFO_NOW_PLAYING = "A tocar"
SONGINFO_QUEUE_ADDED = "Adicionada à lista de discos pedidos"
SONGINFO_SONGINFO = "Informação da cantiga"
SONGINFO_ERROR = "Ou não conheço esta cantiga, ou tem bolinha vermelha!"
SONGINFO_PLAYLIST_QUEUED = "Lista de discos pedidos :page_with_curl:"
SONGINFO_UNKNOWN_DURATION = "Desconhecida"

HELP_ADDBOT_SHORT = "Mandar DelfimFol para outra freguesia."
HELP_ADDBOT_LONG = "Gives you the link for adding this bot to another server of yours."
HELP_CONNECT_SHORT = "Entrar na adega."
HELP_CONNECT_LONG = "Chama o Delfim Fol para vir para adega."
HELP_DISCONNECT_SHORT = "Explusar o Delfim Fol da adega."
HELP_DISCONNECT_LONG = "Expulsa o Delfim Fol da adega e mete-lhe uma mordaça na boca."

HELP_SETTINGS_SHORT = "Ver os meus atributos."
HELP_SETTINGS_LONG = "Ver os meus atributos. Usa: {}settings setting_name value".format(BOT_PREFIX)

HELP_HISTORY_SHORT = "Mostrar o histórico de discos pedidos."
HELP_HISTORY_LONG = "Mostrar as ultimas " + str(MAX_TRACKNAME_HISTORY_LENGTH) + " cantigas tocadas."
HELP_PAUSE_SHORT = "Pausar a cantoria."
HELP_PAUSE_LONG = f"Pausar a cantoria. Para recomeçar usa o commando {BOT_PREFIX}resume."
HELP_VOL_SHORT = "Muda o volume."
HELP_VOL_LONG = "Muda o Volume. Toca tão alto quantos mais copos me deres (%)."
HELP_PREV_SHORT = "Interpretar a cantiga anterior."
HELP_PREV_LONG = "Interpretar a cantiga anterior."
HELP_RESUME_SHORT = "Retomar a cantoria depois de um bela macieira."
HELP_RESUME_LONG = "Retomar a cantoria depois de um bela macieira."
HELP_SKIP_SHORT = "Saltar a cantiga."
HELP_SKIP_LONG = "Parar a cantiga que estou a tocar e toco a próxima."
HELP_SONGINFO_SHORT = "Informação sobre a cantiga ataual."
HELP_SONGINFO_LONG = "Mostra detalhes sobre a cantiga que está a ser reproduzida e posta um link para a música."
HELP_STOP_SHORT = "Parar a cantoria."
HELP_STOP_LONG = "Parar a cantoria e pegar na lista de discos pedidos e limpar a peida."
HELP_YT_SHORT = "Play a supported link or search on youtube."
HELP_YT_LONG = ("$p [link/video title/key words/playlist-link/soundcloud link/spotify link/bandcamp link/twitter link]")
HELP_PING_SHORT = "Pong"
HELP_PING_LONG = "Test bot response status."
HELP_CLEAR_SHORT = "Limpar a peida com a folha dos discos pedidos."
HELP_CLEAR_LONG = "Limpa a peida com a folha dos discos pedidos e Clears the queue and skips the current song."
HELP_LOOP_SHORT = "Loops the currently playing song, toggle on/off."
HELP_LOOP_LONG = "Loops the currently playing song and locks the queue. Use the command again to disable loop."
HELP_QUEUE_SHORT = "Mostra todas as cantigas na lista de discos pedidos."
HELP_QUEUE_LONG = "Mostra todas as cantigas na lista de discos pedidos, até 10."
HELP_SHUFFLE_SHORT = "Embaralhar a lista de discos pedidos."
HELP_SHUFFLE_LONG = "Embaralhar a lista de discos pedidos."
HELP_CHANGECHANNEL_SHORT = "Mudar de adega."
HELP_CHANGECHANNEL_LONG = "Muda para VC que estás."

ABSOLUTE_PATH = '' #do not modify