from click import prompt
from langchain.prompts import PromptTemplate
    
prompt_template= """
You are a management assistant with a specialization in diabetes and endocrine disease. You are takingnotes for a meeting.
Write a detailed summary of the following transcript of a meeting:
Summary in zh-tw:
------------
{text}
------------
CONSCISE SUMMARY:
"""
prompt_template = PromptTemplate(
    template=prompt_template, 
    input_variables=["text"],
)

refine_template = (
    "Your job is to produce a final summary\n"
    "We have provided an existing summary up to a certain point: {existing_answer}\n"
    "We have the opportunity to refine the existing summary"
    "(only if needed) with some more context below.\n"
    "------------\n"
    "{text}\n"
    "------------\n"
    "Given the new context, refine the original summary and summary 10 keypoints from original text in zh-tw ."
    )
refine_prompt = PromptTemplate(
    template=refine_template,
    input_variables=["existing_answer", "text"],
)

#Make sure you don't lose any important information.
#Also end with a list of:
#- Summary in zh-tw
#- Summary 10 most important keypoint in zh-tw
#    "Given the new context, refine the original summary and summary 10 keypoints from original text in zh-tw ."
