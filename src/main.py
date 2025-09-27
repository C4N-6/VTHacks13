from piazza_api import Piazza
import os
from fastapi import FastAPI
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
    p.user_login(email=user_email, password=user_password)
    course = p.network(user_course_id)
    all_posts = []
    
    posts = course.iter_all_posts(limit=334, sleep=1)
    for post in posts:
         

        
        
        # Debug: Check if children exist
        children = post.get("children", [])
        
        
        if children:
            
            for i, child in enumerate(children):
               pass
        
        question_text = clean_html(post["history"][0]["content"])
        answers = []
        
        for child in post.get("children", []):
            if child["type"] in ["i_answer", "s_answer"]:
                
                answer_content = clean_html(child["history"][0]["content"])
                answers.append(answer_content)

                
        
        
        
        all_posts.append({
            "question_id": post["id"],
            "question": question_text,
            "answers": answers
        })
    
    return all_posts
    




app = FastAPI()

@app.get("/")
def read_root():
    user = os.getenv("PIAZZA_USER")
    
    password = os.getenv("PIAZZA_PASS")
    
    questions_and_answers = get_latest_question(user,password,"m63z5y05jgj3f6")

    
    for i in questions_and_answers:
        if i["answers"]: 
            with open("./questions/"+i["question_id"]+".txt", "w") as f:
                f.write(i["question"])
                f.write("\n \n")
                for answer in i["answers"]:
                    f.write(answer)
                    f.write("\n \n")

    return questions_and_answers


       


    