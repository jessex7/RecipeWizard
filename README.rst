**Recipe Wizard**

A playground app to learn more about various technologies in the python ecosystem. Should help meal planning, grocery list generation, and recipe management.

Things to do:

- [x] Build out basic endpoints to create, read, update, and delete recipes
- [x] Complete first rev of frontend views for above functionality
- [x] Write "happy" tests for basic endpoints
- [ ] Write "happy" tests for basic frontend views
- [x] Make the frontend views less horrifically ugly - probs incorporate css framework

   - [x] Main/index page 
   - [x] Edit page -- make delete form a little trashcan icon and move it to index page
   - [x] Create page

- [ ] Add logging to existing codebase
- [ ] Incorporate an authentication & authorization solution
- [ ] Prototype a noSQL implementation
- [ ] Choose noSQL or sqlalchemy

   - [ ] if sqlalchemy is chosen, write logic that efficiently compares an object with a submitted updated object

- [ ] CAPABILITY | Search for recipe by ingredient(s), rating, name
- [ ] Think through best way to allow recipe organization (e.g. cuisine, "cookbooks", generic tags, etc.)
- [ ] CAPABILITY | Plan meals - assignment of recipes to specific days 

   - [ ] Implement a calendar view w/ an ability to allocate recipes to days
   - [ ] Update backend models to include a meal_plan structure

- [ ] CAPABILITY | Export grocery list based on meal plan
- [x] Mature model for ingredients. That should be a list, not long strings with comma separation 
- [ ] Deployable as docker container
- [ ] Deploy to AWS, google cloud, or linode
- [ ] Integrate terraform
- [ ] Do a quick analysis of website against OWASP top 10 vulnerabilities 



