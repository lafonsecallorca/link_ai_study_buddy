from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/study_bot_url", methods=["GET"])
def read_url():

    def helper_request_method(api_url, endpoint:str, data:str):
        api_url = api_url + endpoint
        json_data = {"user_input": data}
        return requests.get(api_url, json=json_data)

    url = request.args.get("urlInput")

    api_url = "http://127.0.0.1:8000/"
    end_point = "read_content"
    response = helper_request_method(api_url, end_point, url)

    if response.status_code == 200:
        # Process the response or return it
        website_text = response.text
        summary_response = helper_request_method(api_url, "summary", website_text)
        summary = summary_response.text
        read_qs_response = helper_request_method(api_url, "read_along_qs", website_text)
        read_qs = read_qs_response.text
        qa_pairs_response = helper_request_method(api_url, "qa_pairs", website_text)
        qa_pairs = qa_pairs_response.text
        summary_lines = json.loads(summary)
        read_qs_lines = json.loads(read_qs)
        qa_pairs_lines = json.loads(qa_pairs)
        
        return render_template('index.html', summary=summary_lines, read_qs=read_qs_lines, qa_pair=qa_pairs_lines)
     
    else:
        invalid_url = True
        return render_template('index.html', invalid_url=invalid_url)

@app.route("/study_bot_text", methods=["POST"])
def read_text():
    invalid_text = False
    def helper_request_method(api_url, endpoint:str, data:str):
        api_url = api_url + endpoint
        json_data = {"user_input": data}
        return requests.get(api_url, json=json_data)

    url = request.form.get("myText")
    if url == " " or None:
        invalid_text = True
    
    scroll_to_intro= request.args.get("scroll_to_intro")  

    api_url = "http://127.0.0.1:8000/"
    end_point = "summary"
    response = helper_request_method(api_url, end_point, url)

    if response.status_code == 200:
        # Process the response or return it
        summary = response.text
        read_qs_response = helper_request_method(api_url, "read_along_qs", url)
        read_qs = read_qs_response.text
        qa_pairs_response = helper_request_method(api_url, "qa_pairs", url)
        qa_pairs = qa_pairs_response.text
        summary_lines = json.loads(summary)
        read_qs_lines = json.loads(read_qs)
        qa_pairs_lines = json.loads(qa_pairs)
        
        return render_template('index.html', summa=summary_lines, read_q=read_qs_lines, qa=qa_pairs_lines, scroll_to_intro=scroll_to_intro, invalid_text=invalid_text)
     
    else:
        # Handle non-successful responses
        return jsonify({"error": f"Failed to retrieve content. Status code: {response.status_code}"}), 500


if __name__ == "__main__":
    app.run(debug=True)