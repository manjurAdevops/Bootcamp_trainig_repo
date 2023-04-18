#! usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# This script will convert XML to CSV
# Usage : python XML_to_CSV.py
#            --infile = <"D:\Python\bootcamp\Mock\Team_Skillset.xml">
#            --outfile = <"D:\Python\bootcamp\Mock\Team_Skillset.csv">
# Based on different scenario script will return different exit code as follows:
#  0: Ran Successfully.
# -1: Script Failure.
################################################################################

# Importing Required Libraries
import argparse
import sys
import pandas as pd
import xml.etree.ElementTree as ET
import os

# Defining Global Parameters
infile = ""
outfile = ""

################################################################################
# Function Name  : process_cmdl_args
# Arguments      : None
# Return Value   : -1 (in case of failure)
# Called By      : main
# Description    : Read command line arguments
################################################################################
def process_cmdl_args():
    global infile, outfile

    print("Reading Command Line Arguments..")

    example_usage = '''example usage:
                --infile = <"D:\Python\bootcamp\Mock\Team_Skillset.xml">
                --outfile = <"D:\Python\bootcamp\Mock\Team_Skillset.csv">'''

    # Reading All Command Line Arguments
    parser = argparse.ArgumentParser(description = example_usage)
    parser.add_argument("-infile", "--infile", type=str, required=True, help="Enter Ocnf file path")
    parser.add_argument("-outfile", "--outfile", type=str,required=True, help="Enter csv file path")

    # Assigning the Command Line Arguments to Global Variables
    try:
        args = parser.parse_args()
        infile = args.infile
        outfile = args.outfile

        if not os.path.exists(infile):
            raiseException("Exception Occured :" ,"Invalid infile path can't find XML file")

        directory = os.path.dirname(outfile)
        if not os.path.exists(directory):
            os.makedirs(directory)

    except Exception as e:
        raiseException(e, "Error While Reading Command Line arguments")
    else:
        print("Arguments Fetched Successfully!")

################################################################################
# Function Name  : raiseException
# Arguments      : err, msg
# Return Value   : -1
# Called By      : Wherever we want to raise exception.
# Description    : Helper Function to give exception and exit the system!
################################################################################
def raiseException(err, msg):
    print(f"Exception Occurred: {msg} : {err}")
    sys.exit(-1)

################################################################################
# Function Name  : convert_to_csv
# Arguments      : infile, outfile
# Return Value   : 0,-1
# Called By      : main
# Description    : This function will convert ocnf to csv
################################################################################
def convert_to_csv(infile, outfile):
    print("Convering xml to csv...")
    fields = ["Company", "Team_Member", "Python_Rating","Git", "SW_Code_Quality", "Database", "Jenkins"]
    rows = []
    try:
        # parse xml file and get root
        tree = ET.parse(infile)
        root = tree.getroot()
        company_name = root.tag

        templist = []
        root = next(root.iter('ListOfTeamMembers'))
        # iterating through the xml file
        for iteam in root:
            templist.append(company_name)
            for subiteams in iteam:
                templist.append(subiteams.text)
            rows.append(templist)
            templist = []

        # converting xml to csv using pandas
        df = pd.DataFrame(rows, columns=fields)
        df.to_csv(outfile, index=False)
        print("csv file generated successfully...")

    except Exception as e:
        raiseException(e,"Error while converting XML to CSV")

################################################################################
# Function Name  : main
# Arguments      : None
# Return Value   : 0,-1
# Called By      : None
# Description    : This is the main function.
################################################################################
def main():
    global infile, outfile

    # Processing Command Line Arguments
    process_cmdl_args()

    # converting to csv
    convert_to_csv(infile, outfile)


if __name__ == '__main__':
    print("================== XML_TO_CSV : SCRIPT RUNNING ==================")
    main()
