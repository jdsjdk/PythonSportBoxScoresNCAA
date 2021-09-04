'''
This is to get the Boxscores of all of the for all of the teams in a given date
range.

1.  Get the Boxscores
2.  Create functions and objects for file names and etc.
3.  Output all of the data into a csv file.

Author: Jess Summerhill
Date: 3-11-2021
'''


from sportsreference.ncaab.boxscore import Boxscores
from datetime import datetime as dt
from pathlib import Path as fp
from datetime import date as d
import copy
import csv


class SportsRefGetBoxScores:
    def __init__(self):
        return None

    def main(self):

        def save_file_format():
            # A simple funtion that saves the correct file format
            t = d.today()
            mm = str(t.month)
            dd = str(t.day)
            yy = str(t.year)
            tmdy = "_" + mm + "_" + dd + "_" + yy
            fname = "sports_reference_ncaa_boxscore" + tmdy + ".csv"

            return fname

        def output_csvfile(fname, fheaders=[], boxscore_dict={}):

            # Get the file path, write the folder and the file name, output the CSV file
            p = fp("ouput/")
            p.mkdir(parents=True, exist_ok=True)
            fpath = p / fname

            # Output the CSV file
            with fpath.open("w", encoding="utf-8") as f:
                fwriter = csv.DictWriter(
                    f, dialect="excel", fieldnames=fheaders, delimiter='\t')

                # Write the headers
                fwriter.writeheader()

                # Write the elements out to a file
                fwriter.writerow(boxscore_dict)

            return None

        box_games_dict = {}

        # get the boxscore and the boxscore range
        ncaa_boxscore_rge = Boxscores(dt(2020, 11, 1), dt.today())

        # get the file name
        file_name = save_file_format()

        # Create a list of headers for the csv file
        file_keys_list = list(ncaa_boxscore_rge.games.keys())

        # Do a deep copy of the boxscore games
        box_games_dict = copy.deepcopy(ncaa_boxscore_rge.games)

        output_csvfile(file_name, file_keys_list, box_games_dict)

        print("Success!")

        return None


sprt_ref_box = SportsRefGetBoxScores()
sprt_ref_box.main()
