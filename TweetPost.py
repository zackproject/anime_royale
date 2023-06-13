import tweepy
from tweepy import OAuthHandler
from RoyaleKeys import keys
from TextFile import *


def twitter_api():
    auth = OAuthHandler(keys["twitter"]["auth"]["consumer_key"],
                        keys["twitter"]["auth"]["consumer_secret"])
    auth.set_access_token(keys["twitter"]["auth"]["access_token"],
                          keys["twitter"]["auth"]["access_token_secret"])
    #    api = auth
    return tweepy.API(auth)


def tweet_only(message):
    try:
        api = twitter_api()
        api.update_status(message)
        print("Tweeted - {0}".format(message))
    except Exception as e:
        directMessage("ERROR Inicial [{0}]".format(
            str(e)))
        print("ERROR {0}".format(str(e)))


def tweet_multimage():
    #Read the conect from the file
    message = getTextFromFile(keys["path"]["txt_info"])
    #alt_img = "Image Generated with AnimeRoyaleBot"
    filenames = [
        keys["path"]["img_asesino"],
        keys["path"]["img_victima"],
        keys["path"]["img_panel"],
    ]
    try:
        api = twitter_api()
        # Upload images and get media_ids
        media_ids = []
        for filename in filenames:
            res = api.media_upload(filename)
            api.create_media_metadata(res.media_id,"") #, alt_img
            media_ids.append(res.media_id)
        # Tweet with multiple images
        api.update_status(status=message, media_ids=media_ids)
        print("Tweeted royale [3 images + text]")
    except Exception as e:
        directMessage("ERROR [{0}]".format(str(e)))
        print("ERROR [{0}]".format(str(e)))


def directMessage(textMessage=keys["twitter"]["text"]["on_finihed_dm"]):
    api = twitter_api()
    # ID of the recipient Twitter Username number
    recipient_id = keys["twitter"]["auth"]["id_user_dm_error"]
    text = textMessage  # text to be sent
    direct_message = api.send_direct_message(
        recipient_id, text)  # sending the direct message
    # printing the text of the sent direct message
    print(direct_message.message_create["message_data"]["text"])


def tweetWinner(filename, message):
    alt_img = "Image Generated with AnimeRoyaleBot"
    numId = keys["twitter"]["auth"]["id_user_dm_error"]
    api = twitter_api()
    media_ids = []
    try:
        res = api.media_upload(filename)
        # Add alt text on image before upload
        api.create_media_metadata(res.media_id, alt_img)
        media_ids.append(res.media_id)
        api.update_status(media_ids=media_ids, status=message)
    except Exception as e:
        directMessage("ERROR Tweet [{0}]".format(str(e)))
