# Emotion Detection Web App

An AI-based web application that performs emotion analytics on customer feedback using IBM Watson NLP. Built as a final project for an e-commerce company to better understand customer sentiment on their signature products.

## Overview

This application goes beyond traditional sentiment analysis by detecting finer emotions — **anger**, **disgust**, **fear**, **joy**, and **sadness** — from customer-provided text. It identifies the dominant emotion and can power recommendation systems, automated chatbots, and product feedback pipelines.

## Features

- Emotion detection via IBM Watson NLP (Skills Network)
- Returns scores for 5 emotions + dominant emotion
- REST API endpoint via Flask
- Clean web interface
- Unit tested and statically analysed

## Project Structure

```
final-project/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py   # Watson NLP wrapper
├── templates/
│   └── index.html             # Frontend UI
├── static/
│   └── mywebscript.js         # Frontend logic
├── server.py                  # Flask web server
├── test_emotion_detection.py  # Unit tests
└── README.md
```

## Installation

```bash
pip install flask requests
```

## Usage

### Start the server

```bash
python server.py
```

Then open `http://localhost:5000` in your browser.

### API endpoint

```
GET /emotionDetector?textToAnalyze=<your text>
```

**Example response:**
```
For the given statement, the system response is anger: 0.12, disgust: 0.08,
fear: 0.05, joy: 0.73, sadness: 0.02. The dominant emotion is joy.
```

## Running Tests

```bash
python -m unittest test_emotion_detection.py
```

## Tasks Completed

| # | Task |
|---|------|
| 1 | Fork and clone the project repository |
| 2 | Create emotion detection application using Watson NLP |
| 3 | Format the output of the application |
| 4 | Package the application as `EmotionDetection` |
| 5 | Run unit tests |
| 6 | Deploy as web application using Flask |
| 7 | Incorporate error handling |
| 8 | Run static code analysis |

## Technologies

- **Python 3**
- **Flask** — web framework
- **IBM Watson NLP** — emotion prediction model
- **unittest** — test framework
