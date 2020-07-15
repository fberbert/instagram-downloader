import instaloader
from getpass import getpass
import re
import os
import sys

#verificar se a URL foi informada
try:
    url = sys.argv[1]
except IndexError:
    print("Forma de uso:\n\n", sys.argv[0], "URL\n\nInforme uma URL válida\n\n")
    sys.exit()

#diretório de download
downloadDir = '/home/fabio/Downloads'
os.chdir(downloadDir)

loader = instaloader.Instaloader(
  download_pictures=True, 
  download_videos=True, 
  download_video_thumbnails=False, 
  download_geotags=False,
  download_comments=False, 
  save_metadata=False, 
  compress_json=False,
  filename_pattern='{profile}_{mediaid}'
  )

#o login é opcional, necessário somente no 
#caso de download de posts de contas privadas
#comente as próximas 3 linhas caso esteja
#fazendo download de posts de contas públicas
# username = input('Usuário: ')
# password = getpass('Senha: ')
# loader.login(username,password)

#extrair "short_code" da URL
#exemplo: https://www.instagram.com/p/CCfeQV-AssF/
expr = r'\/p\/([^\/]*)/'
found = re.search(expr, url)

if found:
  print("Baixando ", found.group(1), "...")
  post = instaloader.Post.from_shortcode(loader.context, found.group(1))
  loader.download_post(post, ".")
