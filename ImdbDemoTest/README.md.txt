														***IMDb Website Testing Automation Project***

This repository contains an automation testing project for the IMDb website using Selenium with Python. The project demonstrates various automation testing capabilities, including data-driven tests, cross-browser testing, and logging, while showcasing integration with PyTest and Excel file operations.

--> Features
The project includes the following test cases:

1. Fetch Single Movie Rating
	a.Retrieve the rating of a specific movie from IMDb.

2. Fetch and Update Multiple Movie Ratings

	a. Read a list of movie titles from an Excel file.
	b. Retrieve their ratings from IMDb.
	c. Store the fetched ratings back into the same Excel file.


3. Featured Today List

	a. Extract the "Featured Today" section from IMDb.
	b. Save the list in an Excel file.

4. Movies by Release Date

	a. Retrieve a list of movies based on a specified start and end release date range.



--> Technologies and Tools
The following technologies and tools were utilized:

a. Selenium WebDriver for browser automation.
b. PyTest for organizing and running test cases.
c. Logging to track execution details and errors.
d. OpenPyXL for reading from and writing to Excel files.
e. Cross-Browser Testing for ensuring compatibility across different browsers.
f. HTML Report Generation to provide detailed insights into test execution results.


--> Project Highlights
a. Data-Driven Testing: Excel-based input and output enhance reusability.
b. Cross-Browser Testing: Ensures compatibility across Chrome and Firefox.
c. Custom Logging: Provides detailed execution insights.
d. HTML Reports: Easy-to-read test execution summaries.

--> Future Enhancements
a. Adding support for headless browser testing.
b. Integration with CI/CD pipelines like Jenkins.
c. Expanding test cases to cover additional IMDb functionalities.
