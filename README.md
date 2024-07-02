# University Web Design

Welcome to the official website of St Jude Chaplaincy at Karatina University. This project is designed to provide information about the chaplaincy's activities, events, and resources for the university community.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [HTML Template](#html-template)
- [Contact](#contact)

## Introduction

The St Jude Chaplaincy website is designed to cultivate the Christian faith within the university community. The site provides information on various activities, events, and resources available to students and staff.

## Features

- **Welcome Section**: A warm welcome message displayed with a marquee.
- **Navigation Bar**: Links to important pages such as Home, About, St Jude Songs, Catholic Songs, Gallery, Departments, Announcements, Daily Reading and Homily, Register, and Login.
- **Activities Section**: Information about the chaplaincy's activities including Prayers, Charity, and Eucharistic Mass.
- **Responsive Design**: Ensures the website looks good on various devices.
- **User Authentication**: Users can register, log in, and log out.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/georgeklangat/Personal-website.git
2. **Navigate to the project directory**:
      cd Personal-website
3. **Ensure you have Django installed**:
   ```sh
      pip install django
4. **Run the Django server**:
   ```sh
      python manage.py runserver
## Project Structure
   Personal-website/
   ├── stjude_web/
   │   ├── static/
   │   │   ├── stjude_web/
   │   │   │   ├── styles/
   │   │   │   │   └── STJUDEstyles.css
   │   │   │   └── images/
   │   │   │       ├── karu logo.png
   │   │   │       └── st jude logo.png
   │   ├── templates/
   │   │   └── stjude_web/
   │   │       └── STJUDE_WEB.html
   │   ├── views.py
   │   ├── models.py
   │   ├── urls.py
   ├── manage.py
   └── README.md
   ## HTML Template
      {% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta content="IE=edge" http-equiv="X-UA-Compatible">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <title>UNIVERSITY WEB DESIGN</title>

    <link href="{% static 'stjude_web/styles/STJUDEstyles.css' %}" rel="stylesheet">
</head>
<body>

<section class="header">
    <marquee behavior="scroll" bgcolor="black" direction="" height="500%" loop="" scrollamount="10" stop()
             style="color: aliceblue;"
             width="100%"><h1>Welcome To St Jude Chaplaincy</h1></marquee>
    <nav>
        <a href="STJUDEWEB.html"><img src="{% static 'stjude_web/images/karu logo.png' %}"></a>
        <div class="nav-links">
            <ul>
                <li><a href="{% url 'login' %}">HOME</a></li>
                <li><a href="https://web.facebook.com/StJudeKarU/about">ABOUT</a></li>
                <li><a href="https://www.youtube.com/@stjudecatholicchaplaincyka6673/videos">ST JUDE SONGS</a></li>
                <li><a href="https://tubidy.mobi/search.php?q=catholic+church+songs">CATHOLIC SONGS</a></li>
                <li><a href="">GALLERY</a></li>
                <li><a href="https://63ee26ab5ba9d.site123.me/">DEPARTMENTS</a></li>
                <li><a href="">ANOUNCEMENT</a></li>
                <li><a href="https://catholic-daily-reflections.com/daily-reflections/">DAILY READING AND HOMILY</a></li>
                <li><a href="{% url 'register' %}">REGISTER</a></li>
                <li><a href="{% url 'login' %}">LOGIN</a></li>
            </ul>
        </div>
        <a href="STJUDEWEB.html"><img alt="" src="{% static 'stjude_web/images/st jude logo.png' %}"></a>
    </nav>

   <div class="text-box">
        <h1 title="This is the church where we cultivate the christian faith">St Jude Chaplaincy Karatina
            University</h1>
        <h3 style="color: burlywood;">We Cultivate The Christian Faith</h3>
        <br>
        <br>
        <br>
    </div>
</section>

<section class="Activities">
    <h1>Activities in the Chaplaincy</h1>
    <p>St Jude Chaplaincy engages all Christians in strengthening the Faith through prayers, charity, socialization,
        and Holy Mass</p>

   <div class="row">
        <div class="Activities-col">
            <h3>Prayers</h3>
            <p>The small Christian community takes place every Monday
                and Wednesday, where the students meet to pray Rosary, novenas, and other prayers.</p>
        </div>

   <div class="Activities-col">
            <h3>Charity</h3>
            <p>The Chaplaincy takes part in helping needy students through the student-student initiative, and
                through the SCC, students get in touch with each other as a family.</p>
        </div>

   <div class="Activities-col">
            <h3>Eucharistic Mass</h3>
            <p>The Chaplaincy holds Holy Eucharistic Mass during the week and every Sunday.</p>
        </div>
    </div>
</section>

<script>
</script>
</body>
</html>
## Contributing
Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, please create an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## Contact
For any inquiries or questions, please contact George Klangat at georgeklangat@gmail.com





