import os
import time
import requests
import win32gui
import win32con

# 图片URL
img_url = "https://img.nsmc.org.cn/CLOUDIMAGE/FY4B/AGRI/GCLR/FY4B_REGC_GCLR.JPG"
temp_img_path = os.path.join(os.getcwd(), 'temp_wallpaper.jpg')  # 使用当前目录作为临时图片存储路径

def download_image(url, path):
    response = requests.get(url)
    with open(path, 'wb') as f:
        f.write(response.content)

def clear_previous_image():
    if os.path.exists(temp_img_path):
        os.remove(temp_img_path)

def set_wallpaper(img_path):
    img_path = os.path.abspath(img_path)
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, img_path, 0x00000002)

def main():
    while True:
        try:
            clear_previous_image()
            download_image(img_url, temp_img_path)
            set_wallpaper(temp_img_path)
            print("壁纸已成功更新至最新图片")
        except Exception as e:
            print(f"更换壁纸时发生错误: {e}")

        # 每隔10分钟更换一次壁纸
        time.sleep(600)

if __name__ == "__main__":
    main()
