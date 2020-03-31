import datetime
import psycopg2
import os
import re


endpoint = os.environ.get('ENDPOINT')
port = os.environ.get('PORT')
dbuser = os.environ.get('DBUSER')
password = os.environ.get('DBPASSWORD')
database = os.environ.get('DATABASE')

query = "INSERT INTO nexrad_data" \
        "(filename, s3_object, radar_id, year, month, day, hour, min, second)"\
        "VALUES (%s %s %s %s %s %s %s %s %s)"


def make_connection():

    conn_str = f"host={endpoint} dbname={database} user={dbuser}" \
               f" password={password} port={port}"
    conn = psycopg2.connect(conn_str)
    conn.autocommit = True

    return conn


def extract_radar_info(s3_file):
    """
    Extracts information from NEXRAD files being passed to this function via
    SNS.

    :param s3_file: S3 file retrieved from SNS message sent from S3 bucket.
    :return: Dictionary containing year, month, day, hour, min, sec key/value
    pairs.
    """

    event_datetime = re.match(
        r"(?P<file_datetime>\d{8}_\d{6})", s3_file)

    if event_datetime:
        event_datetime_obj = datetime.datetime.strptime(
            event_datetime.group("file_datetime"), "%Y%m%d_%H%M%S")
    else:
        raise ValueError("File with unexpected date/time format received.")

    return {"year": event_datetime_obj.year,
            "month": event_datetime_obj.month,
            "day": event_datetime_obj.day,
            "hour": event_datetime_obj.hour,
            "min": event_datetime_obj.minute,
            "sec": event_datetime_obj.second}


def handler(event, context):
    """
    Extracts information from NEXRAD files being passed to this function via
    SNS.

    :param event: Information related to SNS event passed to the function
    :param context: Provides information related to invocation, function, and
    execution environment.
    :return:
    """
    s3_event = event["Records"][0]["Sns"]["Message"]["Records"][0]["s3"]["object"]["key"]

    try:
        cnx = make_connection()
        var = "worked"
        print('it worked')
    except psycopg2.Error as e:
        print("you thought")
        var = "failed"

    return {"body": var, "headers": {}, "statusCode": 200,
        "isBase64Encoded":"false"}


# if __name__ == "__main__":
#     handler(None, None)
