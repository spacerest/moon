from moon.custom_image import CustomImage 
from moon.res.en.ui_messages import *
from datetime import datetime, timezone, timedelta
import urllib, urllib.request, json, sys, pkg_resources
from functools import lru_cache


# Get strings for URLs and IDs this Moon class will need
# https://stackoverflow.com/questions/60687577/trying-to-read-json-file-within-a-python-package
if sys.version_info >= (3, 7):
    import importlib.resources
    with importlib.resources.open_text("moon.res", "constants.json") as file:
        CONSTANTS_JSON_DICT = json.load(file)
else:
    import pkg_resources
    resource_package = __name__
    resource_path = '/'.join(('res', 'constants.json'))
    constants_string = pkg_resources.resource_string(resource_package, resource_path)
    CONSTANTS_JSON_DICT = json.loads(constants_string)

class Moon(CustomImage):
    def __init__(self, size=(730,730), highres=False):
        if not highres:
            self.size = size
        else:
            self.size = (5760,3240)
        self.DIALAMOON_API_BASE_URL = CONSTANTS_JSON_DICT["DIALAMOON_API_BASE_URL"]
        super()
        return

    def __str__(self):
        return requested_datetime.strftime(self.requested_datetime,'%Y%m%d')

    def set_moon_phase(self, date=None, hour=None):
        try:
            self.set_moon_datetime(date, hour)
            self.request_moon_image()
            self.make_mooninfo_url()
            self.set_moon_datetime_info(requested_datetime=self.requested_datetime)
            if self.returned_datetime.year != self.requested_datetime.year:
                raise ValueError(YEAR_MISMATCH_ERROR.format(
                    year_requested=self.requested_datetime.year,
                    year_returned=self.returned_datetime.year))
        except Exception as e:
            raise e
        return True

    def set_moon_datetime(self, date=None, hour=None):
        """
        Keyword arguments:
        date -- UTC date in format YYYY-MM-DD, defaults to current date
        hour -- UTC hours 0 through 23, defaults to current hour
        """
        try:
            self.requested_datetime = self.make_datetime(date, hour)
            self.image = None
            self.make_mooninfo_url()
            self.url = self.make_moon_image_url()
        except Exception as e:
            raise e
        return True

    def request_moon_image(self):
        try:
            self.image = self.set_image(url=self.url)
        except Exception as e:
            raise e
        return True

    def make_datetime(self, date, hour):
        # if hour and hour <= 0 or hour >= 23:
        #     raise ValueError(HOUR_ERROR)
        if hour is None:
            hour = datetime.now(timezone.utc).hour
        
        if date is None:
            date = datetime.now(timezone.utc)
        else:
            date = datetime.strptime(date, '%Y-%m-%d').replace(tzinfo=timezone.utc)
        
        year, month, day = date.year, date.month, date.day
  
        return datetime(year=year, month=month, day=day, hour=hour).replace(tzinfo=timezone.utc)

    def make_moon_image_url(self):
        # "https://svs.gsfc.nasa.gov/api/dialamoon/{year}-{month}-{day}T{hour}:{minute}"
        response = urllib.request.urlopen(self.DIALAMOON_API_BASE_URL.format(
            year = "{:04d}".format(self.requested_datetime.year),
            month = "{:02d}".format(self.requested_datetime.month),
            day = "{:02d}".format(self.requested_datetime.day),
            hour = "{:02d}".format(self.requested_datetime.hour),
            minute = "{:02d}".format(self.requested_datetime.minute)
            ))

        moon_info_json = json.load(response)
        return moon_info_json["image"]["url"]

    def save(self, prefix="moon-image-"):
        date = datetime.strftime(self.requested_datetime,'%Y%m%d')
        self.save_to_disk(prefix + date)

    def get_moon_phase_date(self):
        return self.requested_datetime

    def make_mooninfo_url(self):
        self.url = self.DIALAMOON_API_BASE_URL.format(
            year = "{:04d}".format(self.requested_datetime.year),
            month = "{:02d}".format(self.requested_datetime.month),
            day = "{:02d}".format(self.requested_datetime.day),
            hour = "{:02d}".format(self.requested_datetime.hour),
            minute = "{:02d}".format(self.requested_datetime.minute)
            )

    @lru_cache()
    def set_moon_datetime_info(self, requested_datetime=None):
        self.info = json.load(urllib.request.urlopen(self.url))
        self.returned_datetime = datetime.strptime(self.info["time"], '%Y-%m-%dT%H:%M')




