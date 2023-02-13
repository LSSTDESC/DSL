from dataclasses import dataclass


@dataclass
class SurveyProperties:
    mask_filename: str
    luminosity_function: float
    cut_m_bright: float
    cut_m_faint: float
    cut_M_bright: float
    cut_M_faint: float 
    resolution: int # same resolution for all z bins? sth to think about. 
    
    def mask_at_voxel(self) -> int:
        """
        Given a fits map return its value at (x,y,z) or (ra,dec)
        Some operation on self.mask_filename
        Healpix map of the survey at a given resolution given NSIDE
        """
        return
        
    def selection_at_voxel(self) -> float:
        """
        Given a luminosity function return its value at (x,y,z)
        Some operation on self.luminosity_function
        and potentially self.cut ...
        """
        return
    
    def survey_response(self) -> float:
        """
        Product of selection and mask we will use in the bias
        """
        
        return 
    
    def shot_noise(self) -> float:
        """
        Survey noise for a given number of galaxies per pixel
        """
        return

        