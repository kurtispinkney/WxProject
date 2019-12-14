import boto3

s3client = boto3.client('s3', region_name="us-east-1")
result = s3client.list_objects(Bucket="noaa-nexrad-level2", Delimiter="/", Prefix="2019/12/10/")

s3_radar_id = []
for o in result.get('CommonPrefixes'):
    s3_radar_id.append(o.get('Prefix').split("/")[-2])

radar_files_to_dl = []
for radar_id in s3_radar_id:
    prefix = f"2019/12/10/{radar_id}/{radar_id}"
    radar_files = s3client.list_objects(Bucket="noaa-nexrad-level2", Delimiter="/", Prefix=prefix)
    radar_files_to_dl.append(radar_files["Contents"][0]["Key"])

s3 = boto3.resource('s3')
# s3.meta.client.download_file('noaa-nexrad-level2', 'hello.txt', '/tmp/hello.txt')
for radar_file in radar_files_to_dl:
    s3.meta.client.download_file('noaa-nexrad-level2', radar_file, f"radar_data/{radar_file.split('/')[-1]}")

    # s3client.get_object(Bucket="noaa-nexrad-level2", Key=radar_file)
