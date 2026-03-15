import json

def recommend_career(skills):

    with open("career_data.json") as f:
        careers = json.load(f)

    best_match = None
    max_score = 0

    for career, req_skills in careers.items():

        score = len(set(skills).intersection(req_skills))

        if score > max_score:
            max_score = score
            best_match = career

    return best_match