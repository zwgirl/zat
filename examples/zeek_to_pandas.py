"""Zeek log to Pandas Dataframe Example"""
from __future__ import print_function
import os
import sys
import argparse

# Local imports
from zat.log_to_dataframe import LogToDataFrame

if __name__ == '__main__':
    # Example to populate a Pandas dataframe from a zeek log reader

    # Collect args from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument('zeek_log', type=str, help='Specify a zeek log to run ZeekLogReader test on')
    args, commands = parser.parse_known_args()

    # Check for unknown args
    if commands:
        print('Unrecognized args: %s' % commands)
        sys.exit(1)

    # File may have a tilde in it
    if args.zeek_log:
        args.zeek_log = os.path.expanduser(args.zeek_log)

        # Create a Pandas dataframe from a Zeek log
        log_to_df = LogToDataFrame()
        zeek_df = log_to_df.create_dataframe(args.zeek_log)

        # Print out the head of the dataframe
        print(zeek_df.head())

        # Print out the types of the columns
        print(zeek_df.dtypes)

        # Print out size and memory usage
        print('DF Shape: {:s}'.format(str(zeek_df.shape)))
        print('DF Memory:')
        memory_usage = zeek_df.memory_usage(deep=True)
        total = memory_usage.sum()
        for item in memory_usage.items():
            print('\t {:s}: \t{:.2f} MB'.format(item[0], item[1]/1e6))
        print('DF Total: {:.2f} GB'.format(total/(1e9)))
