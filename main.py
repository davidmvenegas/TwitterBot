import pip._vendor.requests as requests
import shutil
import tweepy


def get_caption_and_image():
    while True:
        images_request = requests.get('https://dalle2.gallery/api/images/aggregated?pagesize=20&page=0&random=true', verify=False)
        images_as_json = images_request.json()

        for image in images_as_json:
            if image['Caption'] is not None and image['PromptImagePath'] is not None:
                image_caption = image['Caption']
                image_URL = image['PromptImagePath']

                return image_caption, image_URL


def download_image(image_url):
    filename = "pic.webp"
    r = requests.get(image_url, stream=True)

    if r.status_code == 200:
        r.raw.decode_content = True

        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image successfully Downloaded')
    else:
        print('Image Couldn\'t be retrieved')


def api():
    auth = tweepy.OAuthHandler("K3sDjWRTgZWIYAvb2dBKsn1xm", "oak5WmF2KUT82W2rWn4swdOiCy39IfhyqU0Mhv4JUN2gylu1fg")
    auth.set_access_token("1614455148125749250-yaiyhsYENkqgsK7l6ZgMjjogOwjXyl", "o9hHpOgWmYsGO90TX9U92JtWf4ynntwRFGsjbvi4NLzEz")
    return tweepy.API(auth)


def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print('Tweeted successfully!')


def run_bot():
    image_caption, image_URL = get_caption_and_image()
    download_image(image_URL)
    tweet(api(), image_caption, 'pic.webp')


if __name__ == "__main__":
    run_bot()
