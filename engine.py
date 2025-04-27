from experta import KnowledgeEngine, Fact
from data import load_components
from rules import RecommendationRules

class HardwareRecommender(RecommendationRules, KnowledgeEngine):
    """
    Combines the component‐pool loader and all recommendation rules
    into a single KnowledgeEngine subclass.
    """
    def reset(self):
        super().reset()
        load_components(self)


if __name__ == '__main__':
    engine = HardwareRecommender()
    engine.reset()

    uc = input("Enter your use case (gaming, office, video_editing): ").strip().lower()
    engine.declare(Fact(use_case=uc))
    engine.run()