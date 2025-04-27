from experta import Rule, Fact, TEST, MATCH
from facts import CPU, Motherboard, GPU

class RecommendationRules:
    @Rule(Fact(use_case=MATCH.uc),
          TEST(lambda uc: uc not in ('gaming', 'office', 'video_editing')),
          salience=10)
    def unknown_use_case(self, uc):
        """Default unrecognized use case to 'office'."""
        print(f"Use case '{uc}' not recognized; defaulting to office.\n")
        self.declare(Fact(use_case='office'))

    @Rule(
        Fact(use_case='gaming'),
        CPU(name=MATCH.cpu_name, socket=MATCH.socket,
            performance='high', core_count=MATCH.core),
        TEST(lambda core: core >= 8),
        Motherboard(name=MATCH.mb_name, socket=MATCH.socket,
                    expansion_slots=MATCH.exp_slots),
        TEST(lambda exp_slots: exp_slots >= 1),
        GPU(name=MATCH.gpu_name, performance='high', vram=MATCH.vram),
        TEST(lambda vram: vram >= 8),
        salience=5
    )
    def gaming_config(self, cpu_name, mb_name, gpu_name, socket, core, exp_slots, vram):
        print("=== GAMING CONFIGURATION ===")
        print(f"CPU         : {cpu_name} ({socket}, {core} cores, high perf)")
        print(f"Motherboard : {mb_name} ({socket}, {exp_slots} PCIe slots)")
        print(f"GPU         : {gpu_name} ({vram}GB VRAM, high perf)\n")
        print(f"Compatibility confirmed: socket {socket}, {exp_slots} slot(s).")
        self.halt()

    @Rule(
        Fact(use_case='office'),
        CPU(name=MATCH.cpu_name, socket=MATCH.socket,
            performance='medium', core_count=MATCH.core),
        TEST(lambda core: core <= 6),
        Motherboard(name=MATCH.mb_name, socket=MATCH.socket,
                    expansion_slots=MATCH.exp),
        TEST(lambda exp: exp >= 1),
        GPU(name=MATCH.gpu_name, performance='low'),
        salience=5
    )
    def office_config(self, cpu_name, mb_name, gpu_name, socket, core, exp):
        print("=== OFFICE CONFIGURATION ===")
        print(f"CPU         : {cpu_name} ({socket}, {core} cores, med perf)")
        print(f"Motherboard : {mb_name} ({socket}, {exp} PCIe slot)")
        print(f"GPU         : {gpu_name} (low perf)\n")
        print(f"Compatibility confirmed: socket {socket}, {exp} slot(s).")
        self.halt()

    @Rule(
        Fact(use_case='video_editing'),
        CPU(name=MATCH.cpu_name, socket=MATCH.socket,
            performance='high', core_count=MATCH.core),
        TEST(lambda core: core >= 8),
        Motherboard(name=MATCH.mb_name, socket=MATCH.socket,
                    ram_slots=MATCH.ram_slots),
        TEST(lambda ram_slots: ram_slots >= 4),
        GPU(name=MATCH.gpu_name, performance='high', vram=MATCH.vram),
        TEST(lambda vram: vram >= 8),
        salience=5
    )
    def video_editing_config(self, cpu_name, mb_name, gpu_name, socket, core, ram_slots, vram):
        print("=== VIDEO EDITING CONFIGURATION ===")
        print(f"CPU         : {cpu_name} ({socket}, {core} cores, high perf)")
        print(f"Motherboard : {mb_name} ({socket}, {ram_slots} RAM slots)")
        print(f"GPU         : {gpu_name} ({vram}GB VRAM, high perf)\n")
        print(f"Compatibility confirmed: socket {socket}, {ram_slots} RAM slot(s).")
        self.halt()