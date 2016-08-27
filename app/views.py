import os
from flask import render_template, jsonify, request, json, abort

from app import app

@app.route('/')
def index():
    return render_template('index.html', departments=departments)

@app.route('/email-template')
def email_template():
    return render_template('email-template.html')

@app.route('/department/<dept>')
def department(dept):
    department = departments.get(dept)
    if department is None:
        abort(404)
    return render_template('department.html', department=department, email_body=email_body)

@app.route('/search', methods=['POST'])
def search():
    query = request.json['query']
    res = list(map(lambda x: x.__repr__(),
                   filter(lambda d: d.search(query), department_list)))
    return jsonify(res)

class Department:
    def __init__(self, name, data):
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

email_body = """
[Date of Request]%0D%0A
Dear [Contact],%0D%0A
%0D%0A
%0D%0A
Under the California Public Records Act § 6250 et seq., and
San Francisco Municipal Code Chapter 67 et seq. (“Sunshine
Ordinance”), I request access to and copies of the following
information in electronic, searchable/sortable format, where applicable.
%0D%0A
%0D%0A
[Outline of the information requested, including dates where applicable.]
%0D%0A
%0D%0A
I’d be happy to discuss my request to figure out what would be the easiest
or best way to provide the requested data. If there are any fees, I
respectfully ask that you notify me if costs exceed $25.
%0D%0A
%0D%0A
If my request is denied in whole or part, I ask that you justify all
deletions by reference to specific exemptions of the law. I will also
expect you to release all segregable portions of otherwise exempt
material. I reserve the right to appeal your decision to withhold any
information or deny a waiver of fees.
%0D%0A
%0D%0A
Please contact me by email if you have any questions about this request. I
expect a response within 10 business days of this filing, as is required by
state law. Thank you for your assistance.
%0D%0A
%0D%0A
Sincerely,%0D%0A
[Name]
"""

contacts = get_contacts()
departments = dict((k, Department(k, v)) for k, v in contacts.items())
department_list = departments.values()
