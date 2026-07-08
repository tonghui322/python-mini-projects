#读取websites.txt文件中的网站

def readFile(filePath):
    content = ''
    with open(filePath,'r',encoding='utf-8') as f:
        content = f.read()
    return content

#将文档内容每一行都切分出来，放到数组中
def websiteStrToArr(fileContent):
    arr = fileContent.split('\n')
    print(arr)
    return arr

#判断网站的访问状态


if __name__ == "__main__":
    websiteStr = readFile("./websites.txt")
    websiteStrArr = websiteStrToArr(websiteStr)