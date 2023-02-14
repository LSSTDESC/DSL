from dataclasses import dataclass

import survey_properties as sp


@dataclass
class GalaxyBias:
    density_planes: float
    
    def bias_density(self) -> float:
        """
        N_mean x survey_response x linear function of density_planes
        This is the Poisson intensity, see Eq. 4-5 in https://arxiv.org/abs/2301.03581.
        """
        return N_mean * sp.survey_response(x, y, z) * density_planes # biased density planes
