# Defining a function that hold two sets of symptom categories
def cc_symptoms(symptoms):
    Malaria_symptoms = {
        "fever",
        "chills",
        "sweating",
        "headache",
        "nausea",
        "vomiting",
        "muscle pain",
        "fatigue",
        "anemia",
        "jaundice"
    }
    Stress_symptoms = {
         "irritability",
        "anxiety",
        "restlessness",
        "muscle tension",
        "headache",
        "fatigue",
        "difficulty concentrating",
        "changes in appetite",
        "sleep disturbances",
        "digestive issues"
    }

    # Converting user input to lowercase for case sensitivity checking
    input_symptoms = set(symptom.lower() for symptom in symptoms)

    # Determing how many user-inputted symptoms match the list of symptoms in the categories defined above
    Malaria_matches = input_symptoms.intersection(Malaria_symptoms)
    Stress_matches = input_symptoms.intersection(Stress_symptoms)

    # Determing the length of symptom matches
    Malaria = len(Malaria_matches)
    Stress = len(Stress_matches)

    # Determining Possible Conditions
    if Malaria > Stress and Malaria >= 2:
        return "Malaria detected. Consult a health professional"
    elif Stress > Malaria and Stress >= 2:
        return "High level of stress detected. Seek the service of a mental health professional"
    else:
        return "You seem fine. Seek assistance of a health professional if you think you're unwell"


if __name__ == "__main__":
    print("Welcome to the demo symptoms checker. Enter symptoms you\'ve noticed so far separated by commas")
    entry = input('Enter your symptoms: ')
    # Splitting user inputs into a list
    symptom_list = [symptom.strip for symptom in entry.split(",")]
    result = cc_symptoms(symptom_list)
    print(result)
