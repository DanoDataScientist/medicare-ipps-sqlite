# Define functions that communicate with the SQLite database.

import sqlite3

# SQLite database file:
databaseFn = "database.db"

def unlockDatabase():
    """Unlock SQLite database.
    """
    conn = sqlite3.connect(databaseFn)
    c = conn.cursor()
    conn.close()

def dropTable(t):
    """Drop a table from the SQLite database.

    Arguments:
    t (string) -- name of SQLite database table
    """
    conn = sqlite3.connect(databaseFn)
    c = conn.cursor()
    c.execute("DROP TABLE %s" % t)
    conn.commit()
    conn.close()

def createIPPSTable(t):
    """Create an IPPS table in the SQLite database.

    Arguments:
    t (string) -- name of SQLite database table
    """
    conn = sqlite3.connect(databaseFn)
    c = conn.cursor()
    c.execute("CREATE TABLE %s " % t +
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
    conn.commit()
    conn.close()

def createStatePopEstTable(t):
    """Create a state population estimate table in the SQLite database.

    Arguments:
    t (string) -- name of SQLite database table
    """
    conn = sqlite3.connect(databaseFn)
    c = conn.cursor()
    c.execute("CREATE TABLE %s " % t +
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
    conn.commit()
    conn.close()

def createUSDARestaurantsTable(t):
    """Create the USDA restaurants table in the SQLite database.

    Arguments:
    t (string) -- name of SQLite database table
    """
    conn = sqlite3.connect(databaseFn)
    c = conn.cursor()
    c.execute("CREATE TABLE %s " % t +
              "(fips text," +
              "state text," +
              "county text," +
              "ffr07 integer," +
              "ffr12 integer," +
              "pch_ffr_07_12 real," +
              "ffrpth07 real," +
              "ffrpth12 real," +
              "pch_ffrpth_07_12 real," +
              "fsr07 integer," +
              "fsr12 integer," +
              "pch_fsr_07_12 real," +
              "fsrpth07 real," +
              "fsrpth12 real," +
              "pch_fsrpth_07_12 real," +
              "pc_ffrsales02 real," +
              "pc_ffrsales07 real," +
              "pc_fsrsales02 real," +
              "pc_fsrsales07 real)")
    conn.commit()
    conn.close()

def insertSingleRowIntoIPPSTable(t, d):
    """Insert a single row of data into an IPPS table.

    Arguments:
    t (string) -- name of SQLite database table
    d (tuple) -- tuple of row data to be inserted
    """
    conn = sqlite3.connect(databaseFn)
    c = conn.cursor()
    sqlString = "INSERT INTO %s VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)" % t
    c.execute(sqlString, d)
    conn.commit()
    conn.close()

def insertMultipleRowsIntoIPPSTable(t, d):
    """Insert multiple rows of data into an IPPS table.

    Arguments:
    t (string) -- name of SQLite database table
    d (tuple) -- tuple of row data to be inserted
    """
    conn = sqlite3.connect(databaseFn)
    c = conn.cursor()
    sqlString = "INSERT INTO %s VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)" % t
    try:
        c.executemany(sqlString, d)
    except:
        print "Error inserting rows into %s table. Consult source code." % t
    conn.commit()
    conn.close()

def insertMultipleRowsIntoStatePopEstTable(t, d):
    """Insert multiple rows of data into the state population estimate table.

    Arguments:
    t (string) -- name of SQLite database table
    d (tuple) -- tuple of row data to be inserted
    """
    conn = sqlite3.connect(databaseFn)
    c = conn.cursor()
    sqlString = "INSERT INTO %s VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)" % t
    try:
        c.executemany(sqlString, d)
    except:
        print "Error inserting rows into %s table. Consult source code." % t
    conn.commit()
    conn.close()

def insertMultipleRowsIntoUSDARestaurantsTable(t, d):
    """Insert multiple rows of data into the USDA restaurants table.

    Arguments:
    t (string) -- name of SQLite database table
    d (tuple) -- tuple of row data to be inserted
    """
    conn = sqlite3.connect(databaseFn)
    c = conn.cursor()
    sqlString = "INSERT INTO %s VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" % t
    try:
        c.executemany(sqlString, d)
    except:
        print "Error inserting rows into %s table. Consult source code." % t
    conn.commit()
    conn.close()

def query(s):
    """Submit a SQL query.

    Arguments:
    s (string) = SQL query to submit
    """
    conn = sqlite3.connect(databaseFn)
    c = conn.cursor()
    c.execute(s)
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

def initIPPSTable(t, d):
    """Initialize IPPS tables and insert data.

    Arguments:
    t (string) = name of SQLite database table
    d (tuple) -- tuple of row data to be inserted
    """
    createIPPSTable(t)
    insertMultipleRowsIntoIPPSTable(t, d)

def initStatePopEstTable(t, d):
    """Initialize state population estimate table and insert data.

    Arguments:
    t (string) = name of SQLite database table
    d (tuple) -- tuple of row data to be inserted
    """
    createStatePopEstTable(t)
    insertMultipleRowsIntoStatePopEstTable(t, d)

def initUSDARestaurantsTable(t, d):
    """Initialize USDA restaurants tables and insert data.

    Arguments:
    t (string) = name of SQLite database table
    d (tuple) -- tuple of row data to be inserted
    """
    createUSDARestaurantsTable(t)
    insertMultipleRowsIntoUSDARestaurantsTable(t, d)

def printNumRowsInTable(t):
    """Print number of rows in a table.

    Arguments:
    t (string) = name of SQLite database table
    """
    q = query("SELECT COUNT(*) FROM %s" % t)
    print "Number of rows in '%s' table: %s" % (t, q[0][0])

def printNumRowsInAllTables():
    """Print number of rows in all tables.
    """
    printNumRowsInTable('ipps2011')
    printNumRowsInTable('ipps2012')
    printNumRowsInTable('ipps2013')
    printNumRowsInTable('usdaRestaurants')

def getListOfStateAbbreviations():
    """Get list of state abbreviations (51 total including DC)
    """
    states = []
    q = query("SELECT DISTINCT providerState FROM ipps2011")
    for i in range(len(q)):
        states.append(q[i][0])
    return states

