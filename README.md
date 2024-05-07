# Hospital Patient Management App

Welcome to the Hospital Patient Management App repository! This Django application is designed to manage patient information within a hospital setting. It allows hospital staff to efficiently organize patient records, appointments, and medical history.

## Features

- User authentication and authorization system.
- CRUD operations for patient records.
- Appointment scheduling and management.
- Medical history tracking for patients.

## Installation

To run this application locally, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/hospital-patient-management.git
    ```

2. Navigate to the project directory:

    ```bash
    cd hospital-patient-management
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply the database migrations:

    ```bash
    python manage.py migrate
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

8. Access the application in your web browser at `http://localhost:8000`.

## Containerization

This application is packaged into a Docker container for easy deployment. To build and run the container locally, make sure you have Docker installed and follow these steps:

1. Build the Docker image:

    ```bash
    docker build -t hospital-patient-management .
    ```

2. Run the Docker container:

    ```bash
    docker run -d -p 8000:8000 hospital-patient-management
    ```

3. Access the application in your web browser at `http://localhost:8000`.

## Deployment

This application is deployed on AWS EC2 using GitHub Actions. Whenever changes are pushed to the `main` branch, GitHub Actions automatically builds the Docker image, pushes it to Docker Hub, and deploys it on the EC2 instance.

To set up deployment on your own AWS EC2 instance, follow these general steps:

1. Provision an EC2 instance and configure security groups and key pairs.

2. Install Docker and Docker Compose on the EC2 instance.

3. Set up a GitHub Actions workflow to automate the deployment process.

4. Configure environment variables for sensitive information such as database credentials and secret keys.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Make sure to follow the [contributing guidelines](CONTRIBUTING.md).


