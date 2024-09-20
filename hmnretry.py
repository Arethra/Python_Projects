def cc_symptoms(symptoms):
    Malaria_symptoms = {
        "Fever",
        "Cattarrh",
        "Cough",
        "pneumenia"
    }
    Stress_symptoms = {
        "anxiety",
        "stress"
    }

    input_symptoms = set(symptom.lower() for symptom in symptoms)

    Malaria_matches = input_symptoms.intersection(Malaria_symptoms)
    Stress_matches = input_symptoms.intersection(Stress_symptoms)

    Malaria = len(Malaria_matches)
    Stress = len(Stress_matches)

    if Malaria > Stress and Malaria >= 2:
        return "You have Malaria oga."
    elif Stress > Malaria and Stress >= 2:
        return "oga dey rest abeg..."
    else:
        return "Why are you here??"
    
if __name__ == "__main__":
    print("Someting is wrong abi?? Welcome. Enter what you\'ve noticed so far separated by commas")
    entry = input('Enter your symptoms: ')
    symptom_list = [symptom.strip for symptom in entry.split(",")]
    result = cc_symptoms(symptom_list)
    print(result)