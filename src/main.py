import os
import requests
from bs4 import BeautifulSoup


class soundcloudMp3:
    def __init__(self, url, length_raw):
        self.url = url
        self.length_raw = length_raw
        self.length = f"{round(int(self.length_raw) / 1024 / 1024, 2)}mb"


if "SOUNDCLOUD_RSS" not in os.environ:
    print("'SOUNDCLOUD_RSS' EnVar doesn't exist")
    exit()

if "DOWNLOAD_DIR" not in os.environ:
    print("'DOWNLOAD_DIR' EnVar doesn't exist")
    exit()

print("Collecting SoundCloud feed")
soundcloud_page = requests.get(url=os.environ["SOUNDCLOUD_RSS"]).text

print("Extracting MP3's from feed")
downloads = []
soup = BeautifulSoup(soundcloud_page, "html.parser")
for enclosure in soup.find_all("enclosure"):
    downloads.append(soundcloudMp3(enclosure.attrs["url"], enclosure.attrs["length"]))

print("Ensuring download dir exists")
if not os.path.exists(os.environ["DOWNLOAD_DIR"]):
    print(f"Creating: {os.environ['DOWNLOAD_DIR']}")
    os.makedirs(os.environ["DOWNLOAD_DIR"])


print("Check if already downloaded")
for download in downloads:
    print(f"url: {download.url.split('/')[-1]} length: {download.length}")
    file_path = f"{os.environ['DOWNLOAD_DIR']}{download.url.split('/')[-1]}"
    if not os.path.isfile(file_path):
        print(f"Downloading {download.url.split('/')[-1]}")
        mp3 = requests.get(download.url)
        with open(file_path, "wb") as f:
            f.write(mp3.content)
