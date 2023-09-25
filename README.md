# Simple Chatbot using PyTorch and Flask

This is a simple chatbot project built using PyTorch and Flask. The chatbot is trained to respond to specific user queries or greetings and can provide answers related to predefined intents.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Training the Chatbot](#training-the-chatbot)
- [Customizing the Intents](#customizing-the-intents)
- [Demo](#demo)


## Prerequisites

Before running the chatbot, make sure you have the following installed:

- Python 3.x
- PyTorch
- Flask
- NLTK (Natural Language Toolkit)

You can install the required Python packages using `pip`:

```bash

pip install torch flask nltk
```

## Project Structure
The project is organized as follows:

- `train.py`: Contains the code for training the chatbot using PyTorch.
- `nltk_utils.py`: Helper functions for tokenization, stemming, and creating bag-of-words vectors.
- `models.py`: Defines the neural network architecture for the chatbot.
- `app.py`: Flask application for running the chatbot server.
- `chat.py`: Functions for interacting with the trained chatbot model.
- `intents.json`: Configuration file containing predefined intents and responses.

## Usage

To run the chatbot, follow these steps:

1. Train the chatbot using `train.py` to create a `data.pth` file containing the trained model.
2. Run the Flask application using `app.py`.

3. Open your web browser and navigate to [http://localhost:5000](http://localhost:5000) to interact with the chatbot.

## Training the Chatbot

You can customize and train the chatbot by modifying the `intents.json` file. Add new intents, patterns, and responses to teach the chatbot how to respond to specific user inputs.

### To Train the Chatbot

1. Edit `intents.json` to customize intents, patterns, and responses.

2. Run the training script `train.py` as mentioned above.

### Customizing the Intents

The `intents.json` file contains predefined intents such as greetings, goodbyes, and specific queries. You can customize these intents or add new ones to tailor the chatbot to your specific use case.

Here's an example of a predefined intent:

```
{
  "tag": "greeting",
  "patterns": [
    "Hi",
    "Hey",
    "How are you",
    "Is anyone there?",
    "Hello",
    "Good day"
  ],
  "responses": [
    "Hey :-)",
    "Hello, thanks for visiting",
    "Hi there, what can I do for you?",
    "Hi there, how can I help?"
  ]
}
```

## Demo
![Chatbot](https://github.com/mohammedshaneeb-ai/AI_Chatbot_using_Pytorch/blob/main/Demo%20Files/AI_Chatbot_from_scratch.jpeg)

