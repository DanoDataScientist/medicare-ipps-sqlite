# Define functions used to retrieve data from the SQLite database and to
# create plots.

import matplotlib.pyplot as plt

import sql

stateAbbrev = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL',
               'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA',
               'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE',
               'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI',
               'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV',
               'WY']

# Functions used to retrieve data from the SQLite database
def getTotalDischargesPerState(s, y):
    """Get total discharges per state for a specific drgDefinition and year.

    Arguments:
    s (string) = drgDefinition
    y (string) = year ('2011', '2012', or '2013')

    Returns:
    (list) -- list of total discharges for each state
    """
    tdList = []
    for i in range(len(stateAbbrev)):
        q = sql.query('SELECT SUM(totalDischarges) FROM ipps' + y + ' ' +
                      "WHERE drgDefinition LIKE '%" + s + "%' " +
                      "AND providerState='" + stateAbbrev[i] + "'")
        tdList.append(int(q[0][0]))
    return tdList

def getStatePopEst65AndOver(s, y):
    """Get state population estimate for age>=65 for a specific sex and year.

    Arguments:
    s (string) -- sex ('0' = Total, '1' = Male, '2' = Female)
    y (string) -- year ('2010', '2011', '2012', '2013', '2014')

    Returns:
    (list) -- population estimate for age>=65 for specific sex for each state
    """
    speList = []
    for i in range(len(stateAbbrev)):
        q = sql.query('SELECT SUM(popEst' + y + 'Civ) FROM statePopEst ' +
                      'WHERE sex=' + s + ' AND (age BETWEEN 65 AND 85) ' +
                      "AND name='" + stateAbbrev[i] + "'")
        speList.append(int(q[0][0]))
    return speList

# Functions used to create plots
def quantityVsState(s, y, fn):
    """Create a scatter plot of the total discharges vs state for a
    specific drgDefinition. Save the plot as a PNG image file in the
    results/ directory.

    Arguments:
    s (string) = drgDefinition for which the total discharges are plotted
    y (string) = year for which data are plotted ('2011', '2012', or '2013')
    fn (string) = filename of PNG image
    """
    xList = range(51)
    yList = getTotalDischargesPerState(s, y)
    plt.figure(num=1)
    plt.xlabel('state')
    plt.ylabel('total discharges:\n' + s)
    plt.subplots_adjust(bottom=0.1, left=0.15, right=0.9, top=0.9,
                        hspace=0.2, wspace=0.2)
    plt.grid(linestyle=':')
    plt.plot(xList, yList, color='r', linestyle='None',
             marker='o', markersize=6)
    for i in range(len(stateAbbrev)):
        plt.text(xList[i], yList[i], stateAbbrev[i], fontsize=10)
    plt.savefig(fn, format='png')
    plt.clf()

def totalDischargesVsState(s, y, fn):
    """Create a scatter plot of the total discharges vs state for a
    specific drgDefinition. Save the plot as a PNG image file in the
    results/ directory.

    Arguments:
    s (string) = drgDefinition for which the total discharges are plotted
    y (string) = year for which data are plotted ('2011', '2012', or '2013')
    fn (string) = filename of PNG image
    """
    yList = getTotalDischargesPerState(s, y)
    quantityVsState(yList, fn)

