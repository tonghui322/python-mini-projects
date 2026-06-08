from PyPDF2 import PdfReader
import pyttsx3
import time

def readPDFContent(pdf_path):
    """读取PDF并清洗文本"""
    content = ""
    try:
        print("正在读取PDF...")
        reader = PdfReader(pdf_path)
        total_page = len(reader.pages)
        print(f"文档总页数：{total_page}")

        for idx, page in enumerate(reader.pages, 1):
            print(f"读取第 {idx} 页")
            page_text = page.extract_text()
            if page_text:
                # 清洗空行、多余空格
                clean_text = " ".join(page_text.split())
                content += clean_text + " "
        print("PDF 读取完成\n")
    except Exception as e:
        print(f"读取PDF失败：{e}")
    return content

def text2Voice(text):
    """分段处理文本，一次性生成语音文件（兼容旧版pyttsx3，无append参数）"""
    if not text.strip():
        print("未提取到有效文本，退出语音合成")
        return

    print("开始生成语音文件...")
    try:
        engine = pyttsx3.init()
        # 语速、音量微调，适配中文
        engine.setProperty('rate', 170)
        engine.setProperty('volume', 1.0)

        # 按短句分段切割文本（降低单次处理压力）
        text_list = text.split(". ")
        # 重新拼接分段后的文本（不多次写入文件，规避append报错）
        combine_text = "。".join(text_list)

        # 一次性保存为wav文件，旧版本标准写法
        engine.save_to_file(combine_text, "audio.wav")
        engine.runAndWait()
        print("✅ 语音文件 audio.wav 生成完毕！")
    except Exception as e:
        print(f"语音生成失败：{e}")

if __name__ == "__main__":
    # 重要建议：Windows下PDF文件名尽量改为纯英文，避免解析异常
    # pdf_file = "test.pdf"  # 推荐使用英文文件名
    pdf_file = "论大数据Lambda架构.pdf"
    pdf_text = readPDFContent(pdf_file)
    text2Voice(pdf_text)
    print("程序执行结束")