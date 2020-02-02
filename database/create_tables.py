import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE "nexrad_data" (
            filename int PRIMARY KEY,
            s3_object varchar NOT NULL,
            radar_id str NOT NULL,
            year int NOT NULL,
            month int NOT NULL,
            day int NOT NULL,
            hour int NOT NULL,
            min int NOT NULL,
            second int NOT NULL
            FOREIGN KEY (radar_id)
            REFERENCES radars (radar_id)
            ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """ 
        CREATE TABLE "radars" (
          "id" str PRIMARY KEY,
          "lat" float,
          "lon" float
        )
        """,
        """ 
        CREATE TABLE "lightning_data" (
          "filename" str PRIMARY KEY,
          "s3_object" varchar
        )
        """,
        """
        CREATE TABLE "flashes" (
          "id" SERIAL PRIMARY KEY,
          "flash_id" int,
          "data_id" int,
          "storm_id" into,
          "lat" float,
          "lon" float,
          "area" float,
          "energy" float,
          "quality_flag" int
        )
        """,
        """
        CREATE TABLE "storms" (
          "id" SERIAL PRIMARY KEY,
          "storm_id" int,
          "radar_file" str,
          "grid_x" float,
          "grid_y" float,
          "lon" float,
          "lat" float,
          "area" float,
          "volume" float,
          "max_refl" float,
          "max_alt" float,
          "isolated" boolean
        )
        """
        """
        CREATE TABLE part_drawings (
                part_id INTEGER PRIMARY KEY,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE vendor_parts (
                vendor_id INTEGER NOT NULL,
                part_id INTEGER NOT NULL,
                PRIMARY KEY (vendor_id , part_id),
                FOREIGN KEY (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
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