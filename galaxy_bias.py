from dataclasses import dataclass

import survey_properties as sp


@dataclass
class GalaxyBias:
    density_planes: float
    # We can probably implement a power law directly?
    
    def bias_density(self) -> float:
        """
        N_mean x survey_response x linear function of density_planes
        The exact implementation will depend on the shape of density_planes
        """
        return N_mean * density_planes # biased density planes


    def poisson_intensity(self, x, y, z) -> float:
        """ This is the intensity of the Poisson process that generates galaxies
        """
        lambdap = sp.survey_response(x, y, z) * bias_density
        return lambdap