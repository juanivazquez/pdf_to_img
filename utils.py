import os
import shutil
import fitz



def pdf_to_img_pdf(pdf):
    '''
    f(x): it takes a pdf and creates a new pdf out of images of it.
    in  : pdf file path
    out : new pdf made of png images
    '''
    # 1° creates folder with imgs:
    file_name = pdf_to_imgs("input.pdf",save=True)
    
    # 2° create files:
    imgs_to_pdf(file_name)
    
    # 3° remove_all:
    delete_folder('temp')
    


def pdf_to_imgs(pdf_file,save=True):
    '''
    f(x): it creates a temp folder with png images from the original pdf and provides a file_name for the final pdf
    in  : pdf file path
    out : file_name 
    '''
    doc = fitz.open(pdf_file)
    zoom = 4
    mat = fitz.Matrix(zoom, zoom)
    count = 0

    folder_name = 'temp'
    os.makedirs(folder_name, exist_ok=True)
    
    for p in doc:
        count += 1
    for i in range(count):
        val = os.path.join(folder_name,f"image_{i+1000000}.png")
        page = doc.load_page(i)
        pix = page.get_pixmap(matrix=mat)
        pix.save(val)    
    doc.close()
    print('Images saved to temp')
    
    return pdf_file.replace('.pdf','')
 
def imgs_to_pdf(file_name, save = True):
    doc = fitz.open() 
    imglist = os.listdir('temp')  
    imglist = [f for f in imglist if f.endswith('.png')]  # Check for PNG files
    imgcount = len(imglist)  
    
    for i, f in enumerate(imglist):
        img = fitz.open(os.path.join('temp', f)) 
        rect = img[0].rect  
        pdfbytes = img.convert_to_pdf() 
        img.close() 
        imgPDF = fitz.open("pdf", pdfbytes)  
        page = doc.new_page(width = rect.width, height = rect.height) 
        page.show_pdf_page(rect, imgPDF, 0)  

    if save:
        new_pdf_name = file_name + '_img.pdf'
        c = 1
        while os.path.exists(new_pdf_name):
            new_pdf_name = file_name + f'_img_{c}.pdf'
            c += 1
        doc.save(new_pdf_name)
        print(f"{new_pdf_name} created successfully")
    return doc   

def delete_folder(folder_path):
    '''
    f(x): Deletes a folder and all its contents.
    in  : folder_path (str) - Path of the folder to be deleted.
    '''
    # Delete the folder and all its contents
    try:
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' and its contents deleted.")
    except:
        print(f"{folder_path} not deleted")
