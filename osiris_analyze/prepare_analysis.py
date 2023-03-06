from .species_quantity import SpeciesQuantity
import argparse
import pathlib


def prepare_analysis():

    # define command line arguments
    parser = argparse.ArgumentParser(description=' A multithreaded data analysis tool for the particle-in-cell code OSIRIS ')

    # general options
    parser.add_argument('analysis', nargs='+', help='what analysis to run')
    parser.add_argument('--threads', default=1, type=int, help='number of processes running in parallel (default: 1)')

    # general input/output paths
    parser.add_argument('--dir', type=pathlib.Path, help='path to simulation directory (default: .)')
    parser.add_argument('--ms', type=pathlib.Path, help='path to MS folder containing osiris data (default [dir]/MS)')
    parser.add_argument('--input-file', type=pathlib.Path, help='path to osiris input file (default: [dir]/input.os)')
    parser.add_argument('--out', type=pathlib.Path, help='path to write output file (default: [dir]/[default name])')

    # general data analysis options
    parser.add_argument('--units', choices=('normalized', 'physical'), default='normalized', help='units to use in results (default: normalized)')

    # general plotting options
    parser.add_argument('--dpi', type=int, default=300, help='density per inch to output each frame (default: 300)')

    # parse arguments
    args = vars(parser.parse_args())

    # sanity check arguments
    assert args['threads'] > 0

    # get analysis object
    if args['analysis'][0] == 'plot':
        return SpeciesQuantity(args)
    else:
        assert False
