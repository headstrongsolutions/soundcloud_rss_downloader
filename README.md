# SoundCloud Feed MP3 Downloader

## Syncs to a local directory and downloads missing files

Requires two Environmental Variables to be set, `SOUNDCLOUD_RSS` and `DOWNLOAD_DIR`.
In the `.vscode\launch.json` file there is an example of both of these, they target a folder in my Steamdecks `~/Music` directory called `n-type` for the download directory and the URL for n-type's soundcloud RSS feed.

..so yes, this is an extremely naive (as in I don't do much error checking, works on my machine this one time I've run it so that's good enough for my purposes) RSS Feed Download Script, my plan is to probably chuck it onto a computer and cron job it every nigth at 1:00 in the morning or some such nonsense.

Other notes, it uses BeautifulSoup4 and requests to do the download and enough os file stuff to make sure it can check for dir/file exists. That's pretty much it. Really simple stuff to be fair.

I started playing with dataclasses for the download object (filesize/URL) but was tripping over dynamic values (as in self.size_in_mb = f"{self.size_in_bytes/1024/1024}mb"), so I just created a standard class object and created the dynamic value in the init dunder.