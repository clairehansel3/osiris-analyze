import numpy as np


def get_quantity_info(quantity):
    return {
        't': ('$t$', '$\\omega_p^{-1}$', 'time'),
        'ct': ('$ct$', '$c / \\omega_p$', 'length'),
        'mu_x': ('$\\mu_x$', '$c / \\omega_p$', 'length'),
        'mu_y': ('$\\mu_x$', '$c / \\omega_p$', 'length'),
        'mu_z': ('$\\mu_x$', '$c / \\omega_p$', 'length'),
    }[quantity]


def unit_convert(characteristic_scale, quantity_type, skin_depth):
    # determine basic conversion factor and unit
    if quantity_type == 'length':
        conversion_factor = skin_depth
        unit_name_latex = 'm'
    elif quantity_type == 'time':
        # c = 299792458 m/s
        conversion_factor = skin_depth / 299792458
        unit_name_latex = 's'
    elif quantity_type == 'electric field':
        # (m_e c^2) / e = 510998.9500015 V
        conversion_factor = 510998.9500015 / skin_depth
        unit_name_latex = 'V$\;$m$^{-1}$'
    elif quantity_type == 'magnetic field':
        # (m_e c) / e = 0.00170450902 Tm
        conversion_factor = 0.00170450902 / skin_depth
        unit_name_latex = 'T'
    elif quantity_type == 'poynting vector':
        # (m_e^2 c^3) / (e^2 mu_0) = 6.9312162e8 W
        conversion_factor = 6.9312162e8 / (skin_depth ** 2)
        unit_name_latex = 'W$\;$m$^{-2}$'
    elif quantity_type == 'density':
        # (1 / (4 * pi * r_e))
        conversion_factor = 2.82395872e7 / (skin_depth ** 2)
        unit_name_latex = 'cm$^{-3}$'
        return conversion_factor, unit_name_latex
    else:
        assert False
    # determine metric prefix
    characteristic_scale *= conversion_factor
    prefix_names = ['a', 'f', 'p', 'n', '$\\mu$', 'm', '', 'k', 'M', 'G', 'T', 'P']
    for i, prefix_name in enumerate(prefix_names):
        if (10 ** (-18 + 3*i)) < characteristic_scale < (10 ** (-18 + 3*(i+1))):
            conversion_factor /= (10 ** (-18 + 3*i))
            unit_name_latex = prefix_name + unit_name_latex
            break
    return conversion_factor, unit_name_latex
