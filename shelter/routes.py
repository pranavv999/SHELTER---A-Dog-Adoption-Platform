from flask import render_template, url_for, flash, redirect, request, abort
from shelter import app, db
from shelter.forms import (SignUpForm, LoginForm,
                           UpdateAccountForm, AdvertiseForm)
from shelter.utils import password_hash, check_password, save_picture
from shelter.models import User, Advertisement
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/home')
def home():
    ads = Advertisement.query.all()
    return render_template('index.html', title="Home", ads=ads)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        # Getting User data from FORM
        hashed_password = password_hash(form.password.data)
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        mobile_no = form.mobile_number.data
        # Creating Table Object
        user = User(name=name, surname=surname, email=email,
                    mobile_number=mobile_no, password=hashed_password)
        # Adding User data to DATABASE
        db.session.add(user)
        db.session.commit()
        # Dsiplay success message on screen
        flash("Account Created Successfully..!", "success")
        return redirect(url_for('login'))
    return render_template('signup.html', title="SignUp", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next', 'home')
            return redirect(next_page)

        else:
            flash("Login Unsuccessful", 'danger')
    return render_template('login.html', title="Login", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.surname = form.surname.data
        current_user.email = form.email.data
        current_user.mobile_number = form.mobile_number.data
        db.session.commit()
        flash('Your account updated successfully..!', 'success')
        return redirect(url_for('account'))

    elif request.method == 'GET':
        form.name.data = current_user.name
        form.surname.data = current_user.surname
        form.email.data = current_user.email
        form.mobile_number.data = current_user.mobile_number

    return render_template('account.html', title='User Account', form=form)


@app.route('/ad/new', methods=['GET', 'POST'])
@login_required
def post_advertise():
    form = AdvertiseForm()
    if form.validate_on_submit():
        # Getting Ad Data From FORM
        breed = form.dog_breed.data
        location = form.location.data
        description = form.description.data
        picture = save_picture(form.dog_pic.data)
        owner = current_user
        # Creating table Object
        ad = Advertisement(breed_name=breed, location=location,
                           description=description, image_file=picture,
                           owner=owner
                           )
        db.session.add(ad)
        db.session.commit()
        flash('Your Advertise has been added', 'success')
        return redirect(url_for('home'))
    return render_template('post_advertise.html', title='Post Advertise',
                           form=form, legend='Update Post')


@app.route('/ad/<int:ad_id>')
def ad_details(ad_id):
    ad = Advertisement.query.get_or_404(ad_id)
    return render_template('ad_details.html', title='Dog details', ad=ad)


@app.route('/user/<int:user_id>')
@login_required
def user_info(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user_info.html', title='User Info', user=user)


@app.route('/ad/<int:ad_id>/update', methods=['GET', 'POST'])
@login_required
def ad_update(ad_id):
    ad = Advertisement.query.get_or_404(ad_id)
    if ad.owner != current_user:
        abort(403)
    form = AdvertiseForm()
    if form.validate_on_submit():
        ad.breed_name = form.dog_breed.data
        ad.location = form.location.data
        ad.description = form.description.data
        ad.image_file = save_picture(form.dog_pic.data)
        db.session.commit()
        flash('Your Post Successfully Updated..!!!', 'success')
        return redirect(url_for('ad_details', ad_id=ad.id))
    elif request.method == 'GET':
        # Pre-Populating Fields
        form.dog_breed.data = ad.breed_name
        form.location.data = ad.location
        form.description.data = ad.description
        form.dog_pic.data = url_for('static',
                                    filename='img/dog_img/' + ad.image_file)
    return render_template('post_advertise.html', title='Update Advertise',
                           form=form, legend='Update Post')


@app.route('/ad/<int:ad_id>/delete', methods=['POST'])
@login_required
def delete_ad(ad_id):
    ad = Advertisement.query.get_or_404(ad_id)
    if ad.owner != current_user:
        abort(403)
    else:
        db.session.delete(ad)
        db.session.commit()
        flash('Your advertisement has been deleted..!', 'warning')
        return redirect(url_for('home'))
