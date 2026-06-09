# smart-AI-travel-planner

An AI-powered agent that designs custom travel itineraries from your starting city, providing live weather updates and smart budget tracking.

## ✨ Features
* 📍 **Custom Routing:** Plan trips from any starting city to your dream destination.
* 🌤️ **Live Weather:** Uses search tools to fetch real-time weather conditions for the trip.
* 💰 **Budget Tracking:** Built-in AI calculator ensures the total itinerary cost stays within your defined budget.
* 🖥️ **Interactive UI:** Easy-to-use web interface powered by Gradio.

## 🛠️ Setup & Installation

### Prerequisites
To run this project, you need a **Groq API Key**. You can get one for free from the Groq Cloud Console. 
*(Note: Never share your API key publicly!)*

### Required Libraries
If you want to run this code on your local computer, install the necessary Python packages using this command:
```bash
pip install langchain langchain-groq duckduckgo-search langchain-community langchain-classic gradio

How to Run in Google Colab

Open the notebook in Google Colab.
Set up your API Key Securely:
Click on the Secrets (🔑 Key icon) tab on the left sidebar.
Add a new secret named GROQ_API_KEY.
Paste your unique Groq API key into the Value field.
Toggle the button to grant Notebook access.
Run the code cell. A Gradio web link will be generated at the bottom to view your app!
