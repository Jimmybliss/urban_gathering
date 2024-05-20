import pickle
from django.shortcuts import render
from .models import Invitation
from django.http import HttpResponse
from django.http import HttpResponseBadRequest

   # Load the model and encoders
with open('logistic_regression_model.pkl', 'rb') as f:
   model = pickle.load(f)

with open('label_encoders.pkl', 'rb') as f:
   label_encoders = pickle.load(f)

def predict_invitation(request):
    invited = None
    if request.method == 'POST':
        try:
            # Extract form data
            age = int(request.POST['age'])
            gender = label_encoders['gender'].transform([request.POST['gender']])[0]
            occupation = label_encoders['occupation'].transform([request.POST['occupation']])[0]
            past_attendance = 'past_attendance' in request.POST
            social_media_followers = int(request.POST['social_media_followers'])
            interest_in_music = 'interest_in_music' in request.POST
            interest_in_art = 'interest_in_art' in request.POST
            interest_in_technology = 'interest_in_technology' in request.POST
            distance_from_venue = float(request.POST['distance_from_venue'])
            has_plus_one = 'has_plus_one' in request.POST

            # Prepare data for prediction
            input_data = [[age, gender, occupation, past_attendance, social_media_followers,
                           interest_in_music, interest_in_art, interest_in_technology,
                           distance_from_venue, has_plus_one]]

            # Predict
            prediction = model.predict(input_data)[0]
            invited = bool(prediction)
        except Exception as e:
            return HttpResponseBadRequest(f"Error: {e}")

        return render(request, 'invitations/predict.html', {'invited': invited})
    else:
        # Render the form for GET requests
        return render(request, 'invitations/predict.html')  # Render the form template
