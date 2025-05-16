from PIL import Image
import os

def create_solid_color_image(color, width, height, filename):
    """生成指定颜色、尺寸的纯色图像并保存"""
    # 创建新图像，模式为RGB
    img = Image.new('RGB', (width, height), color)
    
    # 确保输出目录存在
    os.makedirs('output', exist_ok=True)
    
    # 保存图像
    output_path = os.path.join('output', filename)
    img.save(output_path)
    print(f"已生成图像: {output_path}")
    return output_path

def main():
    # 设置图像尺寸
    width, height = 1920, 1080  # 全高清分辨率
    
    # 生成纯白图像 (255, 255, 255)
    white_image = create_solid_color_image((255, 255, 255), width, height, "pure_white.png")
    
    # 生成纯黑图像 (0, 0, 0)
    black_image = create_solid_color_image((0, 0, 0), width, height, "pure_black.png")
    
    print(f"生成完毕！文件保存在 {os.path.abspath('output')} 目录下")

if __name__ == "__main__":
    main()