from m3u8 import Downloader
import os

def load_file(file_path):
    file = open(file_path, "r")
    lines = file.readlines()
    file.close()
    result = [x.strip() for x in lines]
    return result

def convert_mp4(src_file_path, dest_file):
    ts_file = src_file_path + '/*.ts'
    strings = [ts_file, dest_file]
    cmd = "ffmpeg -i {0}  -map 0 -c copy {1}".format(*strings)
    os.system(cmd)

def run_from_file(data_path, download_path, index_num):
    lines = load_file(data_path)
    for idx, url in enumerate(lines):
        print(url)
        dest_path = download_path + str(idx+index_num)
        downloader = Downloader(50)
        downloader.run(url, dest_path)
        dest_file = download_path + str(idx+index_num) + '.mp4'
        convert_mp4(dest_path, dest_file)


run_from_file('/home/data.txt', '/home/download/', 1)