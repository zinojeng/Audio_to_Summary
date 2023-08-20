from langchain.prompts import PromptTemplate
    
prompt_template_questions = """
You are a management assistant with a specialization in diabetes and endocrine disease. You are takingnotes for a meeting.
Write a detailed summary of the following transcript of a meeting:

------------
{text}
------------



QUESTIONS:
"""
PROMPT_QUESTIONS = PromptTemplate(template=prompt_template_questions, input_variables=["text"])

#Make sure you don't lose any important information.
#Also end with a list of:
#- Summary in zh-tw
#- Summary 10 most important keypoint in zh-tw
