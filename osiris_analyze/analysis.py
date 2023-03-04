import abc


class Analysis(abc.ABC):

    def __init__(self, args):
        self._n_threads = args['threads']

    def n_threads(self):
        return self._n_threads

    @abc.abstractmethod
    def n_passes(self):
        pass

    @abc.abstractmethod
    def n_iterations(self):
        pass

    @abc.abstractmethod
    def setup(self, pass_idx):
        pass

    @abc.abstractmethod
    def do_pass(self, pass_idx, iteration):
        pass

    @abc.abstractmethod
    def merge(self, pass_idx, result, new_result):
        pass

    @abc.abstractmethod
    def finalize(self, pass_idx):
        pass


class AnalysisTest(Analysis):

    def __init__(self, args):
        super().__init__(args)

    def n_passes(self):
        return 1

    def n_iterations(self):
        return 10

    def setup(self, pass_idx):
        print('setting up pass', pass_idx)

    def do_pass(self, pass_idx, iteration):
        print('pass', pass_idx, 'iteration', iteration)

    def merge(self, pass_idx, result, new_result):
        return {}

    def finalize(self, pass_idx, result):
        print('finalizing', pass_idx)
