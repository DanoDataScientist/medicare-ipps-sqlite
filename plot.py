# Define functions used to retrieve data from the SQLite database and to
# create plots.

import matplotlib.pyplot as plt

import sql

state_abbrev = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL',
                'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA',
                'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE',
                'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI',
                'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV',
                'WY']

# Functions used to retrieve data from the SQLite database
def get_total_discharges_per_state(s, y):
    """Get total discharges per state for a specific drgDefinition and year.

    Arguments:
    s (string) -- drgDefinition
    y (string) -- year ('2011', '2012', or '2013')

    Returns:
    (list) -- list of total discharges for each state
    """
    td_list = []
    for i in range(len(state_abbrev)):
        q = sql.query('SELECT SUM(totalDischarges) FROM ipps' + y + ' ' +
                      "WHERE drgDefinition LIKE '%" + s + "%' " +
                      "AND providerState='" + state_abbrev[i] + "'")
        if q[0][0] is None:
            td_list.append(0)
        else:
            td_list.append(int(q[0][0]))
    return td_list

def get_state_pop_est_65_and_over(s, y):
    """Get state population estimate for age>=65 for a specific sex and year.

    Arguments:
    s (string) -- sex ('0' = Total, '1' = Male, '2' = Female)
    y (string) -- year ('2010', '2011', '2012', '2013', '2014')

    Returns:
    (list) -- population estimate for age>=65 for specific sex for each state
    """
    spe_list = []
    for i in range(len(state_abbrev)):
        q = sql.query('SELECT SUM(popEst' + y + 'Civ) FROM statePopEst ' +
                      'WHERE sex=' + s + ' AND (age BETWEEN 65 AND 85) ' +
                      "AND name='" + state_abbrev[i] + "'")
        spe_list.append(int(q[0][0]))
    return spe_list

# Functions used to create plots
def create_plot(x_list, x_label, y_list, y_label, p_title, fn):
    """Create a scatter plot for a quantity y vs a quantity x.
    Save the plot as a PNG image file in the results/ directory.

    Arguments:
    x_list (list) -- list of x-axis data
    x_label (string) -- x-axis label
    y_list (list) -- list of y-axis data
    y_label (string) -- y-axis label
    p_title (string) -- plot title
    fn (string) -- filename of PNG image
    """
    plt.figure(num=1)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(p_title)
    plt.subplots_adjust(bottom=0.1, left=0.15, right=0.9, top=0.9,
                        hspace=0.2, wspace=0.2)
    plt.grid(linestyle=':')
    plt.plot(x_list, y_list, color='r', linestyle='None',
             marker='o', markersize=6)
    for i in range(len(state_abbrev)):
        plt.text(x_list[i], y_list[i], state_abbrev[i], fontsize=12)
    plt.savefig('plots/' + fn, format='png')
    plt.clf()

def plot_total_discharges_vs_state(s, y, fn):
    """Create a scatter plot of the total discharges vs state for a
    specific drgDefinition. Save the plot as a PNG image file in the
    results/ directory.

    Arguments:
    s (string) -- drgDefinition for which the total discharges are plotted
    y (string) -- year for which data are plotted ('2011', '2012', or '2013')
    fn (string) -- filename of PNG image
    """
    x_list = range(51)
    x_label = 'state'
    y_list = get_total_discharges_per_state(s, y)
    y_label = y + ' total discharges'
    create_plot(x_list, x_label, y_list, y_label, s, fn)

def plot_total_discharges_per_state_pop_vs_state(s, y, fn):
    """Create a scatter plot of the total discharges per state population
    vs state for a specific drgDefinition. Save the plot as a PNG image
    file in the results/ directory.

    Arguments:
    s (string) -- drgDefinition for which the total discharges are plotted
    y (string) -- year for which data are plotted ('2011', '2012', or '2013')
    fn (string) -- filename of PNG image
    """
    x_list = range(51)
    x_label = 'state'
    s_list = get_state_pop_est_65_and_over('0', y)
    d_list = get_total_discharges_per_state(s, y)
    y_list = []
    for i in range(len(s_list)):
        d = float(d_list[i]) / float(s_list[i])
        y_list.append(d)
    y_label = y + ' total discharges / state pop (age 65 and over)'
    create_plot(x_list, x_label, y_list, y_label, s, fn)

def plot_total_discharges_vs_state_pop(s, y, fn):
    """Create a scatter plot of the total discharges vs state population
    for a specific drgDefinition. Save the plot as a PNG image file in the
    results/ directory.

    Arguments:
    s (string) -- drgDefinition for which the total discharges are plotted
    y (string) -- year for which data are plotted ('2011', '2012', or '2013')
    fn (string) -- filename of PNG image
    """
    s_list = get_state_pop_est_65_and_over('0', y)
    x_list = []
    for i in range(len(s_list)):
        d = float(s_list[i]) / (1.0e6)
        x_list.append(d)
    x_label = 'state population (millions), age 65 and over'
    y_list = get_total_discharges_per_state(s, y)
    y_label = y + ' total discharges'
    create_plot(x_list, x_label, y_list, y_label, s, fn)

