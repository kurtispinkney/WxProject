import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """ 
        CREATE TABLE radars (
            radar_id varchar PRIMARY KEY,
            lat float NOT NULL,
            lon float NOT NULL
        )
        """,
        """
        CREATE TABLE nexrad_data (
            filename varchar PRIMARY KEY,
            s3_object varchar NOT NULL,
            radar_id varchar NOT NULL,
            year int NOT NULL,
            month int NOT NULL,
            day int NOT NULL,
            hour int NOT NULL,
            min int NOT NULL,
            second int NOT NULL,
            FOREIGN KEY (radar_id)
            REFERENCES radars (radar_id)
            ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """ 
        CREATE TABLE lightning_data (
            filename varchar PRIMARY KEY,
            s3_object varchar NOT NULL
        )
        """,
        """
        CREATE TABLE flashes (
            id SERIAL PRIMARY KEY,
            flash_id int NOT NULL,
            data_id varchar NOT NULL,
            lat float NOT NULL,
            lon float NOT NULL,
            area float NOT NULL,
            energy float NOT NULL,
            quality_flag int NOT NULL,
            FOREIGN KEY (data_id)
                REFERENCES lightning_data (filename)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
    )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
