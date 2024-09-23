<a id="readme-top"></a>

<h1 align='center'>JobZila | Job Search Application :briefcase:</h1>

<div align='center'>

<img src='/assets/images/main_readme.png' alt='Home page of JobZila'>
Welcome to JobZila, a Django-based job search application where users can search for job listings based on keywords, location, and category. This project was built as a demonstration of how to create a fully functional job search engine using Django's framework.

<br /> Are you ready to be inspired?

<a href='https://github.com/AmberForrester/Django/tree/main/jobzila/jobzila'><strong>Source Code »</strong></a>
<br />
</div>



<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#features">Features</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>
<br />



## Features
- Search for job listings by **keywords**, **location**, and **category**.
- Dynamic job listings fetched from a JSON file or Django Admin.
- Simple and intuitive UI to help users find their dream jobs.
- Ability to manage job listings via Django Admin.

<p align="right">(<a href="#readme-top">top of page</a>)</p>



## Installation

### Prerequisites
- Python 3.x
- Django 4.x (or latest)
- Virtual Environment (optional but recommended)



### Step-by-Step Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/jobzila.git
   cd jobzila
   ```

2. **Set up a Virtual Environment**(Optional but recommended)
    ```bash
    python -m venv .venv
    .\.venv\Scripts\Activate
    ```

3. **Install Required Dependencies** Navigate to the project directory and install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations to Set Up the Database** Run the following commands to set up the database:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a Superuser to Access the Django Admin**
    ```bash
    python manage.py createsuperuser
    Hit [Enter] after each prompt below:
    Username:
    Email Address:
    Password: (not visible)
    Password(again): (not visible)
    R/T to Test Environment Bypass Password Validation and create user anyway? [y/N]: y
    ```

6. **Run the Django Development Server** Start the server to view the project in your browser:
    ```bash
    pythong manage.py runserver
    ```

7. **Visit the Application** Open your browser and visit:
    - **Application**: `http://127.0.0.1:8000/`
    - **Django Admin**: `http://127.0.0.1:8000/admin`

<p align="right">(<a href="#readme-top">top of page</a>)</p>



## Usage

### Managing Job Listings via Django Admin

1. **Login** to the Django Admin interface(`http://127.0.0.1:8000/admin/`).

2. **Add Job Listings** manually or use a JSON file to bulk import jobs.

### Importing Job Listings from JSON

To bulk import job listings from a JSON file, follow these steps:
1. **Create the JSON File** (e.g., joblistings.json):
    ```
    [{
    "title": "Front-end Developer",
    "company": "ABC Company",
    "location": "Toronto, ON",
    "description": "We are seeking a talented Front-end Developer...",
    "apply_link": "https://example.com/apply"
        }]   // Add more jobs...  
    ```

2. **Run the Import Command:** Place the JSON file in the project root directory and run:
    ```bash
    python manage.py import_jobs
    ```
<p align="right">(<a href="#readme-top">top of page</a>)</p>



## Project Structure

![Project Structure](/assets/images/project_struct.png)

<p align="right">(<a href="#readme-top">top of page</a>)</p>



## Contributing

I have learned that contributions are the heart of what makes the open source community such an amazing place! We are constantly able to learn, grow, inspire eachother, and create incredible things. Any contributions you make are **greatly appreciated**, we are so lucky to be here together.

If you have a suggestion that would make this project better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please, don't forget to give the project a :star:! 

I appreciate you!

<p align="right">(<a href="#readme-top">top of page</a>)</p>



## License

Distributed under the MIT License. See `License.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>