def get_input(word_type, first_occurrence, tense=None):
    """Prompt the user to input a word, and return the word they input"""
    if first_occurrence == True:
        if tense is not None:
            output_word = input("Please enter a {} in the {} tense: ".format(word_type, tense))
        else:
            output_word = input("Please enter a {}: ".format(word_type))
    else:
        if tense is not None:
            output_word = input("Please enter another {} in the {} tense: ".format(word_type, tense))
        else:
            output_word = input("Please enter another {}: ".format(word_type))
    return(output_word)

noun_1 = get_input("noun", True)
noun_2 = get_input("noun", False)
adjective_1 = input("Please enter an adjective: ")
adjective_2 = input("Please enter another adjective: ")
adjective_3 = input("Please enter another adjective: ")
verb = input("Please enter a verb in the past tense: ")



print(
    "The {}, {}, {} {} over the {} {}.".format(
        noun_1,
        noun_2,
        adjective_1,
        adjective_2,
        adjective_3,
        verb
    )
)