from google import genai


class AI:
    """before starting do the following command to set up a your ai key
    ```
    export GEMINI_API_KEY=YOUR_AI_KEY_GOES_HERE
    ```
    """

    def __init__(self) -> None:
        self.client = genai.Client()

    def askAI(self, prompt: str) -> str:
        """
        prompts the ai and returns the result
        """
        return self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        ).text.__str__()
