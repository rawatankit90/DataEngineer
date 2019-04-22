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

1.) Postgres database
2.) Python 3.6 with panda library
3.) Jupyter Notebooks - optional for practive

## Programming languages

1.) SQL
2.) Python
3.) JSON

## DataSet

1.) Song Dataset
    The first dataset is a subset of real data from the Million Song Dataset. Each file is in 
    JSON format and contains metadata about a song and the artist of that song.
    
2.) Log Dataset
    The  dataset consists of log files in JSON format generated by this event simulator based on
    the songs in the dataset above. These simulate app activity logs from a music streaming app 
    based on specified  configurations.

## How to run from Udacity Workspace

1.) Run database_setup.ipynb Jupyter notebook
2.) Run etl_process.ipynb Jupyter notebook


## How to run from local

1.) Install Python 3.6 with pandas library.  
2.) Install Postgres 10 database
3.) Create student user in Postgres database from postgres
4.) Create studentdb database Postgres database from postgres
5.) Download the sql_queries.py, create_tables.py, etl.py files in a single directory along with data
    folder.
6.) Run create_tables.py
7.) Run etl.py
8.) Validate the tables `songplays`, `users`, `songs`, `artists`, `time` for data inserted from
    JSON files present