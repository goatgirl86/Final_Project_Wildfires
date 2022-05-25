CREATE TABLE fire_name (
    fire_index INT NOT NULL,
    fire_name VARCHAR(20) NOT NULL,
    PRIMARY KEY (fire_index),
     UNIQUE (fire_name),
    );

CREATE TABLE fire_info (
	fire_index INT NOT NULL,
	fire_size INT NOT NULL,
	fire_cause VARCHAR NOT NULL,
	discovery_month VARCHAR NOT NULL,
	putout_time DATE NOT NULL,
    year INT NOT NULL,
	PRIMARY KEY (fire_index)
);

CREATE TABLE fire_location (
fire_index INT NOT NULL,
    latitude INT NOT NULL,
    longitude INT NOT NULL,
    State varchar NOT NULL,
FOREIGN KEY (fire_index) REFERENCES fire_info (fire_index),
FOREIGN KEY (fire_index) REFERENCES fire_name (fire_name),
    PRIMARY KEY (fire_index)
);

CREATE TABLE weather_data (
fire_index INT NOT NULL,
    Temp_pre_30 INT NOT NULL,
    Wind_pre_30 INT NOT NULL,
    Hum_pre_30 INT NOT NULL,
    Temp_pre_15 INT NOT NULL,
    Wind_pre_15 INT NOT NULL,
    Hum_pre_15 INT NOT NULL,
    Temp_pre_7 INT NOT NULL,
    Wind_pre_7 INT NOT NULL,
    Hum_pre_7 INT NOT NULL,
FOREIGN KEY (fire_index) REFERENCES fire_info (fire_index),
FOREIGN KEY (fire_index) REFERENCES fire_name(fire_index),
    PRIMARY KEY (fire_index)
);
              
-- New tabble 1 joining multiple columns
SELECT fc.fire_id,
    fl.state, 
    fi.discovery_month,
    fi.fire_cause, 
    wd."Temp_pre_30",
    wd."Wind_pre_30",
    wd."Hum_pre_30",
    fi.putout_time, 
    fc.fire_size_bin,
    fc.fire_size_bin_no
INTO wildfire_details_30
FROM fire_category AS fc
    INNER JOIN fire_location AS fl 
        ON (fc.fire_id = fl.fire_id)
    INNER JOIN fire_info AS fi 
        ON (fc.fire_id = fi.fire_id)
    INNER JOIN weather_data AS wd 
        ON (fc.fire_id = wd.fire_id);

-- New table 2 joining multiple columns
SELECT fc.fire_id,
    fl.state, 
    fi.discovery_month,
    fi.fire_cause, 
    wd."Temp_pre_7",
    wd."Wind_pre_7",
    wd."Hum_pre_7",
    fi.putout_time, 
    fc.fire_size_bin,
    fc.fire_size_bin_no
INTO wildfire_details_7
FROM fire_category AS fc
    INNER JOIN fire_location AS fl 
        ON (fc.fire_id = fl.fire_id)
    INNER JOIN fire_info AS fi 
        ON (fc.fire_id = fi.fire_id)
    INNER JOIN weather_data AS wd 
        ON (fc.fire_id = wd.fire_id);