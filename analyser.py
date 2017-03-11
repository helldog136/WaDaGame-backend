import pyimgur
import example


def getResult(image_name):
    upload_image_url = upload_to_imgur(image_name)
    tag = example.main(upload_image_url)
    # need to return tags
    return tag


def upload_to_imgur(image_name):
    CLIENT_ID = "d1ae4f90773e9af"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(image_name, title=image_name)
    print(uploaded_image.link)
    return uploaded_image.link

#upload_to_imgur("../ftl01.jpg")