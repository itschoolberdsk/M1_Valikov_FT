import topic_sport as tsp
import topic_animals_world as taw
import topic_space as tspa
import normal_dialog as nd
import base

print(nd.CONVERSATION)
print(base.CHOOSE_THEME)

def answerQuestion(data: dict):
    global onBot
    while True:
            question = input()
            question_mini = question.lower()
            
            if question_mini == base.END_DIALOG:
                print(base.END_TEXT)
                onBot = False
                break
            elif question_mini == base.CHANGING_THE_SUBJECT:
                print(base.CHOOSE_THEME)
                break
            elif question_mini not in data.keys():
                print(base.SUGGESTION)
                continue

            print(data.get(question_mini))


onBot = True
while onBot:
    choose_theme = input()
    choose_theme_mini = choose_theme.lower()
    
    if choose_theme_mini in base.END_DIALOG:
        print(base.END_TEXT)
        break
    elif choose_theme_mini in tsp.SPORT:
        print(base.FIND_OUT_SOMETHING)
        answerQuestion(tsp.answerToQuestion)
    elif choose_theme_mini in taw.ANIMALS_WORLD:
        print(base.FIND_OUT_SOMETHING)
        answerQuestion(taw.answerToQuestion)  
    elif choose_theme_mini in tspa.SPACE:
        print(base.FIND_OUT_SOMETHING)
        answerQuestion(tspa.answerToQuestion)
    elif choose_theme_mini in nd.CONVERSATION:
        print(base.OK_TEXT)
        answerQuestion(nd.answerToQuestion)
