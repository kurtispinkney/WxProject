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


def make_connection() -> psycopg2.extensions.connection:

    conn_str = f"host={endpoint} dbname={database} user={dbuser}" \
               f" password={password} port={port}"
    conn = psycopg2.connect(conn_str)
    conn.autocommit = True

    return conn


def _scrape_date_info(s3_key: str) -> datetime.datetime:
    """
    Helper function that searches for regex date/time pattern in key filename
    and returns a datetime object using the matched string.

    :param s3_key: S3 bucket key associated with SNS message.
    :return: Datetime object created from key filename date/time string.
    """

    event_datetime = re.search(
        r"(?P<file_datetime>\d{8}_\d{6})_V06", s3_key)

    if event_datetime:
        return datetime.datetime.strptime(
            event_datetime.group("file_datetime"), "%Y%m%d_%H%M%S")
    else:
        raise ValueError("File with unexpected date/time format received.")


def extract_radar_info(s3_event: dict) -> tuple:
    """
    Extracts bucket and filename information from S3 event associated with SNS
    message.

    :param s3_event: S3 event retrieved from SNS message sent from S3 bucket.
    :return: Dictionary containing s3_key, s3_bucket, radar_id,
    year, month, day, hour, min, sec key/value
    pairs.
    """

    s3_key = s3_event["object"]["key"]
    event_datetime_obj = _scrape_date_info(s3_key)

    s3_bucket = s3_event["bucket"]["name"]

    radar_id = re.search(r"/(?P<radar_id>\D{4})/", s3_key).group("radar_id")

    return (s3_key,
            s3_bucket,
            radar_id,
            event_datetime_obj.year,
            event_datetime_obj.month,
            event_datetime_obj.day,
            event_datetime_obj.hour,
            event_datetime_obj.minute,
            event_datetime_obj.second)


def handler(event: dict, context: dict):
    """
    Extracts relevant information from SNS message and inserts into a database.

    :param event: SNS event passed to the function
    :param context: Provides information related to invocation, function, and
    execution environment.
    """

    s3_event = event["Records"][0]["Sns"]["Message"]["Records"][0]["s3"]

    insert_records = extract_radar_info(s3_event)

    try:
        conn = make_connection()
        cur = conn.cursor()
        try:
            cur.execute(query, insert_records)
        except (Exception, psycopg2.DatabaseError) as e:
            raise RuntimeError(f"Couldn't execute query: {query} because of "
                               f"error {e}.")
    except psycopg2.Error as e:
        raise(f"There was an error {e} while attempting to connect to database"
              f" {database}.")
    finally:
        conn.close()


# if __name__ == "__main__":
#     handler(None, None)
