import os
import time
import requests
import win32gui
import win32con

# 图片URL
nsmc_list = [
    {
        "id": 1,
        "name": "FY-3D_MERSI_GLOBAL",
        "cn_name": "FY-3D最新全球影像",
        "img_url": "https://img.nsmc.org.cn/CLOUDIMAGE/FY3D/MIPS/FY3D_MERSI_GLOBAL.jpg"
    },
    {
        "id": 2,
        "name": "GEOS_IMAGR_GBAL_L2_MOS_IRX_GLL",
        "cn_name": "静止卫星全球云图最新影像",
        "img_url": "https://img.nsmc.org.cn/CLOUDIMAGE/GEOS/MOS/IRX/PIC/GBAL/GEOS_IMAGR_GBAL_L2_MOS_IRX_GLL_YYYYMMDD_HHmm_10KM_MS.jpg"
    },
    {
        "id": 3,
        "name": "FY4B_DISK_GCLR",
        "cn_name": "FY-4B最新全圆盘真彩色合成图",
        "img_url": "https://img.nsmc.org.cn/CLOUDIMAGE/FY4B/AGRI/GCLR/FY4B_DISK_GCLR.JPG"
    },
    {
        "id": 4,
        "name": "FY4A_DISK",
        "cn_name": "FY-4A最新全圆盘云图",
        "img_url": "https://img.nsmc.org.cn/CLOUDIMAGE/FY4A/MTCC/FY4A_DISK.JPG"
    },
    {
        "id": 5,
        "name": "FY2H_ETV_NOM",
        "cn_name": "FY-2H最新全圆盘云图",
        "img_url": "https://img.nsmc.org.cn/CLOUDIMAGE/FY2H/NOM/FY2H_ETV_NOM.jpg"
    },
    {
        "id": 6,
        "name": "FY4B_REGC_GCLR",
        "cn_name": "FY-4B最新中国区云图",
        "img_url": "https://img.nsmc.org.cn/CLOUDIMAGE/FY4B/AGRI/GCLR/FY4B_REGC_GCLR.JPG"
    },
    {
        "id": 7,
        "name": "FY2H_ETV_SEC_GLB",
        "cn_name": "“一带一路”区域最新云图",
        "img_url": "https://img.nsmc.org.cn/CLOUDIMAGE/FY2H/GLL/FY2H_ETV_SEC_GLB.jpg"
    }
]

# 查找ID为6的条目并获取其img_url值
target_item = next(item for item in nsmc_list if item["id"] == 6)

img_url = target_item['img_url']
temp_img_path = os.path.join(os.getcwd(), 'temp_wallpaper.jpg')  # 使用当前目录作为临时图片存储路径

def download_image(url, path):
    response = requests.get(url)
    with open(path, 'wb') as f:
        f.write(response.content)

def clear_previous_image():
    if os.path.exists(temp_img_path):
        os.remove(temp_img_path)

def set_wallpaper(img_path, style=win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE):
    # 等待完成缓存再替换 定时60s
    time.sleep(60)
    img_path = os.path.abspath(img_path)
    
    # 设置壁纸样式为拉伸（Stretch）
    # 在Windows中，系统默认会尝试拉伸壁纸以适应屏幕大小，通常不需要额外设置
    SPI_SETDESKWALLPAPER = 20
    SPI_SETDESKTOPWALLPAPER = 201  # 也可以使用这个常量，效果相同
    win32gui.SystemParametersInfo(SPI_SETDESKTOPWALLPAPER, img_path, style)

def main():
    while True:
        try:
            clear_previous_image()
            download_image(img_url, temp_img_path)
            set_wallpaper(temp_img_path)
            print(target_item["cn_name"])
            print("壁纸已成功更新至最新图片")
            
        except Exception as e:
            print(f"更换壁纸时发生错误: {e}")

        # 每隔15分钟更换一次壁纸
        time.sleep(900)

if __name__ == "__main__":
    main()
