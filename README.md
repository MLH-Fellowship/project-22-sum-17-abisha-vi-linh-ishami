# Production Engineering - Week 1 - Portfolio Site

A portfolio website that has sections to display basic information, experiences, education, hobbies, and contact info.

## Visuals
<img width="500" alt="Screen Shot 2022-06-05 at 9 17 48 PM" src="https://user-images.githubusercontent.com/81380688/172093992-a66cdcca-c806-4b8e-977b-bce52c8cbd98.png">

<img width="500" alt="Screen Shot 2022-06-05 at 9 18 27 PM" src="https://user-images.githubusercontent.com/81380688/172094046-96e23942-8fc1-48fa-a2ae-16e8e8393705.png">

## Technologies Used
- HTML & CSS for the frontend
- Python, Flask, & Jinja to make use of reusable templates and route to different URLs

## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
