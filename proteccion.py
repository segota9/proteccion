
import base64
import cv2
import numpy as np
import re
import json

def base64toarray(base64_string):
    # Converts an image in base 64 format and returns it as an array.
    base = re.search(u'base64,(.+)', base64_string).group(1)
    image = base64.b64decode(base)
    pimg = np.frombuffer(image, dtype=np.uint8)
    return np.array(pimg)

def image2base64(image, type_='.jpg'):
    # Converts an image to base 64 format.
    _, im_arr = cv2.imencode(type_, image)
    image_as_text = base64.b64encode(im_arr)
    return "data:image/jpeg;base64," + image_as_text.decode("utf-8")


def resizeimagedummy(body):
    # Image dimension adjustment process.
    try:
        string_base64 = body["image"]
        array_ = base64toarray(string_base64)
        image = cv2.imdecode(array_, flags=cv2.IMREAD_COLOR)
        print('Original Dimensions : ',image.shape)
    
        if (image.shape[0]) > image.shape[1]:
            print ("la orientacion de la imagen es vertical")
            if (image.shape[1]) > 796:
                print ("la imagen se debe ajustar")
                image =verticalresize(image)
        else:
            print ("la orientacion de la imagen es horizontal")
            if (image.shape[1]) > 796:
                print ("la imagen se debe ajustar")
                image= horizontalresize(image)

        res = "ok"
    except :
        res = "not_ok"
        print ("image processing ERROR")
        
    return res, image2base64(image)


def verticalresize(imgv):
    # Adjust dimensions to vertical images
    try:          
        scale_percenth = ((1122*100)/(imgv.shape[0]))
        scale_percentv = ((795*100)/(imgv.shape[1]))

        if scale_percenth < scale_percentv:
            scale_percent = scale_percenth
        else:
            scale_percent = scale_percentv

        print (scale_percent)
        width = int(imgv.shape[1] * scale_percent / 100)
        height = int(imgv.shape[0] * scale_percent / 100)
        dim = (width, height)
                
        resized = cv2.resize(imgv, dim, interpolation = cv2.INTER_AREA)
        print('Resized Dimensions : ',resized.shape)
    
    except:
        print ("Vertical resize ERROR")

    return (resized)


def horizontalresize(imgh):
    # Adjust dimensions to horizontal images
    try:
        scale_percenth = ((795*100)/(imgh.shape[0]))
        scale_percentv = ((1122*100)/(imgh.shape[1]))
        if scale_percenth < scale_percentv:
            scale_percent = scale_percenth
        else:
            scale_percent = scale_percentv

        print (scale_percent)
        width = int(imgh.shape[1] * scale_percent / 100)
        height = int(imgh.shape[0] * scale_percent / 100)
        dim = (width, height)
                
        resized = cv2.resize(imgh, dim, interpolation = cv2.INTER_AREA)
        print('Resized Dimensions : ',resized.shape)

    except:
        print ("Horizontal resize ERROR")
    
    return (resized)

 
def create_response(res, base64_):
    # The image is returned to the client after processing.
    if res == 'ok':
        info_json = json.dumps({"image": base64_, "status": res})
        return info_json
    else:
        info_json = json.dumps({"image": None, "status": res})
        return info_json



# def get_base64(data):
    
#     try:
#         info = data["imagen"]
#     except KeyError:
#         info = None
#     return info