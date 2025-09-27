import sys
from typing import List, Tuple

from google import genai
from google.genai.chats import GenerateContentResponse
from google.genai.types import GenerateContentConfig
from .FileSelector import getFilesForPrompt

promptTemplate = """
use this

'''
%s
'''

'''

1->(do not include the 1-> in the answer please) %s (answer this question only !!!!)

'''


imagine your a professor answering a students question in 2-4 sentences make sure you answer the question above in front of 1 - >  answered do not filter out any important information so the student gets all the information he needs  do not write any code unless the students sends code in (also answer in 2-4 sentences only) remove the 1 - > in the beginning of the paragraph 
"""


class AI:
    """before starting do the following command to set up a your ai key
    ```
    export GEMINI_API_KEY=YOUR_AI_KEY_GOES_HERE
    ```
    """

    def __init__(self, textFolder) -> None:
        self.client = genai.Client()
        self.piazzaQuestionsDirectory = textFolder

    def askAI(self, prompt: str, numberOfResults: int = 3) -> List[Tuple[str, str]]:
        """
        prompts the ai and returns the result
        """
        files: List[Tuple[str, int]] = getFilesForPrompt(
            self.piazzaQuestionsDirectory, prompt, numberOfResults
        )
        results: List[Tuple[str, str]] = []

        while results.__len__() <= numberOfResults and files.__len__() != 0:
            currFile = files.pop()
            result: GenerateContentResponse = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=promptTemplate % (currFile[0], prompt),
            )

            results.append((result.text.__str__(), getURL(currFile[0])))

        return results


def getURL(filename):
    if str(filename).count(".") > 1:
        return "hidden files dont work"
    name_without_extension = filename.rsplit(".", 1)[0]
    return f"https://piazza.com/class/m63z5y05jgj3f6/post/{name_without_extension}"
