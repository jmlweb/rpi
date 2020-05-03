from typing import Dict, Union
from gpiozero import LED, Button

Option = Dict[str, Union[LED, Button]]
Options = Dict[str, Option]
