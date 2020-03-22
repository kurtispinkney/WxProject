import datetime
import os
import re


endpoint = os.environ.get('ENDPOINT')
port = os.environ.get('PORT')
dbuser = os.environ.get('DBUSER')
password = os.environ.get('DBPASSWORD')
database = os.environ.get('DATABASE')

def make_connection():


def extract_radar_info(s3_file):
    """
    Extracts information from NEXRAD files being passed to this function via
    SNS.

    :param s3_file: S3 file retrieved from SNS message sent from S3 bucket.
    :return:
    """

    event_datetime = re.match(
        r"(?P<file_datetime>\d{8}_\d{6})", s3_file).group("file_datetime")

    event_datetime_obj = datetime.datetime.strptime(
        event_datetime, "%Y%m%d_%H%M%S")


def handler(event, context):
    """
    Extracts information from NEXRAD files being passed to this function via
    SNS.

    :param event: Information related to SNS event passed to the function
    :param context: Provides information related to invocation, function, and
    execution environment.
    :return:
    """
    s3_event = event["Records"][0]["Sns"]["Message"]["Records"][0]["s3"]["key"]

