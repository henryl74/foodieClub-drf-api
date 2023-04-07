# Testing  

## Methodology  
Testing was done throughout the process while developing the project by the use of Django debug pages. In addition all code has been validated with different online tools as presented below.

* ## Python Validation

    * All Python code was validated using [CI Python Linter](https://pep8ci.herokuapp.com/) found no errors or warnings except in the settings.py file lines too long which was related to built-in Django code.

`settings.py`

![CI Python Linter](./readme-testing-images/drf_api_settings_python_validator.png)

* ## Automated Testings
    * Unit testings was performed in `posts` app.

#### **PostListView Testcase**

![Post list view testcase](./readme-testing-images/post_list_view_tests.png)

#### **PostDetailView Testcase**

![Post details view testcase](./readme-testing-images/post_detail_view_tests.png)

#### **Results from the testing**

![Result from Post testcase](./readme-testing-images/post_tests_results.png)

## Bugs Fixed

Document bugs here

* ## Manual Testing

    * In addition to the other tests, I have conducted a manual check list for myself to carry out to make sure that everything is working as intended.

| Status | **Navigation Bar Logged Out**
|:-------:|:--------|
| &check; | Clicking the navbar logo loads the home page
| &check; | That the navbar shows the tabs Home, Menu, Reservation, Register, Login
| &check; | Clicking the Home tab on the navbar loads the home page
| &check; | Clicking the Menu tab on the navbar loads the menu page
| &check; | Clicking the Reservation tab on the navbar loads the reservation page
| &check; | Clicking the Login tab on the navbar loads the login page

| Status | **Navigation Bar - User Logged In**
|:-------:|:--------|
| &check; | That the navbar shows the username of the logged in user
| &check; | Clicking the navbar logo loads the home page
| &check; | That the navbar shows the tabs Home, Menu, Reservation, My Bookings, Logout if the user is logged in
| &check; | Clicking the Home tab on the navbar loads the home page
| &check; | Clicking the Reservation tab on the navbar loads the Book a Table page
| &check; | Clicking the My Bookings tab on the navbar loads the user's bookings made page
| &check; | Clicking the Logout tab on the navbar loads the logout page
| &check; | That the Logout button once clicked displays a logout message


| Status | **Navigation Bar - Admin (superuser) User Logged In**
|:-------:|:--------|
| &check; | Clicking the navbar Django adminitration logo loads the home page
| &check; | That the navbar displays a welcome message, tabs to View Site, Change Password, Log Out
| &check; | That the navbar shows the username of the logged in user
| &check; | Clicking the Accounts tab on the admin panel loads the Email addresses
| &check; | Clicking the Email Addresses tab, it will load the user emails registered
| &check; | Clicking the Restaurant tab on the admin panel loads the bookings tab
| &check; | Clicking the Booking tab, it will list all the existing reservations that have been made
| &check; | Clicking the Add Booking, allows the admin user to add a booking to an specific user
| &check; | Clicking on an existing Booking, allows the admin user to delete or update that reservation

| Status | **Footer - User Logged Out/In**
|:-------:|:--------|
| &check; | That the Footer displays the Opening Hours, Contact Details, and Social Media icons
| &check; | Clicking the Facebook icon loads the instagram home page in a new tab
| &check; | Clicking the Instagram icon loads the facebook home page in a new tab
| &check; | Clicking the TikTok icon loads the twitter home page in a new tab