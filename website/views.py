from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from werkzeug.exceptions import abort
from .models import Activity, User
from . import db
import json


views = Blueprint('views', __name__)


# Mapping of class titles to display titles
DISPLAY_TITLES = {
    'adult_ent': 'Adult Entertainment',
    'music_venue': 'Music Venue',
    'comedy_club': 'Comedy Club'
}

@views.route('/', methods=['GET'])
def home():
    if current_user.is_authenticated:
        return render_template("home.html", user=current_user)
    else:
        return render_template("home.html", user=None)



# allow activities page to run get and post methods 
@views.route('/activities', methods=['GET', 'POST'])
@login_required
def activities():
    filtered_activities= []
    if request.method == 'POST':
        # Your existing code for adding a new activity

    # Query activities with at least one boolean attribute set to True
        filtered_activities = Activity.query.filter_by(user_id=current_user.id).filter(
        db.or_(
            Activity.nightlife == True,
            Activity.restaurant == True,
            Activity.bakery == True,
            Activity.activity == True,
            Activity.adult_ent == True,
            Activity.nightclub == True,
            Activity.music_venue == True,
            Activity.comedy_club == True,
            Activity.outdoors == True,
            Activity.visited == True,
        )
    ).all()

    return render_template("activities.html", user=current_user, activities=filtered_activities)


@views.route('/add-activity', methods=['GET','POST'])
@login_required
def add_activity():
    if request.method == 'POST':
        # Handle the form submission logic
        title = request.form.get('title')
        description = request.form.get('description')
        nightlife = 'nightlife' in request.form
        restaurant = 'restaurant' in request.form
        bakery = 'bakery' in request.form
        activity = 'activity' in request.form
        adult_ent = 'adult_ent' in request.form
        nightclub = 'nightclub' in request.form
        music_venue = 'music_venue' in request.form
        comedy_club = 'comedy_club' in request.form
        outdoors = 'outdoors' in request.form
        visited = 'visited' in request.form
        
        
        existing_activity = Activity.query.filter_by(title=title, user_id=current_user.id).first()
        
        if existing_activity:
            flash('Activity with the same title already exists.', category='error')
        else:
            new_activity = Activity(
                title=title, 
                description=description, 
                user_id=current_user.id,
                nightlife=nightlife,
                restaurant=restaurant,
                bakery=bakery,
                activity=activity,
                adult_ent=adult_ent,
                nightclub=nightclub,
                music_venue=music_venue,
                comedy_club=comedy_club,
                outdoors=outdoors,
                visited=visited)            
            db.session.add(new_activity)
            db.session.commit()
            flash('Activity added!', category='success')

        # Redirect to the activities page after adding an activity
        return render_template("activities.html", user=current_user)

    # Handle the case where the request method is GET (e.g., displaying the form)
    return render_template("add_activity.html", user=current_user)



@views.route('/delete-activity', methods=['GET', 'POST'])
def delete_activity():
    request_data = json.loads(request.data)
    activity_id = request_data['activityId']
    
    activity_to_delete = Activity.query.get(activity_id)
    
    if activity_to_delete and activity_to_delete.user_id == current_user.id:
        db.session.delete(activity_to_delete)
        db.session.commit()
    return render_template("activities.html", user=current_user)

@views.route('/edit-activity/<int:activity_id>', methods=['GET', 'POST'])
@login_required
def edit_activity(activity_id):
    activity_to_edit = Activity.query.get(activity_id)

    # Check if the user has permission to edit this activity
    if not activity_to_edit or activity_to_edit.user_id != current_user.id:
        abort(403)  # Forbidden

    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        nightlife = 'nightlife' in request.form
        restaurant = 'restaurant' in request.form
        bakery = 'bakery' in request.form
        activity = 'activity' in request.form
        adult_ent = 'adult_ent' in request.form
        nightclub = 'nightclub' in request.form
        music_venue = 'music_venue' in request.form
        comedy_club = 'comedy_club' in request.form
        outdoors = 'outdoors' in request.form
        visited = 'visited' in request.form

        # Update the activity with the new information
        activity_to_edit.title = title
        activity_to_edit.description = description
        activity_to_edit.nightlife = nightlife
        activity_to_edit.restuarant = restaurant
        activity_to_edit.bakery = bakery
        activity_to_edit.activity = activity
        activity_to_edit.adult_ent = adult_ent
        activity_to_edit.nightclub = nightclub
        activity_to_edit.music_venue = music_venue
        activity_to_edit.comedy_club = comedy_club
        activity_to_edit.outdoors = outdoors
        activity_to_edit.visited = visited
        

        db.session.commit()
        flash('Activity updated successfully!', category='success')
        return render_template("activities.html", user=current_user)

    return render_template("edit_activity.html", user=current_user, activity=activity_to_edit)
