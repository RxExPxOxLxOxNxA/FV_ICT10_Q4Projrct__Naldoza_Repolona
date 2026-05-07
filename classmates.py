from js import document

# Class
class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hi, I am {self.name} from {self.section}. My favorite subject is {self.favorite_subject}."

# Default classmates
classmates = [
    Classmate("Al Hazmi", "10-Ruby", "ICT"),
    Classmate("Bernas", "10-Ruby", "Science"),
    Classmate("Alvarez", "10-Ruby", "Math"),
    Classmate("Calaycay", "10-Ruby", "English"),
    Classmate("Cruz", "10-Ruby", "Arts"),
    Classmate("Defensor", "10-Ruby", "P.E."),
    Classmate("Francisco", "10-Ruby", "ICT"),
    Classmate("Dimasuhid", "10-Ruby", "Science"),
    Classmate("Juatchon", "10-Ruby", "Math"),
    Classmate("Lilagan", "10-Ruby", "English"),
    Classmate("Luna", "10-Ruby", "Math"),
    Classmate("Macaranas", "10-Ruby", "ICT"),
    Classmate("Mondragon", "10-Ruby", "Arts"),
    Classmate("Naldoza", "10-Ruby", "Science"),
    Classmate("Ng", "10-Ruby", "Math"),
    Classmate("Natividad", "10-Ruby", "ICT"),
    Classmate("Paz", "10-Ruby", "English"),
    Classmate("Ong", "10-Ruby", "Science"),
    Classmate("Ramos M.", "10-Ruby", "Math"),
    Classmate("Ramos Q.", "10-Ruby", "Arts"),
    Classmate("Ramos S.", "10-Ruby", "ICT"),
    Classmate("Reodica", "10-Ruby", "Science"),
    Classmate("Repolona", "10-Ruby", "Math"),
    Classmate("Belsa", "10-Ruby", "English"),
    Classmate("Hsu", "10-Ruby", "ICT"),
    Classmate("Castelo", "10-Ruby", "Science"),
    Classmate("Judge", "10-Ruby", "Arts"),
    Classmate("Mateo", "10-Ruby", "Math"),
]

# ADD FUNCTION
def add_classmate(event):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value
    classmates.append(Classmate(name, section, subject))
    document.getElementById("output").innerText = "Classmate added!"

# SHOW FUNCTION
def show_classmates(event):
    output = document.getElementById("output")
    text = "<h3>Classmate List:</h3>"
    for c in classmates:
        text += f"<div>{c.introduce()}</div>"
    output.innerHTML = text
