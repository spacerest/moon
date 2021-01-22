#ids to access the moon visualizations per year
SVS_ID_DICT = {
    "2021": 4874,
    "2020": 4768,
    "2019": 4442,
    "2018": 4604,
    "2017": 4537,
    "2016": 4404,
    "2015": 4236,
    "2014": 4118,
    "2013": 4000,
    "2012": 3894,
    "2011": 3810,
}

SVS_URL_BASE = "https://svs.gsfc.nasa.gov/vis/a000000/a00{year_id_modulo}/a00{year_id}/frames/730x730_1x1_30p/moon.{frame_id}.jpg"
SVS_JSON_URL_BASE = "https://svs.gsfc.nasa.gov/vis/a000000/a00{year_id_modulo}/a00{year_id}/mooninfo_{year}.json"
