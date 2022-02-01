import json
import uuid
from deep_translator import GoogleTranslator
translator = GoogleTranslator(source='auto', target='ru') 


def txt_flash_to_list(path_file: str) -> list:
    word_list = []
    with open(path_file) as f:
        for line in f:
            line = line.replace(" \n", "").replace("\n", "")
            if line:
                word_list.append(line)
    return word_list


class FlashCard:
    def __init__(self, eng, rus) -> None:
        self.id = str(uuid.uuid4())
        self.frontContent = "**" + eng + "**"
        self.backContent = "**" + rus + "**"

if __name__ == "__main__":
    eng_list = txt_flash_to_list("1.txt")
    flashcards_list = []

    for i in range(len(eng_list)):
        eng_word = eng_list[i].split(" ")[0]
        print(eng_word)
        translated = translator.translate(eng_word)
        x = FlashCard(eng=eng_list[i], rus=translated)
        print(x.__dict__)
        flashcards_list.append(x.__dict__)
    final_dict = {"version":1,"flashcards":flashcards_list}
    with open("mem_me_data.json", "w+") as output_json:
        json.dump(final_dict, output_json)
