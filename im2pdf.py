from PIL import Image
import os
import sys
 
 
def rea(path, pdf_name):
    file_list = os.listdir(path)
    pic_name = []
    im_list = []
    for x in file_list:
        if "jpg" in x or 'png' in x or 'jpeg' in x:
            if x == 'cover.jpg':
                continue
            pic_name.append(x)
    pic_name.sort()
    # print("hec", pic_name)
 
    im1 = Image.open(os.path.join(path, pic_name[0]))
    pic_name.pop(0)
    for i in pic_name:
        img = Image.open(os.path.join(path, i))
        try:
            img.load()
        except IOError as e:
            continue
        im_list.append(Image.open(os.path.join(path, i)))
        # if img.mode == "RGBA":
        #     img = img.convert('RGB')
        #     im_list.append(img)
        # else:
        #     im_list.append(img)
    im1.save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=im_list)
    print("输出文件名称：", pdf_name)
 
 
if __name__ == '__main__':
    mypath= sys.argv[1]
    pdf_name = sys.argv[2]
    
    if ".pdf" in pdf_name:
        rea(mypath, pdf_name=pdf_name)
    else:
        rea(mypath, pdf_name="{}.pdf".format(pdf_name))