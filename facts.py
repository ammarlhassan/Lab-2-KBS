from experta import Fact, Field

class CPU(Fact):
    """Represents a CPU component."""
    name        = Field(str, mandatory=True)
    socket      = Field(str, mandatory=True)
    performance = Field(str, mandatory=True)  # 'high'/'medium'/'low' enforced in rules
    core_count  = Field(int, mandatory=True)

class Motherboard(Fact):
    """Represents a Motherboard component."""
    name            = Field(str, mandatory=True)
    socket          = Field(str, mandatory=True)
    ram_slots       = Field(int, mandatory=True)
    expansion_slots = Field(int, mandatory=True)

class GPU(Fact):
    """Represents a GPU component."""
    name        = Field(str, mandatory=True)
    performance = Field(str, mandatory=True)  # 'high'/'medium'/'low' enforced in rules
    vram        = Field(int, mandatory=True)