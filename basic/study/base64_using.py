
import base64

with open("D:/图片/科幻壁纸/4.jpg","rb") as f:#转为二进制格式
    base64_data =base64.b64encode(f.read())#使用base64进行加密
    print(base64_data)
    file=open('result.html','wt')#写成文本格式
    file.write('<img src="data:image/jpg;base64,'+str(base64_data.decode())+'"/>')
    file.close()
