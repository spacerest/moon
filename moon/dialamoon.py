from moon.custom_image import CustomImage 
from moon.res.constants import *
from datetime import datetime, timezone, timedelta
import urllib
import json

class Moon(CustomImage):
    def __init__(self, size=(1000,1000)):
        self.size = size
        self.url = ""
        self.frame_id = ""
        super()
        return

    def __str__(self):
        return datetime.strftime(self.datetime,'%Y%m%d')

    def set_moon_image(self, relative_date="today", date=None):
        """Sets the image that will be used as a mask on the image

        Keyword arguments:
        date -- the date in format YYYYMMDD
        relative_date -- defaults to "today". Other accepted options are "yesterday" and "tomorrow"
        """
        self.set_moon_url()

        self.set_image(url=self.url)
        return

    def determine_datetime(self, relative_date="today", date=None):

        #if more than one of these parameters are provided, raise an error.
        #TODO check for a cleaner way to do this

        if (date):
            self.datetime = datetime.strptime(date, '%Y-%m-%d').replace(tzinfo=timezone.utc)
        elif (relative_date.lower() == "today"):
            self.datetime = datetime.now(timezone.utc)
        elif (relative_date.lower() == "tomorrow"):
            self.datetime = datetime.now(timezone.utc) + timedelta(days=1)
        elif (relative_date.lower() == "yesterday"):
            self.datetime = datetime.now(timezone.utc) + timedelta(days=-1)

    def set_nasa_frame_id(self):
        #code logic courtesy of Ernie Wright
        year = self.datetime.year
        #todo - check why we're checking that the year isn't 2019
        if (year != 2019):
            moon_imagenum = 1
        janone = datetime(year, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc );
        moon_imagenum = int(round((self.datetime - janone ).total_seconds() / 3600))
        if (moon_imagenum > 8760):
            moon_imagenum = 8760
        self.frame_id = str(moon_imagenum + 1).zfill(4)

    def set_moon_url(self):
        self.nasa_id = NASA_ID[str(self.datetime.year)]
        self.url = "https://svs.gsfc.nasa.gov/vis/a000000/a00{year_id_modulo}/a00{year_id}/frames/730x730_1x1_30p/moon.{frame_id}.jpg".format(
            year_id_modulo = str(self.nasa_id - self.nasa_id % 100),
            year_id = str(self.nasa_id),
            frame_id = str(self.frame_id)
        )
        self.url = self.url

    def save(self, prefix="moon-image-"):
        date = datetime.strftime(self.datetime,'%Y%m%d')
        self.save_to_disk(prefix + date)

    def get_moon_phase_date(self):
        return self.datetime

    def set_moon_phase(self, relative_date="today", date=None):
        self.url = ""
        self.determine_datetime(relative_date, date)
        self.set_nasa_frame_id()
 
        self.set_moon_image(date)
        self.set_moon_info(date)

    def set_moon_info(self, date):
        self.json_url = "https://svs.gsfc.nasa.gov/vis/a000000/a00{year_id_modulo}/a00{year_id}/mooninfo_{year}.json".format(
            year_id_modulo = str(self.nasa_id - self.nasa_id % 100),
            year_id = str(self.nasa_id),
            frame_id = str(self.frame_id),
            year = self.datetime.year
        )
        response = urllib.request.urlopen(self.json_url) 
        self.moon_info = json.loads(response.read())[int(self.frame_id)]
