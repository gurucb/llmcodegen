from abc import ABC, abstractmethod

class nlp_provider:
    # TODO: pickup stop_words from a file rather than hard coding
    stop_words = "['and', 'of', 'it']"
    word_breaker  = ' '

    @abstractmethod
    def get_attributes(user_prompt) -> list[str]:
        pass

    @abstractmethod
    def get_entities(user_prompt) -> list[str]:
        pass
