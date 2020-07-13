import instaloader
from getpass import getpass
import re

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

username = input('Usuário: ')
password = getpass('Senha: ')

loader.login(username,password)

url = input('URL: ')
# https://www.instagram.com/p/CCfeQV-AssF/
expr = r'\/p\/([^\/]*)/'
found = re.search(expr, url)

if found:
  print("Baixando ", found.group(1), "...")
  post = instaloader.Post.from_shortcode(loader.context, found.group(1))
  loader.download_post(post, "downloads")
