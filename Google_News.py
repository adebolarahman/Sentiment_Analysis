# Import the necessary modules
from datetime import date
import datetime
import pandas as pd
from .GoogleNewsEngine import GoogleNews
from math import ceil

def query_input(query: str,startdate: str = None, enddate: str = None, period: str = None, top: int=10, proxy=False):
    '''
    Set the query to search for, run through 10 Google pages, and remove the duplicates
    :param query (str): the search phrase
    :params startdate (str): the start date to search for in the format 'MM/DD/YYYY'
    :params enddate (str): the end date of the query search in the format 'MM/DD/YYYY'
    :param period (str): {'h': 'past 1 hour', 'd':'past 24 hours',
        'w':'past 1 week', 'm':'past 1 month', 'y':'past 1 year'}. When this
        argument is argument is passed, from_date and to_date will be ignored.
    :param top (int): number of top results to return

    :return list:
    '''
    if enddate is None:
        enddate = today = date.today().strftime("%m/%d/%Y")
    if startdate is None:
        startdate = (date.today() - datetime.timedelta(1)).strftime("%m/%d/%Y")

    # If period parameter is provided, use period to instantiate the GoogleNews class
    if period:
        googlenews = GoogleNews(period = period, proxy=proxy)
    else:
        googlenews = GoogleNews(start = startdate, end = enddate, proxy=proxy)

    # Get the first page
    googlenews.search(query)
    output = googlenews.get__links()

    
    # Get other pages 
    for i in range(2, ceil(top/10)+1):
        googlenews.getpage(i)
        output += googlenews.get__links()
        # Concat each search page result with the others

    # Turn the list of dictionary into a DataFrame
    # final_output = pd.DataFrame(output)
    # Remove duplicate records
    # final_output.drop_duplicates(inplace = True)
    # final_output = {out:query for out in output}

    return output[:top]

