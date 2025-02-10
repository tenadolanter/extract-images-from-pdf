from pdf2image import convert_from_path
import os

def pdf_to_images_in_single_folder(pdf_path, output_folder, dpi=200):
    """
    将单个 PDF 的每一页转换为图片并保存到统一的输出文件夹中。
    :param pdf_path: PDF 文件路径
    :param output_folder: 输出图片的统一文件夹
    :param dpi: 转换图片的分辨率（默认 200）
    """
    os.makedirs(output_folder, exist_ok=True)

    print(f"正在处理 PDF 文件：{pdf_path}")
    try:
        # 将 PDF 转换为图片列表
        images = convert_from_path(pdf_path, dpi=dpi)

        for page_number, image in enumerate(images, start=1):
            # 构造统一的输出图片路径，包含 PDF 文件名和页码
            pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
            image_filename = f"{pdf_name}_page_{page_number}.jpg"
            image_path = os.path.join(output_folder, image_filename)

            # 保存图片
            image.save(image_path, "JPEG")
            print(f"已保存图片：{image_path}")

    except Exception as e:
        print(f"处理文件 {pdf_path} 时出错：{e}")

def batch_convert_pdf_to_images_in_single_folder(input_folder, output_folder, dpi=200):
    """
    批量将文件夹中的所有 PDF 转换为图片，并统一保存到一个文件夹中。
    :param input_folder: 包含 PDF 文件的文件夹
    :param output_folder: 图片保存的统一文件夹
    :param dpi: 转换图片的分辨率（默认 200）
    """
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(".pdf"):  # 检查是否是 PDF 文件
                pdf_path = os.path.join(root, file)
                pdf_to_images_in_single_folder(pdf_path, output_folder, dpi=dpi)

# 示例调用
input_folder = "pdf_folder"  # 包含多个 PDF 文件的文件夹
output_folder = "all_images"  # 所有图片的统一输出文件夹
batch_convert_pdf_to_images_in_single_folder(input_folder, output_folder)
