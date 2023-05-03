- clone this repository
- cd into the root
- `python -m venv env` (Python 3.x is requried)
- `env\Scripts\activate`
- `pip install -r requirements.txt` (pip for Python 3.x is requried)
- `cd website`
- `python manage.py runserver`
- In browser open http://127.0.0.1:8000/docs/
- Set some ID (22 in this case) and press "Enter"
- Should be redirected to http://127.0.0.1:8000/docs/22/edit
- Open 2 more browser tabs with url http://127.0.0.1:8000/docs/22/view
- In http://127.0.0.1:8000/docs/22/edit write something in 2 inputs and press "Send"
- All Tabs should get the message
- Open straight another Tab http://127.0.0.1:8000/docs/33/edit
- Open 2 more browser tabs with url http://127.0.0.1:8000/docs/33/view
- All Tabs with ID 33 should get the new message and its not sending to tabs with ID 22


## Note

#### This does not reflect a good and production ready code:

- I did not care about front end tech in this case and did it in pure javascript, because it feels an overkill to add React or similar for such tiny functionality.
- No CSS, public assets, etc.
- I did not care about handling errors or making front end user friendly or nice.
- Did not comment the code properly
- Could go on and one here, but hope I made a point. 
