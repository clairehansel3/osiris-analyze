from .analysis import Analysis, AnalysisTest
import argparse


def prepare_analysis():
    # define command line arguments
    parser = argparse.ArgumentParser(description=' A multithreaded data analysis tool for the particle-in-cell code OSIRIS ')
    parser.add_argument('analysis', nargs='+', help='what analysis to run')
    parser.add_argument('--threads', default=1, type=int, help='number of processes running in parallel (default: 1)')
    # parse arguments
    args = vars(parser.parse_args())
    # sanity check arguments
    assert args['threads'] > 0
    # return analysis object
    return AnalysisTest(args)
