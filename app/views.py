import os
from flask import render_template, jsonify, request, json

from app import app

@app.route('/')
def index():
    return render_template('index.html', departments=departments)

@app.route('/department/<dept>')
def department(dept):
    return render_template('department.html', department=departments[dept])

@app.route('/search', methods=['POST'])
def search():
    query = request.json['query']
    res = list(map(lambda x: x.__repr__(),
                   filter(lambda d: d.search(query), department_list)))
    return jsonify(res)

class Department:
    def __init__(self, name, data):
        # TODO
        #, description, contact)
        self.name = name
        self.stemmed_name = stemmer(name)

        self.email = data['email']
        self.contact_name = data['name']
        self.notes = data['notes']
        self.url = data['url']

        self.stemmed_email = stemmer(self.email)
        self.stemmed_contact_name = stemmer(self.contact_name)
        self.stemmed_notes = stemmer(self.notes)

    @property
    def localurl(self):
        return "/department/%s" % self.name

    def search(self, query):
        query = stemmer(query)
        if query in self.stemmed_name:
            return True
        else:
            return False

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def stemmer(string):
    return string.lower()

def get_contacts():
    root = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(root, 'static', 'contacts.json')
    with open(json_url) as f:
        return json.load(f)['contacts']['San Francisco']

contacts = get_contacts()
departments = dict((k, Department(k, v)) for k, v in contacts.items())
department_list = departments.values()
