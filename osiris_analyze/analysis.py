import pathlib


class Analysis(object):

    def __init__(self, args):
        self.skip_first_pass = False
        self.dir = pathlib.Path('.') if args['dir'] is None else args['dir']
        self.ms_dir = (self.dir / 'MS') if args['dir'] is None else args['ms_dir']
        self.input_file = (self.dir / 'input.os') if args['dir'] is None else args['input_file']
        self.out = args['out']
        self.__n_threads = args['threads']
        assert self.__n_threads > 0

    def n_threads(self):
        return self.__n_threads

    def n_iterations(self):
        pass

    def setup_first_pass(self):
        pass

    def do_first_pass(self, iteration):
        pass

    def merge_first_pass(self, result, new_result):
        pass

    def finalize_first_pass(self, result):
        pass

    def setup_second_pass(self):
        pass

    def do_second_pass(self, iteration):
        pass

    def finalize_second_pass(self):
        pass
