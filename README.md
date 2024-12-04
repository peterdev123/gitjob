# 🚀 GitJob
**Your Ultimate Job Portal Connecting Job Seekers and Employers**

GitJob is a feature-rich platform designed to bridge the gap between job seekers and employers. From seamless job searching to effective communication, GitJob provides the tools necessary to streamline the hiring process.

GitJob is designed for:

- Job Seekers: Helping individuals find their dream jobs by providing advanced search tools and profile-building options.
- Employers: Simplifying talent acquisition through effective job postings and direct communication with candidates.
  
---

## ⚒️ Contributors

- [Ranz Matheu Lumayno](https://github.com/eggstink)
- [Jorash Jonathan Robillos](https://github.com/Syjhert)
- [Peter Sylvan Vecina](https://github.com/peterdev123)
  
---

## 🌟 **Features**

1. **User Registration**  
   - Create accounts as a Job Seeker or Employer.  
   - Access the rest of the platform's features with an account.

2. **Job Search**  
   - Search for jobs using keywords, filters, and sorting options.  
   - Discover relevant positions based on location, industry, or employment type.

3. **Profile Management**
   - Build a profile, change your profile picture, and showcase your skills and experiences.
   - Job Seekers: Upload resumes and track applications.  

4. **Job Posting**  
   - Employers can post, edit, and manage job listings.  
   - Include job descriptions, salary, qualifications, and more.

5. **Communication**  
   - Built-in messaging system for seamless interaction between Job Seekers and Employers.  
   - Secure and efficient exchange of application details or interview schedules.

6. **Notifications**
   - Stay informed with real-time updates on applications, messages, and job matches.
  
7. **Resume Management**  
   - Job Seekers can create, upload, and manage their resumes.  
   - Employers can view and manage received resumes efficiently.

8. **Business Manager Job Management**  
   - Business Managers can manage job postings, view applications, and oversee job-related activities.
   - Application Review and ability to accept and decline applicants

9. **Application Tracking**  
   - Employers and Job Seekers can track the status of job applications throughout the hiring process.  

---

## 💻 **Technologies Used**

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Django Auth](https://img.shields.io/badge/Django%20Auth-6A0DAD?style=for-the-badge&logo=django&logoColor=white)
![Git](https://img.shields.io/badge/Git-F34F29?style=for-the-badge&logo=git&logoColor=white)

---

## ⚙️ Dependencies

The following are the main dependencies used in this project:

| **Technology**              | **Version**  | **Description**                                    |
|------------------------------|--------------|----------------------------------------------------|
| **[Django](https://www.djangoproject.com/)** | 5.1.3        | The main web framework used for developing the application. |
| **[djangorestframework](https://www.django-rest-framework.org/)** | 3.14.0       | Used to create APIs for the application.          |
| **[SQLite](https://www.sqlite.org/)**        | N/A          | Default database used in the development environment. |
| **[PostgreSQL](https://www.postgresql.org/)**| 14+          | Database used for production.                     |
| **[HTMX](https://htmx.org/)**               | 1.9.0        | For dynamic interactions in templates.            |
| **[Daphne](https://github.com/django/daphne)** | 4.0.0       | ASGI server for WebSocket support.                |
| **[Django Channels](https://channels.readthedocs.io/)** | 4.0.0       | For handling WebSocket communication in Django.   |
| **[Gunicorn](https://gunicorn.org/)**       | 20.1.0       | A WSGI HTTP server for deployment.                |

### Prerequisites 

- Python 3.10+
- Django 5.1.3
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/peterdev123/gitjob
    cd gitjob
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows, use `venv\Scripts\activate`
    ```

3. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```bash
    python manage.py migrate
    ```
5. Run the development server:
    ```bash
    python manage.py runserver
    ```

---

## 📚 Additional Resources  

- [**Functional Requirement**](https://github.com/peterdev123/gitjob/blob/main/Functional%20Requirement%20Document.pdf)
- [**Entity Relationship Diagram**](https://github.com/peterdev123/gitjob/blob/main/Gitjob%20ERD.pdf)
- [**Prototype Design (UI/UX)**](https://github.com/peterdev123/gitjob/blob/main/GitJob%20UI.pdf)
- [**Gantt Chart**](https://github.com/peterdev123/gitjob/blob/main/Gitjob%20Gantt%20Chart.pdf)

---

## 📜 License  

This project is open-source and licensed under the **MIT License**.  
