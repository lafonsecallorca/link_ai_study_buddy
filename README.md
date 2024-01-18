<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Study Buddy AI Bot</title>
</head>

<body>

    <h1>Study Buddy AI Bot</h1>

    <p>Study Buddy is your personal AI bot designed to assist you in summarizing articles, providing active reading prompts, and generating review questions. Whether you input plain text or a URL, Study Buddy leverages state-of-the-art natural language processing models to enhance your study experience.</p>

    <h2>Features</h2>

    <ul>
        <li><strong>Summarization:</strong> Get concise summaries of articles to quickly grasp key information.</li>
        <li><strong>Active Reading Prompts:</strong> Receive prompts to engage actively with the content while reading.</li>
        <li><strong>Review Questions & Answers:</strong> Generate questions and answers for effective review and understanding.</li>
    </ul>

    <h2>Getting Started</h2>

    <h3>Prerequisites</h3>

    <ul>
        <li>Python 3.7 or higher</li>
        <li>FastAPI</li>
        <li>Transformers library</li>
        <li>BeautifulSoup</li>
        <li>Selenium</li>
        <li>Flask</li>
    </ul>

    <h3>Installation</h3>

    <ol>
        <li>Clone the repository:</li>
    </ol>

    <pre><code>git clone https://github.com/lafonsecallorca/link_ai_study_buddy.git</code></pre>

    <ol start="2">
        <li>Install dependencies:</li>
    </ol>

    <pre><code>pip install -r requirements.txt</code></pre>

    <ol start="3">
        <li>Run the FastAPI server:</li>
    </ol>

    <pre><code>uvicorn main:app --reload</code></pre>

    <ol start="4">
        <li>Open the Study Buddy web application:</li>
    </ol>

    <pre><code>http://127.0.0.1:8000/</code></pre>

    <h2>Usage</h2>

    <ol>
        <li><strong>Text Input:</strong>
            <ul>
                <li>Enter your text in the designated area and click "Submit."</li>
                <li>Receive a summary, active reading prompts, and review questions.</li>
            </ul>
        </li>
        <li><strong>URL Input:</strong>
            <ul>
                <li>Enter a URL in the designated area and click "Submit."</li>
                <li>Receive a summary, active reading prompts, and review questions based on the content of the provided URL.</li>
            </ul>
        </li>
    </ol>

    <h2>Contributing</h2>

    <p>Contributions are welcome! If you have ideas for improvements or encounter issues, feel free to <a href="https://github.com/lafonsecallorca/link_ai_study_buddy/issues">open an issue</a> or submit a pull request.</p>

    <h2>License</h2>

    <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>

    <h2>Acknowledgments</h2>

    <p>Special thanks to the developers of the Transformers library and FastAPI for their invaluable contributions to the project.</p>

</body>

</html>
