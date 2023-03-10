# Import required libraries
import snowflake.connector as sf

# Connect to Snowflake
conn = sf.connect(
    user='kanakat',
    password='Kanaka@123',
    account='gabxoij-kyb59240',
    warehouse='COMPUTE_WH',
    database='MY_DB',
    schema='MY_SCHEMA'
)

# Execute SQL statement and perform data transformation
result = ''
cursor = conn.cursor()
cursor.execute("INSERT INTO  MY_TABLE(name,age,add) values('Kanakamma',32,'Bangalore');")
rows = cursor.fetchall()

print(rows)

cursor.close()
conn.close()
