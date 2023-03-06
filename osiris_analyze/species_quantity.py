from .analysis import Analysis
from .units import get_quantity_info, unit_convert
import matplotlib.pyplot as plt
import numpy as np
import h5py


class SpeciesQuantity(Analysis):

    def __init__(self, args):
        super().__init__(args)
        self.skip_first_pass = True
        self.__species_name = args['analysis'][1]
        self.__x_var = args['analysis'][2]
        self.__y_vars = args['analysis'][3:]
        if self.out is None:
            self.out = self.dir / ('_'.join((self.__x_var, *self.__y_vars)) + '.png')
        self.__data_files = list((self.ms_dir / 'RAW' / self.__species_name).iterdir())
        self.__data_files.sort(key=lambda path: int(path.name[-9:-3]))
        self.__units = args['units']
        self.__dpi = args['dpi']
        if self.__units == 'physical':
            with open(self.input_file, 'r') as f:
                split = f.readline().split()
                assert len(split) == 5
                assert split[0] == '!'
                assert split[1] == 'skin_depth'
                assert split[2] == '='
                self.__skin_depth = float(split[3])
                assert split[4] == 'm'

    def n_iterations(self):
        return len(self.__data_files)

    def setup_second_pass(self):
        self.__data = np.empty(dtype=np.float64, shape=(len(self.__y_vars) + 1, self.n_iterations()))

    def do_second_pass(self, iteration):
        with h5py.File(self.__data_files[iteration], 'r') as f:
            self.__data[0, iteration] = self.__compute_species_quantity(f, self.__x_var)
            for i, y_var in enumerate(self.__y_vars):
                self.__data[i+1, iteration] = self.__compute_species_quantity(f, y_var)

    def finalize_second_pass(self):
        assert len(self.__y_vars) == 1
        x = self.__data[0, :]
        y = self.__data[1, :]
        x_name_latex, x_unit_latex, x_quantity_type = get_quantity_info(self.__x_var)
        y_name_latex, y_unit_latex, y_quantity_type = get_quantity_info(self.__y_vars[0])
        if self.__units == 'physical':
            x_conversion_factor, x_unit_latex = unit_convert(max(x.min(), x.max(), key=abs), x_quantity_type, self.__skin_depth)
            y_conversion_factor, y_unit_latex = unit_convert(max(y.min(), y.max(), key=abs), y_quantity_type, self.__skin_depth)
            x *= x_conversion_factor
            y *= y_conversion_factor
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel(f'{x_name_latex} [{x_unit_latex}]')
        ax.set_ylabel(f'{y_name_latex} [{y_unit_latex}]')
        fig.savefig(self.out, dpi=self.__dpi)
        plt.close(fig)

    def __compute_species_quantity(self, f, quantity):
        if quantity in ('t', 'ct'):
            return f.attrs['TIME']
        if quantity in ('mu_x', 'mu_y', 'mu_z'):
            return np.mean(f[{'x': 'x2', 'y': 'x3', 'z': 'x1'}[quantity[-1]]])
        assert False
