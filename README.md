# DecodeLabs-Internship

## About Repository
This repository is a storage unit of the projects I have done during the AI Internship with DecodeLabs. 

The internship consists of four projects starting from 15th of May, 2026 till the 15th of June, 2026. The projects are:  

• Simple Chatbot (General Study Helper Bot) {Date: 15/5/2026-21/5/2026}  

• Data Classification with AI (Zoo Animal Classifier) {Date: 22/5/2026-25/5/2026}  

• AI Recommendation Logic (Project Name Not Decided) {Date: 25/5/2026-Finish Date still not Specified}  

• Project Not Given Yet.  

This README will update until the finishing of the Internship.

## General Study Helper Bot

A simple rule-based chatbot that provides students with automated tips on time management, procrastination, note-taking, exam stress, and studying strategies.

Project by Jomana Shaltout — DecodeLabs Project 1

#### About

The General Study Helper Bot is a lightweight Python chatbot that reads a student’s question or phrase and replies with a prewritten helpful message. It demonstrates an IPO (Input–Process–Output) architecture and uses a dictionary of keyword-to-response mappings to produce quick automated responses. The program is intended as a learning project to explore basic chatbot design, text sanitization, and rule-based intent matching.

#### Features  

- Continuous loop to interact with the user until they type exit.  

- Keyword-based intent matching (stored in a Python dictionary) for fast lookups.  

- Input sanitization: trimming whitespace and lowercasing for robust matching.  

- Seven initial intents covered: hello, studying effectively, exam stress, time management, note taking, procrastination, bye.  

- Fallback reply (“I don’t understand”) for unrecognized inputs.  

- Greeting message on startup and clean termination.

#### Architecture (IPO)

Input: User enters a phrase or question (e.g., "How can I study more effectively?") via input().

Process: The program sanitizes the string (.strip() and .lower()), then scans for keywords using the in operator and a dictionary of keyword-to-response pairs.

Output: If a keyword is matched, the bot prints the corresponding response. If none match, it prints a fallback message. Typing exit ends the loop and closes the program.

#### Why a dictionary?

Dictionaries provide average O(1) lookup time and keep the mapping between keywords and responses compact and easy to manage. This is simpler and faster than long chains of conditional statements for the scale of this project.

#### Limitations and Known Issues  

- Exact keyword matching: the bot only recognizes stored keywords and will not handle synonyms or misspellings.  

- Single-keyword handling: if a user input contains multiple keywords, the bot currently responds to the first detected keyword and ignores others.  

- No follow-up or context handling: conversation history and multi-turn clarifications are not supported.  

- No empty-input handling or input length checks.  

- Limited topic coverage (only 7 intents initially).

#### Suggested improvements  

- Implement basic stemming/lemmatization to handle synonyms and misspellings.  

- Support multi-intent inputs (aggregate relevant responses or prompt for clarification).  

- Add a simple state manager to support follow-up questions and short multi-turn dialogs.  

- Expand intent coverage and make responses modular.

## Zoo Animal Classifier

A small supervised ML project that classifies zoo animals into seven groups (Mammals, Birds, Reptiles, Fish, Amphibians, Bugs, Invertebrates) using a K-Nearest Neighbors classifier.

Project by Jomana Shaltout — DecodeLabs Project 2

#### Summary

This demonstrates an end-to-end machine learning workflow on the Zoo Animal Classification dataset (101 animals, 16 features). The pipeline covers data loading, basic exploration, preprocessing (scaling), training a KNN classifier, evaluation (confusion matrix, F1-score), and visualization.

#### Dataset

Source: Zoo Animal Classification (UCI / Kaggle).

Files: zoo.csv (features) and class.csv (labels) — included in the repo or linked.

Features include: animal_name, hair, feathers, eggs, milk, airborne, aquatic, predator, toothed, backbone, breathes, venomous, fins, tail, domestic, legs, class_type.

Size: 101 samples across 7 classes.

#### How it works

Load and inspect data (shape, data types, class distribution).

Prepare features and labels, drop non-predictive columns (e.g., animal_name).

Split data: 80% train / 20% test, shuffled and stratified.

Scale numeric features with StandardScaler to normalize ranges for KNN.

Train KNeighborsClassifier and predict on test set.

Evaluate using confusion matrix and F1-score.

Visualize class distribution and confusion matrix.

#### Results and visuals

Class distribution bar chart (counts per class).

Confusion matrix heatmap comparing true vs predicted labels.

Reported metrics: accuracy and macro F1. In this project’s run, only one test sample was misclassified.

#### Limitations

Small dataset (101 samples) — limited generalization.

Some features (e.g., catsize) need clarification or cleaning.

No model comparison or hyperparameter tuning beyond basic setup.

#### Recommended improvements

Compare KNN to other classifiers.

Clean ambiguous features and clearly document feature meanings.

#### References

Dataset: https://www.kaggle.com/datasets/uciml/zoo-animal-classification/data

