from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from werkzeug.exceptions import abort
from .models import Activity
from . import db
import json


views = Blueprint('views', __name__)

# allow home page to run get and post methods 
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        
        existing_activity = Activity.query.filter_by(title=title, user_id=current_user.id).first()
        
        if existing_activity:
            flash('Activity with the same title already exists.', category='error')
        else:
            new_activity = Activity(title=title, description=description, user_id=current_user.id)
            db.session.add(new_activity)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/add-activity', methods=['GET','POST'])
@login_required
def add_activity():
    if request.method == 'POST':
        # Handle the form submission logic
        title = request.form.get('title')
        description = request.form.get('description')
        
        existing_activity = Activity.query.filter_by(title=title, user_id=current_user.id).first()
        
        if existing_activity:
            flash('Activity with the same title already exists.', category='error')
        else:
            new_activity = Activity(title=title, description=description, user_id=current_user.id)
            db.session.add(new_activity)
            db.session.commit()
            flash('Activity added!', category='success')

        # Redirect to the home page after adding an activity
        return render_template("home.html", user=current_user)

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
        
    return jsonify({})

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

        # Update the activity with the new information
        activity_to_edit.title = title
        activity_to_edit.description = description

        db.session.commit()
        flash('Activity updated successfully!', category='success')
        return render_template("home.html", user=current_user)

    return render_template("edit_activity.html", user=current_user, activity=activity_to_edit)
