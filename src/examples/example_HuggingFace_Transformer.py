from transformers import pipeline

# Trasformer Model Inference
# This example demonstrates how to use the Hugging Face Transformers library for model inference.

# Sentiment Analysis
# This example demonstrates how to use the Hugging Face Transformers library for sentiment analysis.
# It loads a pre-trained sentiment analysis model and uses it to analyze the sentiment of a given text.

classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
prediction = classifier("The HuggingFace course is amazing!")
print(prediction)

classifier = pipeline("sentiment-analysis", model="oliverguhr/german-sentiment-bert")
prediction = classifier("Der HuggingFace-Kurs ist fantastisch!")
print(prediction)

# Zero-Shot Classification
# This example demonstrates how to use the Hugging Face Transformers library for zero-shot classification.

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
prediction = classifier(
    "This is a course about the Transformers library",
    candidate_labels=["education", "politics", "business"]
)
print(prediction)