from dataclasses import dataclass

import numpy as np
import healpy as hp
from scipy.interpolate import interp1d


@dataclass
class SurveyProperties:
    mask: healpix_map
    distance_grid: float
    selection: float # selection values on distance_grid
    NSIDE: int # same resolution for all z bins? sth to think about. 
    N_mean: float # mean galaxy density
    galaxy_counts: int
    
    def angular_mask(self, x, y, z) -> healpix_map:
        """
        Given a fits map return its value at (x,y,z)
        Some operation on self.mask_filename
        Healpix map of the survey at a given resolution given NSIDE
        """
        print("Approximate resolution at NSIDE {} is {:.2} deg".format(
        self.NSIDE, hp.nside2resol(self.NSIDE, arcmin=True) / 60))
        ipix = hp.vec2pix(x, y, z)
        return mask[ipix]
        

    def radial_selection(self, r) -> float:
        """
        Given a selection, return its value at comoving distance r
        Assumes the radial selection will be given in a file
        in which one column will be the distance_grid and one column
        will be the radial selection.
        """
        selection_interp = interp1d(self.distance_grid, self.selection, fill_value="extrapolate")
        return selection_interp(r)
    

    def survey_response(self, x, y, z) -> healpix_map:
        """
        Product of selection and mask we will use for the bias. 
        """
        r = np.sqrt(x**2 + y**2 + z**2)
        M = angular_mask(x, y, z)
        S = radial_selection(r)
        return M * S
    

    def shot_noise(self) -> healpix_map:
        """
        Survey noise for a given number of galaxies per pixel.
        """
        return 1 / galaxy_counts

        