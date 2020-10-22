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
- [ ] explicit currencies (USD, PLNs)
- [ ] interface to manage cost categories
- 

npm install vue bootstrap-vue bootstrap
npm install vue-router
npm install vuex --save