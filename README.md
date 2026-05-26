# DecodeLabs-Internship

## About Repository
This repository is a storage unit of the projects I have done during the AI Internship with DecodeLabs. 

The internship consists of four projects starting from 15th of May, 2026 till the 15th of June, 2026. The projects are:  

• Simple Chatbot (General Study Helper Bot) {Date: 15/5/2026-21/5/2026}  

• Data Classification with AI (Zoo Animal Classifier) {Date: 22/5/2026-25/5/2026}  

• AI Recommendation Logic (Project Name Not Decided) {Date: 25/5/2026-Finish Date still not Specified}  

• Project Not Given Yet.  

This README will update until the finishing of the Internship.

## Project One: General Study Helper Bot
What is the General Study Helper Bot? It is a chatbot that gives automated responses on things like time management, procrastination, note-taking, etc.

The structure of the project was an IPO (Input-Process-Output) architecture which mean we had three areas to tackle:  

1. Input → What's our input? What will the user give us and what are we supposed to do with it?  #
2. Processing → How do we process this input?  
3. Output → After processing, what's the program supposed to print out?  

<span style="color:blue">Input</span>

Since this is a rule-based chatbot that's supposed to answer student's questions, our input was questions from a student. For example, 'How can I study more effectively?'  

The program simply reads the input using `input()` and stores it in a user input variable.  

<span style="color:blue">Processing</span>  

Before we discuss the processing of the input itself, we have to talk about the 'rule-based' and 'automatic responses' areas.  

The rules or the automatic responses are stored in Python Dictionaries. Why was a dictionary used, and how? Basically, a Dictionary has a time complexity of O(1) in searching compared to conditional statements like `if-elif-else` or `match-case`, hence why it was used. How did we store the responses in the dictionary? It was done as keyword-to-response where if the program searches in the student's question and finds the needed keyword, it will respond accordingly.  

Now, what if the keyword was written differently than what's stored in the dictionary? Here's where input sanitisation comes in. The program takes the input and uses `.lower()` and `.strip` to turn the whole input into lowercase, and to even remove leading and trailing blank characters.  

<span style="color:blue">Output</span>  

Now, if the keyword was found, the chatbot will print out the needed response. If the keyword was not found, it will respond with 'I don't understand'. If the keyword was 'exit', the program will stop running. That means the whole program runs in a while loop forever until the user types 'exit'.  

<span style="color:blue">Conclusion</span>  

There are some missing features in this program:  

1. If the user types two keywords, the program may mistake the intention of the user and respond differently than what's required.  
2. If the user types two keywords, the program will only respond to the first one and ignore the other.  
3. It doesn't allow for follow-up questions.  

## Project Two: Zoo Animal Classifier
