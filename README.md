Navigate to the projectt repo
cd your-repo

Create a virtual environment (optional but recommended):
python3 -m venv env

Activate the virtual environment:
On Windows:
.\env\Scripts\activate
On macOS and Linux:
source env/bin/activate

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Run the development server:
python manage.py runserver

Admin URLs:

/admin/: Django admin interface.
App URLs:

/: Includes URLs from the myapp.urls module.
/upload/: URL for uploading files.
/query-count/: URL for querying the count of records (API endpoint).
/query/: URL for querying data.
/users/: URL for listing users.
Accounts URLs (Django Allauth):

/accounts/: Includes authentication URLs provided by Django Allauth.
/accounts/login/: URL for login page.
/accounts/logout/: URL for logout page.
/accounts/signup/: URL for signup page.
/accounts/password/change/: URL for changing password.
/accounts/password/set/: URL for setting password.
/accounts/password/reset/: URL for resetting password.
/accounts/email/: URL for managing email.
/accounts/confirm-email/: URL for confirming email.
API URLs:

/api/: Includes API URLs from the myapp.api_urls module.
/api/query-count/: URL for querying the count of records (API endpoint).

Keyword: "technology"
Industry: "Information Technology"
Year Founded: 2005
City: "San Francisco"
State: "California"
Country: "United States"
Employees (From): 100
Employees (To): 1000
