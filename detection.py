import numpy as np

class planets:
    def __init__(self, name, depth, duration, number=3):
        """_Defines a set of parameters for planets in our solar system_

        Args:
            name (_type_): _name of the planet_
            depth (_type_): _transit depth in ppm_
            duration (_type_): _transit duration in hours_
            number (_type_): _number of transits_
        """
        super().__init__()
        
        self.name = name
        self.depth = depth
        self.duration = duration
        self.number = number
        
    def noise_level(self, eta=7.1):
        """_Function that implements equation 23 in Marchiori et al (2019) paper_

        Args:
            eta (float, optional): _Statistical significance value adopted for PLATO_. Defaults to 7.1.

        Returns:
            _nsr_: _noise level of the planet transit signal at detector level_
        """
        nsr = self.depth * np.sqrt*(self.duration * self.number) / eta
        return nsr    