from piazza_api import Piazza
import os
import re
def clean_html(text):
    """
    Cleans HTML content by:
    - Removing all HTML tags
    - Replacing <br> and newline tags with spaces
    - Converting multiple spaces/newlines to a single space
    """
    # Replace <br> and variants with space
    text = re.sub(r'<br\s*/?>', ' ', text)
    
    # Remove all other HTML tags
    text = re.sub(r'<.*?>', ' ', text)
    
    # Replace multiple whitespace characters with a single space
    text = re.sub(r'\s+', ' ', text)
    
    # Trim leading/trailing spaces
    return text.strip()

def get_latest_question(user_email, user_password, user_course_id):
    p = Piazza()
    p.user_login(email= user_email, password= user_password)
    course = p.network(user_course_id)

    # Get the latest post (question)
    #limit gets the question number from the top
    posts = course.iter_all_posts(limit=1000)
    for post in posts:
        question_id = post["id"]
        question_text = post["history"][0]["content"]
    
    question_text = clean_html(question_text)
    return question_text
       


    