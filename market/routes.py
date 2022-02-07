from market import app
from flask import render_template, redirect, url_for, flash, request
from market.models import  User, Vacation
from market.forms import RegisterForm, LoginForm, VacationRequestForm
from market import db
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/vacation', methods=['GET', 'POST'])
@login_required
def vacation_page():
    if request.method == "GET":
        all_vacations = Vacation.query.all()
        past_vacations = db.session.query(User, Vacation).join(Vacation).filter_by(requester=current_user.id).all()


        return render_template('vacation.html', all_vacations =all_vacations,past_vacations=past_vacations) #


@app.route('/vacation_request', methods=['GET', 'POST'])
def vacation_request_page():
    form = VacationRequestForm()

    if form.validate_on_submit():
        vacation_to_create = Vacation(
                              # start_date=form.start_date.data,
                              # end_date=form.end_date.data,
                              work_days=form.work_days.data,
                              reason=form.reason.data,
                              comments = form.comments.data,
                              requester = current_user.id )

        db.session.add(vacation_to_create)
        db.session.commit()
        flash(f"Vacation request created successfully! ", category='success')
        return redirect(url_for('vacation_page'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a vacation request: {err_msg}', category='danger')

    return render_template('vacation_request.html', form=form)





@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              first_name=form.first_name.data,
                              last_name=form.last_name.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category='success')
        return redirect(url_for('vacation_page'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('vacation_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))
