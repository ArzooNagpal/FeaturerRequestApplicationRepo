# from App package importing flask variable app
from App import app
# from flask import render_template() to render a template 
from flask import render_template
# On flask app run whenever the browser requests for the URL 'http://127.0.0.1:5000/, the function defined renders form.html
@app.route('/featureRequestForm')
def featureRequestForm():
    return render_template('featureRequestForm.html')
# On flask app run whenever the browser requests for the URL 'http://127.0.0.1:5000/table, the function defined renders table.html
@app.route('/featureRequestDetails')
def featureRequestDetails():
    return render_template('featureRequestDetails.html')


