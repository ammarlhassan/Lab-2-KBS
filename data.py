from facts import CPU, Motherboard, GPU

def load_components(engine):
    """
    Declare a sample pool of components into the engine.
    """
    engine.declare(CPU(name='Intel i9-10900K', socket='LGA1200',
                       performance='high', core_count=10))
    engine.declare(CPU(name='AMD Ryzen 5 5600X', socket='AM4',
                       performance='medium', core_count=6))
    engine.declare(CPU(name='Intel i5-10400',  socket='LGA1200',
                       performance='medium', core_count=6))

    engine.declare(Motherboard(name='ASUS ROG Strix',    socket='LGA1200',
                               ram_slots=4, expansion_slots=2))
    engine.declare(Motherboard(name='MSI B450 Tomahawk', socket='AM4',
                               ram_slots=4, expansion_slots=1))
    engine.declare(Motherboard(name='Gigabyte H410',     socket='LGA1200',
                               ram_slots=2, expansion_slots=1))

    engine.declare(GPU(name='NVIDIA RTX 3080', performance='high',   vram=10))
    engine.declare(GPU(name='AMD RX 6600 XT', performance='medium', vram=8))
    engine.declare(GPU(name='NVIDIA GTX 1650', performance='low',    vram=4))