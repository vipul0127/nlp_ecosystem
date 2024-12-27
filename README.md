<h1>NLP Ecosystem</h1>

<h2>Overview</h2>
<p>
The <strong>NLP Ecosystem</strong> project is a comprehensive collection of natural language processing (NLP) applications designed to address various challenges in text processing, analysis, and understanding. This project combines multiple sub-projects under one umbrella, making it a versatile toolkit for NLP tasks.
</p>

<h2>Home Page Interface</h2>
<p>
The home page provides an intuitive central interface where users can access the applications. Each application is displayed with a description, and clicking on a card redirects to the respective app's interface.
</p>
<p>
Below is an example image of the home page interface:
</p>
<img src="https://media.licdn.com/dms/image/v2/D4E2DAQHS3suFtm4rrQ/profile-treasury-image-shrink_1280_1280/profile-treasury-image-shrink_1280_1280/0/1727890732752?e=1735887600&v=beta&t=0AdFUtAdCoQpjnsqQqfYMyGkIT7rDu3bdswYEwqOSfs" alt="Home Page Interface" style="width:70%; margin:auto; display:block;">

<h2>Features and Applications</h2>

<h3>1. Autocorrect</h3>
<p>
The Autocorrect app implements a spell correction system using algorithms like Jaccard similarity. It provides users with the top 10 suggestions for incorrect spellings and helps refine text input for better accuracy.
</p>
<img src="https://media.licdn.com/dms/image/v2/D4E2DAQFXO6krhJ9_pw/profile-treasury-image-shrink_800_800/profile-treasury-image-shrink_800_800/0/1727890863727?e=1735887600&v=beta&t=cAG-U6bM8qlFvSGalmZkbD3vfecvtcCxXsePG7xX2Eg" alt="Autocorrect App Interface" style="width:70%; margin:auto; display:block;">

<h3>2. Emotion Detection</h3>
<p>
This app analyzes text to detect the emotions expressed, such as joy, sadness, anger, fear, and more. It uses advanced machine learning techniques to understand emotional tones in written communication.
</p>
<img src="https://media.licdn.com/dms/image/v2/D4E2DAQH3kJw7flxD5g/profile-treasury-image-shrink_800_800/profile-treasury-image-shrink_800_800/0/1727890760976?e=1735887600&v=beta&t=x1uPHCThXondOCvTeW9X1iBSlfgT7iToGzK6fKjvd_c" alt="Emotion Detection App Interface" style="width:70%; margin:auto; display:block;">

<h3>3. Sentiment Analysis</h3>
<p>
The Sentiment Analysis app determines the sentiment polarity of a given text, identifying whether it's positive, negative, or neutral. This is particularly useful for analyzing customer feedback, reviews, and opinions.
</p>
<img src="https://media.licdn.com/dms/image/v2/D4E2DAQE4XFQNfYms-Q/profile-treasury-image-shrink_8192_8192/profile-treasury-image-shrink_8192_8192/0/1727890837298?e=1735887600&v=beta&t=jkQXEWgwhgr2QDnQ7w0z4hyGhS1V_66-2H2gN6O-kE4" alt="Sentiment Analysis App Interface" style="width:70%; margin:auto; display:block;">

<h3>4. Spam Detection</h3>
<p>
This app identifies spam messages and filters them out from legitimate communication. It uses classification models trained on datasets to differentiate between spam and non-spam messages.
</p>
<img src="https://media.licdn.com/dms/image/v2/D4E2DAQHuxgerS3l_yA/profile-treasury-image-shrink_800_800/profile-treasury-image-shrink_800_800/0/1727890781249?e=1735887600&v=beta&t=QO_APLPeVT0Jkd1VHpWHbu-hKUDEwwBHAk9-StWaBDw" alt="Spam Detection App Interface" style="width:70%; margin:auto; display:block;">

<h3>5. Summarizer</h3>
<p>
The Summarizer app condenses large pieces of text into concise summaries while retaining the main ideas. It’s ideal for processing lengthy articles, research papers, and documents.
</p>
<img src="https://media.licdn.com/dms/image/v2/D4E2DAQFBFg1o0Wyp9w/profile-treasury-image-shrink_800_800/profile-treasury-image-shrink_800_800/0/1727890807815?e=1735887600&v=beta&t=f_MI9BPtJiLtMypHrcnoQ8JYSR-Xd7NLjpRqAbWzn4E" alt="Summarizer App Interface" style="width:70%; margin:auto; display:block;">

<h3>6. Core NLP</h3>
<p>
The Core NLP app provides foundational tools for tasks like tokenization, stemming, lemmatization, and basic text preprocessing. These functions serve as building blocks for more complex NLP workflows.
</p>

<h3>7. MyApp</h3>
<p>
The MyApp application serves as the main hub for accessing all other apps in this ecosystem. It provides a seamless navigation experience and ensures all functionalities are integrated into a unified system.
</p>


<h2>Project Structure</h2>
<p>The repository is organized as follows:</p>
<ul>
  <li><code>NLP/</code>: Core NLP tools and utilities.</li>
  <li><code>autocorrect/</code>: Codebase for the autocorrect system.</li>
  <li><code>emotion_detection/</code>: Implementation for detecting emotions in text.</li>
  <li><code>myapp/</code>: Main application for integrating and managing all sub-projects.</li>
  <li><code>sentiment_analysis/</code>: Contains sentiment analysis algorithms.</li>
  <li><code>spam/</code>: Implements spam detection models.</li>
  <li><code>summarizer/</code>: Code for text summarization.</li>
  <li><code>db.sqlite3</code>: Database for storing application data.</li>
  <li><code>requirements.txt</code>: List of Python dependencies for the project.</li>
  <li><code>vercel.json</code>: Configuration for deploying the project on Vercel.</li>
</ul>

<h2>Installation</h2>
<p>Follow these steps to set up the NLP Ecosystem locally:</p>
<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/username/nlp_ecosystem.git
cd nlp_ecosystem</code></pre>
  </li>
  <li>Install the required dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Run the application:
    <pre><code>python manage.py runserver</code></pre>
  </li>
  <li>Access the application at <code>http://127.0.0.1:8000</code>.</li>
</ol>

<h2>Usage</h2>
<p>
Once the server is running, navigate to the home page to access the NLP applications. Each app's interface is user-friendly and allows for performing specific NLP tasks seamlessly.
</p>

<h2>Contributing</h2>
<p>Contributions are welcome! Please follow these steps to contribute:</p>
<ol>
  <li>Fork the repository.</li>
  <li>Create a new branch:
    <pre><code>git checkout -b feature-name</code></pre>
  </li>
  <li>Commit your changes and push the branch:
    <pre><code>git commit -m "Description of changes"
git push origin feature-name</code></pre>
  </li>
  <li>Open a pull request.</li>
</ol>

<h2>License</h2>
<p>This project is licensed under the MIT License. See <code>LICENSE</code> for details.</p>

<h2>Contact</h2>
<p>For any questions or suggestions, feel free to reach out:</p>
<ul>
  <li><strong>Email</strong>: <a href="mailto:Vipul22576@iiitd.ac.in">Vipul22576@iiitd.ac.in</a></li>
</ul>
