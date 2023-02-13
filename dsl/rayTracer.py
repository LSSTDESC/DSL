from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class RayTracer:
    """ Class for doing weak lensing ray tracing, using either Born, or 
    PostBorn approximation.
    """
    method: str = 'Born'

    def render(self, 
               lens_planes: List[DensityPlane], 
               source_redshifts: List[Float]) -> Tuple:
        """ Render the lensed image, using either Born or PostBorn 
        approximation.

        lens_planes: List of lens planes, 
        """
        if self.method == 'Born':
            return self._render_born(lens_planes, source_redshifts)
        elif self.method == 'PostBorn':
            return self._render_post_born(lens_planes, source_redshifts)
        else:
            raise ValueError(f'Unknown ray tracing method: {self.method}')
