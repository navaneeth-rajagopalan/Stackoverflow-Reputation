Tool to extract user's reputation from StackOverflow

The tool requires Python 3.x to run
Follow the steps from https://realpython.com/installing-python/ to install and setup python 3.x for the desired platform

Steps to run the tool:

1. Install dependencies:

    a. pandas
        pip install pandas

    b. BeautifulSoup4
        pip install BeautifulSoup4


2. Run the Main.py file.
    
    python Main.py <User's StackOverflow URL> <Region_1> <Region_2> ... <Region_n>
        e.g. 
            python Main.py https://stackoverflow.com/users/696257/dkulkarni Melbourne Sydney

    The Main.py file requires the following arguments:

    a. User's StackOverflow URL - the StackOverflow URL of the user
        e.g.
            https://stackoverflow.com/users/696257/dkulkarni

    b. Region_i - A list of n regions to get the StackOverflow user's relative ranking compared with the respective regions's users. In the below example - Region_1 is Melbourne, Region_2 is Sydney, Region_3 is Bengaluru
        e.g.
            Melbourne Sydney Bengaluru


Additional Notes:

The tool uses Stack Exchange Data Explorer (SEDE) to query StackOverflow database for users from a specific region. The query is saved in SEDE - https://data.stackexchange.com/stackoverflow/query/9320/find-stack-overflow-users-in-your-city-with-user-links. (Feed in the region - say Melbourne in the "Location" textbox and hit "Run Query" button. The URL of the "Download CSV" is used in the tool to query the StackOverlow users from a specific region)