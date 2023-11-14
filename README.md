# HTTP Request Builder

A Python application using Tkinter to create and send GET requests.

## Description

This application provides a graphical user interface for constructing simple HTTP GET requests. Users can input a base URL, add parameters with their respective values, and send the request to receive the server's response.

## Features

- Input field for the base URL
- Ability to add and delete parameters
- Send HTTP GET requests
- Display the server response

## Requirements

- Python 3.x
- requests library (`pip install requests`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/omartrj/http-get-builder.git
   cd http-request-builder
   ```
2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the application by executing the the `main.py` file:
   
```bash
python main.py
```

Once the application window opens:

- Enter the base URL in the provided field.
- Add parameters and their values by clicking the "Add Parameter" button.
- Click the "Send Request" button to send the constructed HTTP request.
- View the server response in the displayed text area.
