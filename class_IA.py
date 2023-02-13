@dataclass
class IntrinsicAlignments:
  """Class for computing the intrinsic alignments"""

  IA_method: str = 'NLA'
  IA_params: List[Float] # different for each redshift bin

  def computeIA(self,
                density_planes: List[DensityPlane]):
    
    """Computes IA from NLA or TATT model and outputs the 
      2 (real and imag) components"""

    if IA_method == 'NLA':
      return self._NLA(density_planes)
    elif IA_method == 'TATT':
      return self._TATT(density_planes)
    else:
      raise ValueError(f'Unknown IA method')
