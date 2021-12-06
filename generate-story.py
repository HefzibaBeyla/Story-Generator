RESOURCES_MAP = {
    'nouns': '~NOUN~',
    'adjectives': '~ADJECTIVE~',
    'present-verbs': '~VERB-PRESENT~',
    'past-verbs': '~VERB-PAST~'
}

WORD_STORE = {}

class Paragraph:
    """Represents a paragraph in the final story, with its associated requirements"""

    def __init__(self, paragraph_text, position):
        self.paragraph_text = paragraph_text
        self.position = position
        self.requirements = self.generate_requirements() # {"adjectives: 5, "past-verbs": 4, "nouns", 6}

    def generate_requirements(self):
        """Given the text, return the quantity of each different type of word required """
        requirements = {}
        for word_type in RESOURCES_MAP:
            requirements[word_type] = self.paragraph_text.count(RESOURCES_MAP[word_type])
        return requirements

    def generate_text(self):
        """Replace the placeholders with words from the word store to generate the final text of the paragraph"""
        updated_text = self.paragraph_text
        for word_type in RESOURCES_MAP.keys():
            while updated_text.find(RESOURCES_MAP[word_type]) >= 0:
                location = updated_text.find(RESOURCES_MAP[word_type])
                fetched_word = self.fetch_word(word_type)
                updated_text = updated_text[:location] + fetched_word + updated_text[location + len(RESOURCES_MAP[word_type]):]

        return updated_text

    def fetch_word(self, word_type):
        """Fetches a word of the required type from the local word store"""
        return WORD_STORE[word_type].pop()

def get_input(word_type, tense=None):
    """Prompt the user to input a word, and return the word they input"""
    if tense is not None:
        output_word = input("Please enter a {} in the {} tense: ".format(word_type, tense))
    else:
        output_word = input("Please enter a {}: ".format(word_type))
    return(output_word)

def build_word_store(requirements):
    """This function takes user inputted words and appends to the global word store"""
    nouns = []
    adjectives = []
    past_verbs = []
    present_verbs = []

    for i in range(requirements["nouns"]):
        nouns.append(get_input("noun"))

    for i in range(requirements["adjectives"]):
        adjectives.append(get_input("adjective"))

    for i in range(requirements["past-verbs"]):
        past_verbs.append(get_input("verb", tense="past"))

    for i in range(requirements["present-verbs"]):
        present_verbs.append(get_input("verb", tense="present"))

    # Add the lists of nouns, adjectives and verbs as values for the keys "nouns", "adjectives" and "verbs" in the dictionary
    WORD_STORE["nouns"] = nouns
    WORD_STORE["adjectives"] = adjectives
    WORD_STORE["past-verbs"] = past_verbs
    WORD_STORE["present-verbs"] = present_verbs

def generate_requirements(*requirements_dicts):
    """Given any number of requirements_dicts, return a combined requirements dict"""
    requirements = {
    'nouns': 0,
    'adjectives': 0,
    'present-verbs': 0,
    'past-verbs': 0
    }
    for requirements_dict in requirements_dicts:
        for word_type in requirements_dict.keys():
            requirements[word_type] += requirements_dict[word_type]

    return requirements


if __name__ == '__main__':

    beginning_1_text = "It was not possible to say when the ~NOUN~ first appeared inside the ~NOUN~\
, but by the time Mademoiselle Wren noticed it, it was already ~ADJECTIVE~. Over the next few \
days, she ~VERB-PAST~ regularly, always thinking about what she had noticed."

    beginning_1 = Paragraph(
        position="beginning",
        paragraph_text = beginning_1_text
    )

    middle_1_text = "The ~NOUN~ never grew any larger, but simply ~VERB-PAST~. The most difficult \
thing to process was its ~ADJECTIVE~ ~NOUN~, which ~VERB-PAST~ far more than would usually be \
considered appropriate."

    middle_1 = Paragraph(
        position="middle",
        paragraph_text=middle_1_text
    )

    end_1_text = "By the time the ~NOUN~ was removed from the ~NOUN~, it had ~VERB-PAST~, so there \
was nothing more to be done. Mademoiselle Wren ~VERB-PAST~ softly, wondering why something that \
~VERB-PRESENT~, ~VERB-PRESENT~ and ~VERB-PRESENT~ never ~VERB-PAST~."

    end_1 = Paragraph(
        position="end",
        paragraph_text=end_1_text
    )

    global_requirements = generate_requirements(
        beginning_1.requirements,
        middle_1.requirements,
        end_1.requirements
    )

    build_word_store(global_requirements)

    print(beginning_1.generate_text() + "\n")
    print(middle_1.generate_text() + "\n")
    print(end_1.generate_text() + "\n")