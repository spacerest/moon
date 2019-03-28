from moonmask.custom_instagram_api import CustomInstagramAPI
import requests
from io import BytesIO
from moonmask.res.constants import *
import pickle

class InstagramWrapper():

    def __init__(self, username, password, save_session=False):
        try:
            self.recover_saved_session(username, password)
        except:
            print("using a new instagram session")
            self.ig = CustomInstagramAPI(username, password)

        self.ig.login()
        self.ig.generateDeviceId("0")
        if save_session:
            try:
                with open(SESSIONS_PATH, 'wb') as fp:
                    pickle.dump(self.ig, fp)
                fp.close()
            except:
                raise Exception("Not able to dump current session into " + SESSIONS_PATH)

    def recover_saved_session(self, username, password):
        print("recovering saved session...")
        with open(SESSIONS_PATH, 'rb') as fp:
            self.ig = pickle.load(fp)
            fp.close()

    def post_image(self, image_path, caption, usertags=USERTAGS, test=False):
        self.ig.login()
        self.ig.generateDeviceId("0")
        photo_path = image_path
        self.ig.uploadPhoto(image_path, caption=caption, usertags=USERTAGS)

    def get_image_info(self, post_url):
        self.ig.login()
        info = {}
        info['media_id'] = self.get_media_id(post_url)
        media_info = self.ig.LastJson
        info['url'] = media_info['items'][0]['image_versions2']['candidates'][0]['url']
        info['username'] = media_info['items'][0]['user']['username']
        info['user_id'] = media_info['items'][0]['user']['pk']
        return info

    def get_media_id(self, url):
        req = requests.get('https://api.instagram.com/oembed/?url={}'.format(url))
        media_id = req.json()['media_id']
        return media_id

    def get_username(self, media_id):
        if not media_id:
            return None
        self.ig.login()
        self.ig.mediaInfo(media_id)
        return self.ig.LastJson['items'][0]['user']['username']
