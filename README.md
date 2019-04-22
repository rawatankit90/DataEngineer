# Sparkify Song Data Analysis

## Problem Statement

Sparkify is an online new music streaming app. They have collected user activity info
and want to do analysis on what songs the users are listening to by doing analytical 
search on the data.As of now the information is store in JSON files and other metadata 
files and there is no easy way to search.

The query that the user wants to run 

## Solution

The solution that is designed to solve the above problem is to build a ETL pipleline by 
extracting the data from JSON files and then transforming it and storing it into a Postgres 
database.

## Software 

*  Postgres database
*  Python 3.6 with panda library
*  Jupyter Notebooks - optional for practive

## Programming languages

*  SQL
*  Python
*  JSON

## DataSet

*  Song Dataset
    The first dataset is a subset of real data from the Million Song Dataset. Each file is in 
    JSON format and contains metadata about a song and the artist of that song.
    
*  Log Dataset
    The  dataset consists of log files in JSON format generated by this event simulator based on
    the songs in the dataset above. These simulate app activity logs from a music streaming app 
    based on specified  configurations.

## How to run from Udacity Workspace  :point_down:

1. Run database_setup.ipynb Jupyter notebook
2. Run etl_process.ipynb Jupyter notebook


## How to run from local  :point_down:

1. Install Python 3.6 with pandas library.  
2. Install Postgres 10 database
3. Create student user in Postgres database from postgres
4. Create studentdb database Postgres database from postgres
5. Download the sql_queries.py, create_tables.py, etl.py files in a single directory along with data
    folder.
6. Run create_tables.py
7. Run etl.py
8. Validate the tables `songplays`, `users`, `songs`, `artists`, `time` for data inserted from
    JSON files present

### A Quick :runner: of the flow  :point_down:

1. Database is designed in Star Schema with Fact and Dimensions table.
2. psycopg2 is utilized to create the tables and insert data into postgres database.
3. Program is designed in a way to first import the dimension data into `songs`, `artist`, `user`, `time` and then
    from these table do the search query to fill the fact table `songplays`.
4. For identifying multiple json files in a directory `os`, `glob` python libraries are used
  To read more on glob https://swcarpentry.github.io/python-novice-inflammation/04-files/


```
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))
 ```
  
 5. For importing and reading json for song records `df = pd.read_json(filepath, typ='series') `
 6. For importing and reading json object per line for log jsons `df = pd.read_json(filepath, lines=True) `
 7. After massaging the data into dataframes from song and log json files, data is inserted into
    database tables by calling sql queries designed in `sql_queries.py` from execute function
    eg. `cur.execute(song_table_insert, song_data)'


