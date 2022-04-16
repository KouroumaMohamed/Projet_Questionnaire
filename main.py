# PROJET QUESTIONNAIRE V3 : POO

# OBJECTIF: PRATIQUER SUR LA POO
# TRAVAILLER SUR DU CODE EXISTANT
# MENER UN RAISONNEMENT

"""
Exercice 1: définir les entitées (données, actions) sous forme de commentaires
- créer la classe Questionnaire qui va contenir les données
- créer les différentes méthodes demander_reponse_numerique_utilisateur, poser_question
et lancer_questionnaire

Analyse prof:
on aura une premiere entité:   Question:
                                    - titre    -str
                                    -choix     -(str)  type tuple
                                    -bonne reponse    -str

                                    -poser_question() --> rep un bool

une deuxième entité ou class: Questionnaire
                                    - questions    -(question) type tuple

                                    -Lancer_questionnaire()
Exercice 2: créer la classe Question et tester que ça fonctionne
Exercice 3: implémenter la classe Questionnaire
"""


class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def poser(self):
        print("QUESTIONS :")
        print("  ", self.titre)
        for i in range(len(self.choix)):
            print(f"{i + 1}-", self.choix[i])
        print()
        reponse_correcte = False
        reponse_int = Question.demander_reponse_numerique_utilisateur(1, len(self.choix))
        if self.choix[reponse_int-1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            reponse_correcte = True
        else:
            print("Mauvaise réponse")

        print()
        return reponse_correcte

    def demander_reponse_numerique_utilisateur(min, max):
        reponse_str = input(f"Votre réponse (entre {min} et {max}) : ")
        try:
            rep_int = int(reponse_str)
            if min <= rep_int <= max:
                return rep_int

            print(f"ERREUR : vous devez rentrer un nombre (entre {min} et {max}). Réessayez ")
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utilisateur(min, max)


class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    def lancer_questionnaire(self):
        score = 0
        for question in self.questions:
            if question.poser():
                score += 1
        print("Score final:", score, "sur", len(self.questions))

# def lancer_questionnaire(questions):
#     score = 0
#     for question in questions:
#         if poser_question(question):
#             score += 1
#     print("Score final:", score, "sur", len(questions))


# Données
questions = (Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
             Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
             Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles"))


# lancer_questionnaire(questionnaire)

# q1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
# q1.poser()

q2 = Questionnaire(questions)
q2.lancer_questionnaire()