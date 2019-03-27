import moonmask.custom_image
from moonmask.constants import *
from datetime import datetime, timezone, timedelta

class MoonImage(custom_image.CustomImage):
    def __init__(self, size):
        self.size = size
        super()
        return

    def set_moon_image(self, relative_date="today", date=None, filename=None):
        """Sets the image that will be used as a mask on the image

        Keyword arguments:
        date -- the date in format YYYYMMDD
        relative_date -- defaults to "today". Other accepted options are "yesterday" and "tomorrow"
        """

        #if more than one of these parameters are provided, raise an error.
        #TODO check for a cleaner way to do this
        url = ""

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
            url = self.get_moon_url(date)

        self.image = self.set_image(url=url, filename=filename)
        return self.image

    def get_nasa_frame_id(self, date):
        #code logic courtesy of Ernie Wright
        year = self.datetime.year
        if (year != 2019):
            moon_imagenum = 1
        janone = datetime(year, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc );
        moon_imagenum = int(round((self.datetime - janone ).total_seconds() / 3600))
        if (moon_imagenum > 8760):
            moon_imagenum = 8760
        return str(moon_imagenum).zfill(4)

    def get_moon_url(self, date):
        self.nasa_id = NASA_ID["2019"]
        url = "https://svs.gsfc.nasa.gov/vis/a000000/a00{year_id_modulo}/a00{year_id}/frames/730x730_1x1_30p/moon.{frame_id}.jpg".format(
            year_id_modulo = str(self.nasa_id - self.nasa_id % 100),
            year_id = str(self.nasa_id),
            frame_id = str(self.frame_id)
        )
        return url

    def save_moon(self):
        if (self.datetime and self.image):
            self.image.save("moon-image-" + self.datetime + ".jpg")
