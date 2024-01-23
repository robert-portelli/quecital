# add_recitals.py


from tomli_w import dump
from quecital.quiz import main_loop
from quecital.multiline_text_editor import get_multiline_edit


def main(quecital_toml_path, quecital_data):
    questions_list = path_to_list_of_dicts(quecital_data)
    new_question_dict = form_toml_entry()
    questions_list.append(new_question_dict)
    with open(quecital_toml_path, "wb") as f:
        dump(quecital_data, f)


def path_to_list_of_dicts(quecital_data):
    """
    Return the list of dictionaries representing questions for the
        selected topic.

    Returns:
        List[Dict]: A list of dictionaries where each dictionary represents
            a question.
    """
    topic_label = main_loop(
        question="Which topic do you want to add a recital to",
        alternatives=quecital_data.keys(),
    )[0]
    return quecital_data[topic_label]["recitals"]

#  TODO handle the key error if ["recitals"] not in quecital_data[topic_label]


def form_toml_entry():
    question = get_multiline_edit("Enter your prompt: ")
    answers = get_multiline_edit("Enter your recital: ")
    hint = get_multiline_edit("Offer a hint? -enter to skip")
    explanation = get_multiline_edit("Offer an explanation? - enter to skip")
    return {
        "question": question,
        "answers": answers,
        #"alternatives": list(alternatives),
        "hint": hint,
        "explanation": explanation,
    }
