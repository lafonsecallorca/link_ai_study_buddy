import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

app = FastAPI()

class InputToAi(BaseModel):
    user_input: str

#global variables
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
question_tokenizer = AutoTokenizer.from_pretrained("voidful/context-only-question-generator")
question_model = AutoModelForSeq2SeqLM.from_pretrained("voidful/context-only-question-generator")
max_token_limit = 1024
t5_max_token = 512

@app.get("/read_content")
async def scrape_website(website: InputToAi):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(website.user_input, headers=headers)

        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            # Continue with your scraping
            website_contents_list = []
            # soup = BeautifulSoup(website, "html.parser")

            paragraphs = soup.find_all("p")

            for paragraph in paragraphs:
                website_contents_list.append(paragraph.getText())

            headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

            for heading in headings:
                website_contents_list.append(heading.getText())

            website_text = ""

            for content in website_contents_list:
                website_text += content
            
            return website_text
        else:
            print(f"Failed to retrieve content. Status code: {response.status_code}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during scraping: {str(e)}")


@app.get("/generate_summary")
async def generate_summary(website_text: InputToAi):

    # Split the document into chunks
    chunks = [website_text.user_input[i:i+max_token_limit] for i in range(0, len(website_text.user_input), max_token_limit)]

    summary_long = []

    for c in chunks:
        tokenized_text = tokenizer(c, truncation=True, max_length=max_token_limit, return_tensors="pt")
        summary_ids = model.generate(tokenized_text["input_ids"], num_beams=2, min_length=0, max_length=300)
        summary = tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        summary_long.append(summary)

    return summary_long

@app.get("/summary")
async def generate_short_summary(website_content: InputToAi):
    summary_long = await generate_summary(website_content)

    summary_short = []

    for summ in summary_long:
        tokenized_text = tokenizer(summ, padding=True, truncation=True, max_length=max_token_limit, return_tensors="pt")
        question_ids = model.generate(tokenized_text["input_ids"], num_beams=2, min_length=0, max_length=300)
        question = tokenizer.batch_decode(question_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        summary_short.append(question)

    return summary_short


@app.get("/read_along_qs")
async def generate_questions(long_summary: InputToAi):
    summary_long = await generate_summary(long_summary)

    questions_short = []

    for summ in summary_long:
        tokenized_text = tokenizer(summ, padding=True, truncation=True, max_length=max_token_limit, return_tensors="pt")
        question_ids = question_model.generate(tokenized_text["input_ids"], num_beams=2, min_length=0, max_length=300)
        question = question_tokenizer.batch_decode(question_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        questions_short.append(question)

    return questions_short



