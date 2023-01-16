import requests
import tweepy
import shutil
from PIL import Image


def main():

    def get_caption_and_image():
        while True:
            images_request = requests.get('https://dalle2.gallery/api/images/aggregated?pagesize=20&page=0&random=true', verify=False)
            images_as_json = images_request.json()

            for image in images_as_json:
                if image['Caption'] is not None and image['PromptImagePath'] is not None:
                    image_caption = image['Caption']
                    image_URL = image['PromptImagePath']

                    if (is_not_transparent(image_URL)):
                        return image_caption


    def is_not_transparent(image_URL):
        r = requests.get(image_URL, stream=True)

        if r.status_code == 200:
            r.raw.decode_content = True

            with open('tmp/pic.webp', 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            print('Image successfully Downloaded')

            img = Image.open('tmp/pic.webp')

            if img.info.get("transparency", None) is not None:
                return False
            if img.mode == "P":
                transparent = img.info.get("transparency", -1)
                for _, index in img.getcolors():
                    if index == transparent:
                        return False
            elif img.mode == "RGBA":
                extrema = img.getextrema()
                if extrema[3][0] < 255:
                    return False
            return True

        else:
            print('Image Couldn\'t be retrieved')


    def api():
        auth = tweepy.OAuthHandler("K3sDjWRTgZWIYAvb2dBKsn1xm", "oak5WmF2KUT82W2rWn4swdOiCy39IfhyqU0Mhv4JUN2gylu1fg")
        auth.set_access_token("1614455148125749250-yaiyhsYENkqgsK7l6ZgMjjogOwjXyl","o9hHpOgWmYsGO90TX9U92JtWf4ynntwRFGsjbvi4NLzEz")
        return tweepy.API(auth)


    def tweet(api: tweepy.API, message: str, image_path=None):
        if image_path:
            api.update_status_with_media(message, image_path)
        else:
            api.update_status(message)

        print('Tweeted successfully!')


    image_caption = get_caption_and_image()
    tweet(api(), image_caption, 'tmp/pic.webp')

main()