# Quiz Game
1.create venv ->  python -m venv venv
2.activate venv ->  venv\Scripts\activate
3.install requirements -> pip install -r requirements.txt 


Initialize Flask-Migrate:
    ?4.flask db init()    (not necessary)
Create an initial migration:
    ?5.flask db migrate -m "Initial migration" (not necessary)
Apply the migration to the database:
    flask db upgrade
---
Whenever you make changes to your database models, generate a new migration:
    flask db migrate -m "Description of changes"
Apply the new migration:
    flask db upgrade
---
By following these steps, you can easily manage database migrations in your Flask application using SQLAlchemy and Flask-Migrate.

6.flask run or python ./run.py


## Project Overview:
The Quiz Game is a web application that allows users to test their knowledge in various subjects through multiple-choice questions. The purpose of the project is to provide an interactive and engaging platform for users to challenge themselves and learn new information. The goal is to create an enjoyable and educational experience for users while promoting knowledge retention and improvement.

## Features and Functionality:
- User Registration and Login: Users can create an account and log in to access the quiz game.
- Multiple-choice Questions: The application presents users with a series of multiple-choice questions from different subjects.
- Score Tracking: The application keeps track of the user's score as they answer questions.
- Leaderboard: Users can view the top scores of other players on the leaderboard.
- Interactive User Interface: The application provides a user-friendly interface with intuitive navigation and visually appealing design.

## Technologies Used:
- HTML
- CSS
- JavaScript
- Python
- Flask (Python web framework)
- MySQL (Database)
- SQLAlchemy (Python SQL toolkit and Object-Relational Mapping)

## Screenshots, Demo Or FlowCharts:
[FlowChart](https://lucid.app/lucidchart/e84b8632-8efd-485a-a98d-5ef0178719dc/edit?viewport_loc=-976%2C-60%2C3601%2C1601%2C0_0&invitationId=inv_f44c8728-b121-44a3-8b43-52883079d562)
[Low-fidelity-design](https://drive.google.com/file/d/1Ilx1929hj45wX6d95ELt9l3Tr58mNSFy/view?usp=sharing)

[Link to Live Demo](https://www.example.com)

## Roadmap and Future Enhancements:
- Implement a timer for each question to add a time constraint.
- Add more subjects and questions to expand the quiz database.
- Introduce different difficulty levels for questions.
- Implement a feature to allow users to create and share their own quizzes.
- Enhance the leaderboard with additional statistics and filters.

## Contact Information:
For any questions or feedback, please feel free to reach out to the project maintainer:
- Name: [Abel Bekele Meaza]
- Email: [abelbeworking245@gmail.com]
- GitHub: [https://www.github.com/switch247]
- LinkedIn: [Your LinkedIn Profile]
