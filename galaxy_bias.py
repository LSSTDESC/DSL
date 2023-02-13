from dataclasses import dataclass


@dataclass
class GalaxyBias:
    density_planes: float
    N_mean: float # mean galaxy density
    # We can probably implement a power law directly?
    
    def bias_density(self) -> float:
        """
        N_mean x survey_response x linear function of density_planes
        """
        return # biased density planes

