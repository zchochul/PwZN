import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from PIL import Image, ImageFilter
import argparse

parser = argparse.ArgumentParser() 
parser.add_argument('-type', '--typ_wykonania', default = 'slow')  

args = parser.parse_args()    

type=str(args.typ_wykonania)


def download_greyscale_gauss(val):
    source = 'http://www.if.pw.edu.pl/~mrow/dyd/wdprir/'        
    req = requests.get(source)  
    status = req.status_code    
    print("Status code = ", status)

    soup = BeautifulSoup(req.text,'html.parser')

    for a in soup.find_all('a', href=True):     
        url =  a['href']
        imag = 'img'+str(val)   

        if imag in url:
            img = requests.get(url=source+url, stream=True).content     

            with open('img/picture'+str(val)+'.png', 'wb') as handler:    
                handler.write(img) 
                im = Image.open('img/picture'+str(val)+'.png')
                im1 = im.convert("L") 
                im2 = im1.filter(ImageFilter.GaussianBlur(radius = 9))  
                im2.save('img/picture_blur'+str(val)+'.png') 
                print('picture created: ' + str(val))

if type=='slow':
    start = time.time()
    for i in range(0, 10):
        download_greyscale_gauss(i)
    stop = time.time() 

    print(f'Po kolei wersja: {stop - start = } s')   


if type=='fast':
    if __name__ == '__main__':
        start = time.time()
        with ProcessPoolExecutor(10) as ex:
            for i in range(0, 10):
                ex.submit(download_greyscale_gauss, i)
        stop = time.time() 

        print(f'Process Pool Execture wersja: {stop - start = } s')  

