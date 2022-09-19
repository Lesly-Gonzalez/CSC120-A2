# Import a few useful containers from the typing module
from typing import Dict, Union, Optional

class Computer:

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
        def __init__(self, description: str, 
                 processor_type: str, hard_drive_capacity: int, memory: int,  operating_system: str, year_made: int,
                    price: int) -> None:
            self.description =  description
            self.processor_type = processor_type
            self.hard_drive_capacity = hard_drive_capacity
            self.memory = memory
            self.operating_system = operating_system
            self.year_made = year_made
            self.price = price
            
        """
        This helper function takes in a bunch of information about a computer,
        and packages it up into a python dictionary to make it easier to store
        """
        def create_computer(description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
            return {'description': description,
                    'processor_type': processor_type,
                    'hard_drive_capacity': hard_drive_capacity,
                    'memory': memory,
                    'operating_system': operating_system,
                    'year_made': year_made,
                    'price': price
            }


        
        
