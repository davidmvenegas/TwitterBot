import pip._vendor.requests as requests
import tweepy

def get_image():
    images_request = requests.get('https://dalle2.gallery/api/images/aggregated?pagesize=20&page=0&random=true', verify=False)
    images_as_json = images_request.json()
    image_with_link = next(item for item in images_as_json if item['Caption'] is not None and item['PromptImagePath'] is not None)

    image_caption = image_with_link['Caption']
    image_URL = image_with_link['PromptImagePath']
    return image_caption, image_URL

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
 

image_caption, image_URL = get_image()

print(image_caption)
print(image_URL)

tweet(api(), 'This is my first tweet as a bot, Hello World')
