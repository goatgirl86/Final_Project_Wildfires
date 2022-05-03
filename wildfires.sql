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
    State DATE NOT NULL,
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
              
