import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    # open song file
    df = pd.read_json(filepath, typ='series') 

    # insert song record
    song_data = df.song_id, df.title, df.artist_id, df.year, df.duration 
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = (df.artist_id, df.artist_name, df.artist_location,
    df.artist_latitude, df.artist_longitude)
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    # open log file
    df = pd.read_json(filepath, lines=True) 

    # filter by NextSong action
    is_NextSong = df['page'] == 'NextSong'
    df = df[is_NextSong]
    
    # convert timestamp column to datetime
    df['ts'] = pd.to_datetime(df['ts'], unit='ms')
    
    # convert timestamp column to datetime
    timestamp = df['ts'].dt.time
    
    # Extract the timestamp, hour, day, week of year, month, year,
    # and weekday from the ts column and set time_data to a list
    # containing these values in order
    hour = df['ts'].dt.hour
    day = df['ts'].dt.day
    week = df['ts'].dt.week
    year = df['ts'].dt.year
    weekday = df['ts'].dt.weekday 
 
    # insert time data records by creating dictionary
    time_data = (timestamp, hour, day, week, year, weekday)
    column_labels = ["lbl_timestamp", "lbl_hour", "lbl_day", "lbl_week",
                     "lbl_year", "lbl_weekday"]
    dictionary = {column_labels[0]: timestamp, column_labels[1]: hour,
                  column_labels[2]: day, column_labels[3]: week,
                  column_labels[4]: year, column_labels[5]: weekday}
    time_df = pd.DataFrame.from_dict(dictionary)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table by extracting data from DataFrame
    userId = df['userId']
    firstName = df['firstName']
    lastName = df['lastName']
    gender = df['gender']
    level = df['level']
    column_labels = ["lbl_userId", "lbl_firstName", "lbl_day",
                    "lbl_lastName", "lbl_gender", "lbl_level"]
    dictionary = {column_labels[0]: userId, column_labels[1]: firstName, 
                  column_labels[2]: lastName, column_labels[3]: gender, 
                  column_labels[4]: level}
    user_df = pd.DataFrame.from_dict(dictionary)

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.ts, row.userId, row.level, songid, artistid,
                         row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)
        

def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student \
                            password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
