from flask import render_template, jsonify, request

from app import app

@app.route('/')
def index():
    return render_template('index.html', departments=departments)

@app.route('/department/<dept>')
def department(dept):
    return render_template('department.html', department=dept)

@app.route('/search', methods=['POST'])
def search():
    query = request.json['query']
    res = list(map(lambda x: x.__repr__(),
                   filter(lambda d: d.search(query), departments)))
    return jsonify(res)

class Department:
    def __init__(self, name):
        # TODO
        #, description, contact)
        self.name = name
        self.stemmed_name = stemmer(name)
        """TODO
        self.description = description
        self.contact = contact
        self.stemmed_description = stemmer(description)
        self.stemmed_contact = 
        """
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

departments = [Department(d) for d in ['water', 'trash', 'cops']]
