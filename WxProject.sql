CREATE TABLE "nexrad_data" (
  "filename" int PRIMARY KEY,
  "s3_object" varchar,
  "radar_id" str,
  "year" int,
  "month" int,
  "day" int,
  "hour" int,
  "min" int,
  "second" int
);

CREATE TABLE "radars" (
  "id" str PRIMARY KEY,
  "lat" float,
  "lon" float
);

CREATE TABLE "lightning_data" (
  "filename" str PRIMARY KEY,
  "s3_object" varchar
);

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
);

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
);

ALTER TABLE "nexrad_data" ADD FOREIGN KEY ("radar_id") REFERENCES "radars" ("id");

ALTER TABLE "flashes" ADD FOREIGN KEY ("data_id") REFERENCES "lightning_data" ("filename");

ALTER TABLE "flashes" ADD FOREIGN KEY ("storm_id") REFERENCES "storms" ("id");

ALTER TABLE "storms" ADD FOREIGN KEY ("radar_file") REFERENCES "nexrad_data" ("filename");
