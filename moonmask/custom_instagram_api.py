from InstagramAPI import InstagramAPI
import time
from requests_toolbelt import MultipartEncoder
import json
from PIL import Image

class CustomInstagramAPI(InstagramAPI):

    def __init__(self, *args, **kwargs):
        print("hi, initting custom instagram api")
        super().__init__(*args, **kwargs)

    def configure(self, upload_id, photo, caption='', usertags=[]):
        usertags = {'in': [{'user_id': str(u['user_id']), 'position': u['position']} for u in usertags]}
        usertags = json.dumps(usertags, separators=(',', ':'))
        (w, h) = Image.open(photo).size
        data = json.dumps({'_csrftoken': self.token,
                           'media_folder': 'Instagram',
                           'source_type': 4,
                           '_uid': self.username_id,
                           '_uuid': self.uuid,
                           'caption': caption,
                           'upload_id': upload_id,
                           'device': self.DEVICE_SETTINTS,
                           'usertags': usertags,
                           'edits': {
                               'crop_original_size': [w * 1.0, h * 1.0],
                               'crop_center': [0.0, 0.0],
                               'crop_zoom': 1.0
                           },
                           'extra': {
                               'source_width': w,
                               'source_height': h
                           }})
        return self.SendRequest('media/configure/?', self.generateSignature(data))

    def uploadPhoto(self, photo, caption=None, upload_id=None, is_sidecar=None, usertags=[]):
        """
        Uploads a single photo
        Args:
            photo
            caption (optional)
            upload_id (optional)
            is_sidecar (optional)
            usertags (optional)
                needs to be a list of dicts like:
                    [{"user_id": 123456789, "position": [x, y]},
                     ....
                    ]
                where each item represents a usertag and x, y are floats between 0.0 and 1.0
        """
        if upload_id is None:
            upload_id = str(int(time.time() * 1000))
        data = {'upload_id': upload_id,
                '_uuid': self.uuid,
                '_csrftoken': self.token,
                'image_compression': '{"lib_name":"jt","lib_version":"1.3.0","quality":"87"}',
                'photo': ('pending_media_%s.jpg' % upload_id, open(photo, 'rb'), 'application/octet-stream', {'Content-Transfer-Encoding': 'binary'})}
        if is_sidecar:
            data['is_sidecar'] = '1'

        # If usertags are provided, verify that the entries are valid.
        if usertags:
            self.throwIfInvalidUsertags(usertags)

        m = MultipartEncoder(data, boundary=self.uuid)
        self.s.headers.update({'X-IG-Capabilities': '3Q4=',
                               'X-IG-Connection-Type': 'WIFI',
                               'Cookie2': '$Version=1',
                               'Accept-Language': 'en-US',
                               'Accept-Encoding': 'gzip, deflate',
                               'Content-type': m.content_type,
                               'Connection': 'close',
                               'User-Agent': self.USER_AGENT})
        response = self.s.post(self.API_URL + "upload/photo/", data=m.to_string())
        if response.status_code == 200:
            if self.configure(upload_id, photo, caption, usertags):
                self.expose()
        return False

    def throwIfInvalidUsertags(self, usertags):
        for user_position in usertags:
            # Verify this usertag entry, ensuring that the entry is format
            # ['position'=>[0.0,1.0],'user_id'=>'123'] and nothing else.
            correct = True
            if isinstance(user_position, dict):
                position = user_position.get('position', None)
                user_id = user_position.get('user_id', None)

                if isinstance(position, list) and len(position) == 2:
                    try:
                        x = float(position[0])
                        y = float(position[1])
                        if x < 0.0 or x > 1.0:
                            correct = False
                        if y < 0.0 or y > 1.0:
                            correct = False
                    except:
                        correct = False
                try:
                    user_id = int(user_id)
                    if user_id < 0:
                        correct = False
                except:
                    correct = False
            if not correct:
                raise Exception('Invalid user entry in usertags array.')
