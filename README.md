# auto-podcast-update
Automatically checks and downloads podcasts listed in feeds.txt, then uploads them to your mp3 player whenever it's connected

#Installation (Only tested in Debian)
1. Change the 'RUN' path in 100-update-mp3-pocasts.rules to your installation path.
2. Change the idVendor and idProduct attributes in 100-update-mp3-podcasts.rules to your device's own values. You can find these by connecting your mp3 player and using the lsusb command in the CLI.
3. Move 100-update-mp3-podcasts.rules to the /etc/udev/rules.d directory.
4. Change PROJECT_PATH in mount_mp3.sh to your installation path.
5. Change MOUNT_PATH in mount_mp3.sh to wherever you want the mp3 player to be mounted.
6. You may need to change DEST_PATH to reflect your mp3 players file system. For a Sony Walkman is it /MUSIC and we create a podcasts folder.
7. Change the dev variable in podcast_rss.py to your installation path.
8. Create a cron job to run podcast_rss.py however often you want it to check and download new podcasts.


#Adding more feeds
Copy and paste the RSS URL into a new line of feeds.txt
