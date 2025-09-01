# Healthcare-Backend
- Basic django framework project stucture
- Django rest framework for restapi
- jwt tokens for auth
- validations
- .env

## Project Setup
```
git clone https://github.com/harshrathore2303/HealthcareBackend.git
cd HealthcareBackend
python -m venv .venv
source venv/bin/activate
pip install -r requirements.txt
```
After this create a database in pgadmin then update .env file which is give below and run 
```
python manage.py migrate
python manage.py createsuperuser <!-- This is to create admin so remember credentials to see updates from web browser -->
python manage.py runserver
```

* .env should be in ./healthcarebackend
```
SECRET_KEY=yoursecretkey
DB_NAME=database_name
DB_USER=database_user
DB_PASSWORD=database_pw
DB_HOST=localhost <!-- for my local machine  -->
DB_PORT=5432  <!-- port number according to your database or pgadmin -->
```

## 1. Authentication APIs
- Live API: [https://healthcare-backend-gefb.onrender.com](https://healthcare-backend-gefb.onrender.com)
- This API has been deployed on render go and checkout these end points.
- **POST** `/api/auth/register/`  
  Register a new user with name, email, and password.

- **POST** `/api/auth/login/`  
  Log in a user and return a JWT token.

---

## 2. Patient Management APIs

- **POST** `/api/patients/`  
  Add a new patient (Authenticated users only).

- **GET** `/api/patients/`  
  Retrieve all patients created by the authenticated user.

- **GET** `/api/patients/<id>/`  
  Get details of a specific patient.

- **PUT** `/api/patients/<id>/`  
  Update patient details.

- **DELETE** `/api/patients/<id>/`  
  Delete a patient record.

---

## 3. Doctor Management APIs

- **POST** `/api/doctors/`  
  Add a new doctor (Authenticated users only).

- **GET** `/api/doctors/`  
  Retrieve all doctors.

- **GET** `/api/doctors/<id>/`  
  Get details of a specific doctor.

- **PUT** `/api/doctors/<id>/`  
  Update doctor details.

- **DELETE** `/api/doctors/<id>/`  
  Delete a doctor record.

---

## 4. Patient-Doctor Mapping APIs

- **POST** `/api/mappings/`  
  Assign a doctor to a patient.

- **GET** `/api/mappings/`  
  Retrieve all patient-doctor mappings.

- **GET** `/api/mappings/<patient_id>/`  
  Get all doctors assigned to a specific patient.

- **DELETE** `/api/mappings/<id>/`  
  Remove a doctor from a patient.

## Working Images
![Backend](structure.png)
![Tables](tables.png)
