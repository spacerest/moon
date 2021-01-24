from moon.custom_image import CustomImage 
from moon.res.constants import SVS_ID_DICT, SVS_URL_BASE, SVS_JSON_URL_BASE
from moon.res.en.ui_messages import *
from datetime import datetime, timezone, timedelta
import urllib
import json
from functools import lru_cache

class Moon(CustomImage):
    def __init__(self, size=(1000,1000)):
        self.size = size
        super()
        return

    def __str__(self):
        return datetime.strftime(self.datetime,'%Y%m%d')

    def set_moon_phase(self, date=None):
        try:
            self.set_moon_datetime(date)
            self.request_moon_image()
            self.make_json_year_mooninfo_url()
            self.set_mooninfo_requested_year()
            self.set_mooninfo_requested_date()
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
            self.datetime = self.make_datetime(date, hour)
            self.image = None
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
        
    def make_nasa_frame_id(self):
        #code logic courtesy of Ernie Wright
        year = self.datetime.year

        #todo - check why we were checking that the year isn't 2019
        # if (year != 2019):
        #     moon_imagenum = 1
        janone = datetime(year, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc )
        moon_imagenum = int(round((self.datetime - janone ).total_seconds() / 3600)) + 1

        #todo check why this was in here
        # if (moon_imagenum > 8760):
        #     moon_imagenum = 8760
        return str(moon_imagenum).zfill(4)

    def make_moon_image_url(self):
        try:
            self.svs_id = SVS_ID_DICT[str(self.datetime.year)]
        except Exception as e:
            years_available = sorted(SVS_ID_DICT.keys())
            requested_year = self.datetime.year
            #datetime wasn't found so unset it
            if requested_year not in years_available:
                self.datetime = None
                raise KeyError(NO_SVS_ID_ERROR.format(
                    year=requested_year,
                    year_range_0=years_available[0],
                    year_range_1=years_available [-1]
                    ))
            else:
                raise e

        self.frame_id = self.make_nasa_frame_id()
        return SVS_URL_BASE.format(
            year_id_modulo = str(self.svs_id - self.svs_id % 100),
            year_id = str(self.svs_id),
            frame_id = str(self.frame_id)
        )

    def save(self, prefix="moon-image-"):
        date = datetime.strftime(self.datetime,'%Y%m%d')
        self.save_to_disk(prefix + date)

    def get_moon_phase_date(self):
        return self.datetime

    def make_json_year_mooninfo_url(self):
        self.json_url = SVS_JSON_URL_BASE.format(
            year_id_modulo = str(self.svs_id - self.svs_id % 100),
            year_id = str(self.svs_id),
            frame_id = str(self.frame_id),
            year = self.datetime.year
        )

    @lru_cache
    def set_mooninfo_requested_year(self):
        response = urllib.request.urlopen(self.json_url) 
        self.moon_year_info = json.loads(response.read())
        return self.moon_year_info

    def set_mooninfo_requested_date(self):
        self.moon_datetime_info = self.moon_year_info[int(self.frame_id) - 1]

