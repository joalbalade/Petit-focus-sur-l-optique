# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 23:14:04 2022

@author: joris
"""

from questions import question

questions_reponses = []

questions = [
    questions(questions_reponses[0], "reponse")
    questions(questions_reponses[1], "reponse")
    questions(questions_reponses[2], "reponse")
    
]


def test(questions):
    score = 0
    for question in questions:
        reponse = input(question.inv_com)
        if reponse == question.reponse:
            score += 1
        print(" Bien joué, tu as 1 point en plus ! Ton total est de : " + str(score) + "/" + str(len(questions)))
        

test(questions)
       