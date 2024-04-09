create_pinterest_query = "CREATE table pinterest_data(index integer NOT NULL,\
unique_id varchar(100),title varchar(50),description varchar(100),poster_name varchar(50),\
follower_count varchar(50),tag_list varchar(100),is_image_or_video varchar(100),\
image_src varchar(100),downloaded  integer ,save_location varchar(100),\
category varchar(50))"

# print(create_pinterest_query)
find_all_tables = "select * from information_schema.tables where table_schema = 'public'"
create_geolocation_data_query = "Create table geolocation_data( ind integer NOT NULL,timestamp TIMESTAMP,latitude varchar(100), longitude varchar(100), country varchar(50))"


create_user_data_query = "CREATE TABLE user_data (ind INTEGER, first_name varchar(50), last_name varchar(50), age INTEGER, date_joined TIMESTAMP)"
insert_data_into_pinterest_data = "INSERT INTO pinterest_data values(70,'travel','title_value','description','postername','10k','tag','imgae',100,1,'https','wander')"
insert_data_into_geolocation_data = "INSERT INTO pinterest_data values()"
insert_data_into_user_data = "INSERT INTO pinterest_data values()"
