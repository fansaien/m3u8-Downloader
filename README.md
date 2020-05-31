# m3u8-Downloader
Download m3u8 to ts with multithreading

# Updates
Python3

# How to use
```bash
downloader = Downloader(50)
downloader.run('http://m3u8.test.com/test.m3u8', '/home/video/')
```

# How to use with multiple files
```bash
# start.py
run_from_file('/home/data.txt', '/home/download/', 1)
```
