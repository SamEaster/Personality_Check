This all started with a challenge I found on Kaggle called "Predict the Introverts from the Extroverts." It felt like a fascinating puzzle to solve. The dataset was real and messy, as data often is, with plenty of missing values that needed careful handling.

My approach involved a few key steps:

Cleaning the Data: First, I worked on thoughtfully filling in the missing gaps using various imputation techniques. It's like being a detective, trying to figure out what the data would say if it were complete.

Finding the Right Model: I experimented with different ways of combining machine learning models, a technique known as "Stacking." The idea is that by having several models work together, they can often make a more accurate prediction than any single model on its own.

A Proud Result: After a lot of tweaking and testing, I was thrilled to land on a model that achieved 96.84% accuracy, placing 12th in the competition!

Bringing the Model to Life
A model is just a file on a computer until people can actually use it. To make this project accessible to everyone, I built a simple web application.

I used Flask, a lightweight Python framework, to handle the backend logic.

The front-end is a clean and simple interface built with HTML and styled with Tailwind CSS.

Finally, I wrapped the entire application in a Docker container and deployed it on Render, so you can try it out with just a click.

If you want to check the model here is the:
https://personality-check-p5x2.onrender.com/ 
