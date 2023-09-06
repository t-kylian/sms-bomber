# OqTepa Spammer

<p align='right'>
  <img align="right" src='https://github.com/temurbeksamijonov/sms-bomber/assets/131855957/c0c13c05-494e-41a8-bc7a-a6701557f8fc'>
</p>

OqTepa Spammer is a Python application built with PyQt5 that allows you to send multiple spam SMS messages to a given phone number using the OqTepa API. It utilizes multithreading to send messages concurrently, improving the efficiency of the spamming process.

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Python 3.x
- PyQt5
- requests
- fake_useragent

You can install these dependencies using the following command:

```
pip install PyQt5 requests fake_useragent
```

## Getting Started

To get started with the OqTepa Spammer, follow the steps below:

1. Clone the repository or download the code files.
2. Install the required dependencies as mentioned in the Prerequisites section.
3. Open a terminal or command prompt and navigate to the directory where the code is located.
4. Run the following command to start the application:

   ```
   python <filename>.py
   ```

   Replace `<filename>` with the name of the Python file containing the code.

## Usage

Upon launching the OqTepa Spammer application, you will see a window with the following components:

- Phone Number: Enter the phone number to which you want to send spam SMS messages.
- Number of Threads: Specify the number of threads (concurrent tasks) to be used for spamming. Each thread will send spam messages independently.
- Spam Button: Click this button to start the spamming process.
- Log: Displays the logs of the spamming process, including the response received from the API.

To send spam SMS messages:

1. Enter the phone number in the "Phone Number" input field.
2. Optionally, adjust the "Number of Threads" input field to specify the concurrency level.
3. Click the "Spam" button to initiate the spamming process.
4. The application will create the specified number of threads and start sending spam messages to the provided phone number concurrently.
5. The logs of the spamming process will be displayed in the "Log" section of the application window.

Please note that the OqTepa API requires a valid token for authentication. The application retrieves the token automatically using predefined credentials. Ensure that you have a stable internet connection for successful API communication.

## Terminating the Application

To terminate the application, you can either click the close button on the window or use the standard close mechanism of your operating system. The application will gracefully shut down, stopping all active threads and releasing system resources.

## Contributing

Contributions to the OqTepa Spammer application are welcome. If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.

## License

This project is licensed under the [Apache License 2.0](LICENSE). You are free to modify, distribute, and use the code in compliance with the terms and conditions of the Apache License 2.0. See the [LICENSE](LICENSE) file for more details.
