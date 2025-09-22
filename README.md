This all started with a challenge I found on Kaggle called "Predict the Introverts from the Extroverts." The competition was competetive as  dataset was real and messy, as data often is, with plenty of missing values that needed careful handling.

# My approach involved a few key steps:

First, I worked on filling in the missing gaps using various imputation techniques. Like KNN Imputer and Iterative Imputer.

I experimented with different ways of combining machine learning models, a technique known as "Stacking." The idea is that by having several models work together, they can often make a more accurate prediction than any single model on its own.

After a lot of tweaking and testing, I was thrilled to land on a model that achieved 96.84% accuracy, placing 12th in the competition!

# Deploying the model
After building the model it thought I should try model deploying, but as I am new to deployment I don't have much knowledge about WebDev tech stack so I choose the basic libraries like. 
Flask, a lightweight Python framework, to handle the backend logic.

I kept front-end clean and simple interface built with HTML and styled with Tailwind CSS.

Finally, I wrapped the entire application in a Docker container and deployed it on Render, so you can try it out with just a click.

If you want to check the model here is the:
https://personality-check-p5x2.onrender.com/ 
