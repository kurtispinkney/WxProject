import boto3
import glob
import pandas as pd
import pyart
from typing import Iterator

s3client = boto3.client('s3', region_name="us-east-1")
result = s3client.list_objects(
    Bucket="noaa-nexrad-level2", Delimiter="/", Prefix="2019/12/10/")


def yield_radar_ids() -> Iterator[str]:
    for o in result.get('CommonPrefixes'):
        yield o.get('Prefix').split("/")[-2]


def yield_sample_data() -> Iterator[str]:
    for radar_id in yield_radar_ids():
        prefix = f"2019/12/10/{radar_id}/{radar_id}"
        radar_files = s3client.list_objects(
            Bucket="noaa-nexrad-level2", Delimiter="/", Prefix=prefix)
        yield radar_files["Contents"][0]["Key"]


def download_radar_data():
    s3 = boto3.resource('s3')
    for radar_file in yield_sample_data():
        s3.meta.client.download_file(
            'noaa-nexrad-level2',
            radar_file,
            f"radar_datas/{radar_file.split('/')[-1]}")


def get_radar_info():
    radar_name = []
    lat = []
    lon = []
    for nexrad_file in glob.iglob("radar_data/*"):
        nexrad_object = pyart.io.read_nexrad_archive(nexrad_file)
        radar_name.append(nexrad_object.metadata["instrument_name"])
        lat.append(nexrad_object.latitude["data"][0])
        lon.append(nexrad_object.longitude["data"][0])

    return radar_name, lat, lon


def create_radar_csv():
    radar_name, lat, lon = get_radar_info()
    df = pd.DataFrame(
        {'Radar_Id': radar_name,
         'Latitude': lat,
         'Longitude': lon
         })
    df.to_csv("aws_radar_locations.csv", index=False)


# download_radar_data()
create_radar_csv()
