from moonmask.custom_image import CustomImage 
from moonmask.res.constants import *
from datetime import datetime, timezone, timedelta

class MoonImage(CustomImage):
    def __init__(self, size, kw):
        self.size = size
        self.url = ""
        self.frame_id = ""
        self.key = kw
        super()
        return

    def __str__(self):
        return self.key

    def set_moon_image(self, relative_date="today", date=None, filename=None):
        """Sets the image that will be used as a mask on the image

        Keyword arguments:
        date -- the date in format YYYYMMDD
        relative_date -- defaults to "today". Other accepted options are "yesterday" and "tomorrow"
        """

        #if more than one of these parameters are provided, raise an error.
        #TODO check for a cleaner way to do this
        self.url = ""

        if (filename == None):
            if (date):
                self.datetime = datetime.strptime(date, '%Y-%m-%d').replace(tzinfo=timezone.utc)
            elif (relative_date.lower() == "today"):
                self.datetime = datetime.now(timezone.utc)
            elif (relative_date.lower() == "tomorrow"):
                self.datetime = datetime.now(timezone.utc) + timedelta(days=1)
            elif (relative_date.lower() == "yesterday"):
                self.datetime = datetime.now(timezone.utc) + timedelta(days=-1)
            self.frame_id = self.get_nasa_frame_id(date)
            self.url = self.get_moon_url(date)

        self.set_image(url=self.url, filename=filename)
        return

    def get_nasa_frame_id(self, date):
        #code logic courtesy of Ernie Wright
        year = self.datetime.year
        if (year != 2019):
            moon_imagenum = 1
        janone = datetime(year, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc );
        moon_imagenum = int(round((self.datetime - janone ).total_seconds() / 3600))
        if (moon_imagenum > 8760):
            moon_imagenum = 8760
        return str(moon_imagenum + 1).zfill(4)

    def get_moon_url(self, date):
        self.nasa_id = NASA_ID["2019"]
        self.url = "https://svs.gsfc.nasa.gov/vis/a000000/a00{year_id_modulo}/a00{year_id}/frames/730x730_1x1_30p/moon.{frame_id}.jpg".format(
            year_id_modulo = str(self.nasa_id - self.nasa_id % 100),
            year_id = str(self.nasa_id),
            frame_id = str(self.frame_id)
        )
        return self.url

    def save_moon(self):
        if (self.datetime and self.image):
            self.image.save("moon-image-" + self.datetime + ".jpg")

    def get_moon_phase_date(self):
        return self.datetime
