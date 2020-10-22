# ExR

Simple Expense Register.
Demo application to document and manage users expenses.

Key features:
* front-end: Single Page Application : Vue.js
* back-end: Django Rest Framework
* end-to-end CRUD implementation
* REST pagination and filtering

Set-up procedure defines following test users in the database:

UserID | Password
------------ | -------------
Eve | Pass4Eve!
Adam | Pass4Adam!

# Content:

* ToDo in the next version (areas of improement)
* Back-end development enviroment set-up
* Front-end developent enviroment set-up
* What you can expect. A couple of screenshots.
  
# ToDo in the next version (areas of improement)
## Must-do
- [ ] Witraw from dynamic Report tables refreshes on every expense add/delete/update operations (it overloads database). Add Refresh button instead.
## Good-to-do
- [ ] apply currency formatting for money values ($1,000 instead of 1000)
- [ ] more consistent button colors and styles for different windows
- [ ] input box for page entered by user from keyboard (not only selected with mouse)
- [ ] reconsider and refactor 'Expensegrid.vue'. This file became too big.
- [ ] initial "Items per Page:" selection box does not show default value. Correct.
## Potential future functionality extensions
- [ ] explicit currencies (USD, PLN, etc.)
- [ ] interface to manage cost categories  (and potencially curriencies)
- [ ] nicer visual design for "Items per Page:" "Pages:" and "Filter:" elements

# Back-end development enviroment set-up

* Step I
```
git clone https://github.com/ka-r-ol/ExR.git

cd ExR
python3 -m venv venv
source venv/bin/activate
pip install pip --upgrade
pip install -r requirements.txt
```
* Step II
```
cd server
python manage.py makemigrations
python manage.py migrate 
```

* Step III

Upload sample records to the datbase from spots/scripts/spots.csv and set-up two test users (mentioned above)
```
./load_sample_data.sh
```

### Test Django-Rest 

Run local server:
```
python manage.py runserver
```
Run tests: 
```

curl -u Eve:Pass4Eve! http://localhost:8000/api/v1/categories | python -m json.tool

curl -u Eve:Pass4Eve! http://127.0.0.1:8000/api/v1/expenses | python -m json.tool

curl -u Eve:Pass4Eve! "http://127.0.0.1:8000/api/v1/expenses?cost_max=150&cost_min=50" | python -m json.tool

```

# Front-end developent enviroment set-up

* Go to ExR directory (the one containing venv subdir)

* Make sure you are in the virutal env (source venv/bin/activated )

* Install nodes virtual env tool:
```
pip install nodeenv
```
* Concatenate nodes virutal env with python virualenv:
```
nodeenv -p
```

```
cd client
npm install
```

install following packages:
```
npm install axios
npm install vue bootstrap-vue bootstrap
npm install vuex --save
```

### Run and Test SPA

* Open chrome in development mode:
Command for mac:
```
open -n -a /Applications/Google\ Chrome.app --args --user-data-dir="/tmp/someFolderName" --disable-web-security
```
in the main project directory there is a script: start_dev_chrome.sh (MAC only).


* Start vue dev enviroment:
```
npm run dev
```

* switch to browser (chrome), log in and enjoy the application
