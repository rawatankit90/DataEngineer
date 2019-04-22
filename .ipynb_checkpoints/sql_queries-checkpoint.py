# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = """CREATE TABLE IF NOT EXISTS songplays 
(songplay_id SERIAL, start_time varchar,user_id varchar,level varchar,
song_id varchar,artist_id varchar, session_id varchar, location varchar,
user_agent varchar)"""

user_table_create = """CREATE TABLE IF NOT EXISTS users 
(user_id varchar, first_name varchar, last_name varchar,
 gender varchar,level varchar)"""

song_table_create = """CREATE TABLE IF NOT EXISTS songs 
(song_id varchar,title varchar,artist_id varchar ,year int,duration numeric)"""

artist_table_create = """CREATE TABLE IF NOT EXISTS artists 
(artist_id varchar, name varchar, location varchar, 
lattitude varchar, longitude varchar)"""

time_table_create = """CREATE TABLE IF NOT EXISTS time 
(start_time varchar, hour varchar, day varchar , week varchar,
 month varchar, weekday varchar)"""


# INSERT RECORDS

songplay_table_insert = """INSERT INTO songplays 
(start_time,user_id,level,song_id,artist_id,session_id,location,user_agent) 
values (%s,%s,%s,%s,%s,%s,%s,%s)"""

user_table_insert = """INSERT INTO users(user_id,first_name,last_name,gender,level) 
values (%s,%s,%s,%s,%s)"""

song_table_insert = """INSERT INTO songs(song_id,title,artist_id,year,duration)
values (%s,%s,%s,%s,%s)"""

artist_table_insert = """INSERT INTO artists (artist_id,name,location,lattitude,longitude)
values (%s,%s,%s,%s,%s)"""

time_table_insert = """INSERT INTO time (start_time,hour,day,week,month,weekday)
values (%s,%s,%s,%s,%s,%s)"""

# FIND SONGS

song_select = """SELECT s.song_id,s.artist_id from songs s, artists a 
where s.artist_id=a.artist_id 
and s.song_id=%s and s.artist_id=%s and s.duration=%s"""

# QUERY LISTS

create_table_queries = [songplay_table_create,
                        user_table_create, song_table_create,
                        artist_table_create, time_table_create]
# create_table_queries = [songplay_table_create]
drop_table_queries = [songplay_table_drop,
                      user_table_drop, song_table_drop,
                      artist_table_drop, time_table_drop]