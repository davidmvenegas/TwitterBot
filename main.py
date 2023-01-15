import pip._vendor.requests as requests
import tweepy

twitter_api_key = "K3sDjWRTgZWIYAvb2dBKsn1xm"
twitter_api_key_secret = "oak5WmF2KUT82W2rWn4swdOiCy39IfhyqU0Mhv4JUN2gylu1fg"
twitter_bearer_token = "AAAAAAAAAAAAAAAAAAAAAJTplAEAAAAAz3jQP2VVkt26YMxqA1UvyK%2FHhxw%3DS4xAlGv8VTIgjhauofaTwJMcBPKs7NGSbluIvjPkpRygvtJFDz"

twitter_access_token = "1614455148125749250-yaiyhsYENkqgsK7l6ZgMjjogOwjXyl"
twitter_access_token_secret = "o9hHpOgWmYsGO90TX9U92JtWf4ynntwRFGsjbvi4NLzEz"

images_request = requests.get('https://dalle2.gallery/api/images/aggregated?pagesize=20&page=0&random=true', verify=False)
images_as_json = images_request.json()
image_with_link = next(item for item in images_as_json if item['Caption'] is not None and item['PromptImagePath'] is not None)

def api():
    # auth = 
    print('Yo')

print(image_with_link)
