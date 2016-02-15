# Define functions that communicate with the SQLite database.

import sqlite3

# SQLite database file:
database_fn = "data/database.db"

def unlock_database():
    """Unlock SQLite database.
    """
    conn = sqlite3.connect(database_fn)
    c = conn.cursor()
    conn.close()

def execute(s):
    """Execute a SQL statement.

    Arguments:
    s (string) -- SQL statement to execute
    """
    conn = sqlite3.connect(database_fn)
    c = conn.cursor()
    c.execute(s)
    conn.commit()
    conn.close()

def execute_parameterized(s, d):
    """Execute a parameterized SQL statement (i.e. includes placeholders).

    Arguments:
    s (string) -- parameterized SQL statement to execute
    d (list or tuple) -- parameters (i.e. data inserted into placeholders)
    """
    conn = sqlite3.connect(database_fn)
    c = conn.cursor()
    c.execute(s, d)
    conn.commit()
    conn.close()

def execute_many_parameterized(s, d):
    """Execute a parameterized SQL statement (i.e. includes placeholders)
    against multiple parameter sequences.

    Arguments:
    s (string) -- parameterized SQL statement to execute
    d (list of tuples) -- parameter sequences (data inserted into placeholders)
    """
    conn = sqlite3.connect(database_fn)
    c = conn.cursor()
    c.executemany(s, d)
    conn.commit()
    conn.close()

def query(s):
    """Submit a SQL query statement and return the result(s).

    Arguments:
    s (string) -- SQL query statement to submit

    Returns:
    (list of tuples) -- SQL query result(s)
    """
    conn = sqlite3.connect(database_fn)
    c = conn.cursor()
    try:
        c.execute(s)
    except sqlite3.OperationalError:
        print 'There is a problem with the following SQL query statement:'
        print s
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

def table_exists(t):
    """Check if a table exists in the SQLite database.

    Arguments:
    t (string) -- name of SQLite database table

    Returns:
    (boolean) -- True (table exists), False (table does not exist)
    """
    q = query("SELECT name FROM sqlite_master " +
              "WHERE type='table' AND name='%s'" % t)
    if len(q) != 0:
        return True
    else:
        return False

def drop_table(t):
    """Drop a table from the SQLite database.

    Arguments:
    t (string) -- name of SQLite database table
    """
    execute("DROP TABLE %s" % t)

def create_ipps_table(t):
    """Create an IPPS table in the SQLite database.

    Arguments:
    t (string) -- name of SQLite database table
    """
    execute("CREATE TABLE %s " % t +
            "(drgDefinition text," +
            "providerId integer," +
            "providerName text," +
            "providerStreetAddress text," +
            "providerCity text," +
            "providerState text," +
            "providerZipCode integer," +
            "hrrDescription text," +
            "totalDischarges integer," +
            "avgCoveredCharges real," +
            "avgTotalPayments real," +
            "avgMedicarePayments real," +
            "avgNonMedicarePayments real," +
            "avgCoveredChargesMinusTotalPayments real)")

def create_state_pop_est_table(t):
    """Create the state population estimate table in the SQLite database.

    Arguments:
    t (string) -- name of SQLite database table
    """
    execute("CREATE TABLE %s " % t +
            "(sumLev text," +
            "region integer," +
            "division integer," +
            "state integer," +
            "name text," +
            "sex integer," +
            "age integer," +
            "estBase2010Civ integer," +
            "popEst2010Civ integer," +
            "popEst2011Civ integer," +
            "popEst2012Civ integer," +
            "popEst2013Civ integer," +
            "popEst2014Civ integer)")

def insert_single_row_into_ipps_table(t, d):
    """Insert a single row of data into an IPPS table.

    Arguments:
    t (string) -- name of SQLite database table
    d (list or tuple) -- single row of data to be inserted
    """
    s = "INSERT INTO %s VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)" % t
    execute_parameterized(s, d)

def insert_multiple_rows_into_ipps_table(t, d):
    """Insert multiple rows of data into an IPPS table.

    Arguments:
    t (string) -- name of SQLite database table
    d (list of tuples) -- multiple row data to be inserted
    """
    s = "INSERT INTO %s VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)" % t
    execute_many_parameterized(s, d)

def insert_multiple_rows_into_state_pop_est_table(t, d):
    """Insert multiple rows of data into the state population estimate table.

    Arguments:
    t (string) -- name of SQLite database table
    d (list of tuples) -- multiple row data to be inserted
    """
    s = "INSERT INTO %s VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)" % t
    execute_many_parameterized(s, d)

def init_ipps_table(t, d):
    """Initialize IPPS tables and insert data.

    Arguments:
    t (string) -- name of SQLite database table
    d (list of tuples) -- multiple row data to be inserted
    """
    create_ipps_table(t)
    insert_multiple_rows_into_ipps_table(t, d)

def init_state_pop_est_table(t, d):
    """Initialize state population estimate table and insert data.

    Arguments:
    t (string) -- name of SQLite database table
    d (list of tuples) -- multiple row data to be inserted
    """
    create_state_pop_est_table(t)
    insert_multiple_rows_into_state_pop_est_table(t, d)

def print_num_rows_in_table(t):
    """Print number of rows in a table.

    Arguments:
    t (string) -- name of SQLite database table
    """
    q = query("SELECT COUNT(*) FROM %s" % t)
    print "Number of rows in '%s' table: %s" % (t, q[0][0])

def print_num_rows_in_all_tables():
    """Print number of rows in all tables.
    """
    print_num_rows_in_table('ipps2011')
    print_num_rows_in_table('ipps2012')
    print_num_rows_in_table('ipps2013')
    print_num_rows_in_table('usdaRestaurants')

def get_list_of_state_abbreviations():
    """Get list of state abbreviations (51 total including DC)

    Returns:
    (list) -- state abbreviations
    """
    states = []
    q = query("SELECT DISTINCT providerState FROM ipps2011")
    for i in range(len(q)):
        states.append(q[i][0])
    return states

