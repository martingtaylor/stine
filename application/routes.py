#from Projects.STINE.application.forms import AlbumForm
# from Projects.STINE.application.models import media_type
import re
from application import app, db
from flask import Flask, render_template, request, redirect, url_for
from application.models import album, music_category, media_label, composer, media_type
from application.forms import AlbumForm, CategoryForm, LabelForm, ComposerForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

# Albums
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def _album():
    error = ""
    # all_albums = album.query.all()
    all_albums = db.session.query(album,composer,media_type,media_label,music_category).filter(composer.id==album.composer).filter(album.media_type==media_type.id).filter(album.label==media_label.id).filter(album.category==music_category.id).order_by(album.name).all()

    form = AlbumForm()

    if request.method == "POST":
        _name       = form.name.data
        _media_type = int(form.mediatype.data)
        _composer   = int(form.composer.data)
        _label      = int(form.media_label.data)
        _category   = int(form.music_category.data)
        _numtracks  = form.number_of_tracks.data
        _numdisks   = form.number_of_disks.data
       
        _album = album( name=_name, 
                        media_type=_media_type,
                        composer=_composer,
                        category=_category,
                        label=_label,
                        number_of_tracks=_numtracks,
                        number_of_disks=_numdisks)

        db.session.add(_album)
        db.session.commit()

        form.name.name = ""
        # all_albums = album.query.all()
        all_albums = db.session.query(album,composer,media_type,media_label,music_category).filter(composer.id==album.composer).filter(album.media_type==media_type.id).filter(album.label==media_label.id).filter(album.category==music_category.id).order_by(album.name).all()

    return render_template('album.html', form=form, album_list=all_albums)
    
@app.route('/albumedit/<aid>', methods=['GET', 'POST'])
def albumedit(aid):
    error = ""
    # all_albums=album.query.all()
    all_albums = db.session.query(album,composer,media_type,media_label,music_category).filter(composer.id==album.composer).filter(album.media_type==media_type.id).filter(album.label==media_label.id).filter(album.category==music_category.id).order_by(album.name).all()


    form = AlbumForm()

    #if form.validate_on_submit():
    if request.method == "GET":
        if db.session.query(album.query.filter(album.id == aid).exists()).scalar():
            _album = album.query.filter_by(id=aid).first()
            _name = _album.name
            _mediatype = int(_album.media_type)
            _composer = int(_album.composer)
            _label = int(_album.label)
            _category = int(_album.category)
            _numoftracks = (_album.number_of_tracks)
            _numofdisks = (_album.number_of_disks)
            form.name.data = _name
            # form.mediatype.id.id = 1
            form.number_of_tracks.data = _numoftracks
            form.number_of_disks.data = _numofdisks
        else:
            error = "Unable to locate ID " + aid
    
    if request.method == "POST":
        if 'Save' in str(request.form):
            # Save item
            _name = form.name.data       
            _mediatype = int(form.mediatype.data)
            _composer = int(form.composer.data)
            _label = int(form.media_label.data)   
            _category = int(form.music_category.data)         
            _number_of_tracks = int(form.number_of_tracks.data)
            _number_of_disks = int(form.number_of_disks.data)
        
            if db.session.query(album.query.filter(album.id == aid).exists()).scalar():
                _album = album.query.filter_by(id=aid).first()
                _album.name = _name
                _album.media_type = _mediatype
                _album.composer = _composer                
                _album.label = _label             
                _album.category = _category
                _album.number_of_tracks = str(_number_of_tracks)
                _album.number_of_disks = str(_number_of_disks)
                db.session.commit()
                return redirect(url_for('_album'))
            else:
                error = "Unable to locate ID " + aid

        if 'Delete' in str(request.form):
            # Delete Item
            if db.session.query(album.query.filter(album.id == aid).exists()).scalar():
                _album = album.query.filter_by(id=aid).first()
                db.session.delete(_album)
                db.session.commit()
                return redirect(url_for('_album'))
            else:
                error = "Unable to locate ID " + aid
    
    return render_template('albumedit.html', form=form, album_list=all_albums, message=error)



# Composer
@app.route('/composer', methods=['GET', 'POST'])
def _composer():
    error = ""
    all_composers = composer.query.all()
    form = ComposerForm()

    if request.method == "POST":
        name = form.name.data
        if not db.session.query(composer.query.filter(composer.name == name).exists()).scalar():
            _composer = composer(name=name)
            db.session.add(_composer)
            db.session.commit()
            form.name.data = ""
            all_composers=composer.query.all()
        else:
            error = "Composer has already been entered"

    return render_template('composer.html', form=form, composer_list=all_composers, message=error)
   
@app.route('/composeredit/<cid>', methods=['GET', 'POST'])
def composeredit(cid):
    error = ""
    all_composers=composer.query.all()
    form = ComposerForm()

    #if form.validate_on_submit():
    if request.method == "GET":
        if db.session.query(composer.query.filter(composer.id == cid).exists()).scalar():
            _composer = composer.query.filter_by(id=cid).first()
            name = _composer.name
            form.name.data = name
        else:
            error = "Unable to locate CID " + cid

    if request.method == "POST":
        if 'Save' in str(request.form):
            # Save item
            name = form.name.data
            if db.session.query(composer.query.filter(composer.id == cid).exists()).scalar():
                _composer = composer.query.filter_by(id=cid).first()
                _composer.name = name
                db.session.commit()
                return redirect(url_for('_composer'))
            else:
                error = "Unable to locate ID " + cid

        if 'Delete' in str(request.form):
            # Delete Item
            if db.session.query(composer.query.filter(composer.id == cid).exists()).scalar():
                _composer = composer.query.filter_by(id=cid).first()
                db.session.delete(_composer)
                db.session.commit()
                return redirect(url_for('_composer'))
            else:
                error = "Unable to locate ID " + cid
    return render_template('composeredit.html', form=form, composer_list=all_composers, message=error)


# Media Labels
@app.route('/label', methods=['GET', 'POST'])
def label():
    error = ""
    all_labels=media_label.query.all()
    form = LabelForm()

    if request.method == "POST":
        name = form.name.data
        if not db.session.query(media_label.query.filter(media_label.name == name).exists()).scalar():
            _label = media_label(name=name)
            db.session.add(_label)
            db.session.commit()
            form.name.data = ""
            all_labels=media_label.query.all()
        else:
            error = "Label has already been entered"

    return render_template('label.html', form=form, lab_list=all_labels, message=error)
   

@app.route('/labeledit/<lid>', methods=['GET', 'POST'])
def labeledit(lid):
    error = ""
    all_labels=media_label.query.all()
    form = LabelForm()

    #if form.validate_on_submit():
    if request.method == "GET":
        if db.session.query(media_label.query.filter(media_label.id == lid).exists()).scalar():
            _label = media_label.query.filter_by(id=lid).first()
            name = _label.name
            form.name.data = name
        else:
            error = "Unable to locate CID " + lid

    if request.method == "POST":
        if 'Save' in str(request.form):
            # Save item
            name = form.name.data
            if db.session.query(media_label.query.filter(media_label.id == lid).exists()).scalar():
                _label = media_label.query.filter_by(id=lid).first()
                _label.name = name
                db.session.commit()
                return redirect(url_for('label'))
            else:
                error = "Unable to locate CID " + lid

        if 'Delete' in str(request.form):
            # Delete Item
            if db.session.query(media_label.query.filter(media_label.id == lid).exists()).scalar():
                _label = media_label.query.filter_by(id=lid).first()
                db.session.delete(_label)
                db.session.commit()
                return redirect(url_for('label'))
            else:
                error = "Unable to locate CID " + lid
    return render_template('labeledit.html', form=form, lab_list=all_labels, message=error)


# Category routes
@app.route('/category', methods=['GET', 'POST'])
def category():
    error = ""
    all_categories=music_category.query.all()
    form = CategoryForm()

    if request.method == "POST":
        desc = form.description.data
        if not db.session.query(music_category.query.filter(music_category.description == desc).exists()).scalar():
            _category = music_category(description=desc)
            db.session.add(_category)
            db.session.commit()
            form.description.data = ""
            all_categories=music_category.query.all()
        else:
            error = "Category has already been entered"

    return render_template('category.html', form=form, cat_list=all_categories, message=error)
    

@app.route('/categoryedit/<cid>', methods=['GET', 'POST'])
def categoryedit(cid):
    error = ""
    all_categories=music_category.query.all()
    form = CategoryForm()

    #if form.validate_on_submit():
    if request.method == "GET":
        if db.session.query(music_category.query.filter(music_category.id == cid).exists()).scalar():
            _category = music_category.query.filter_by(id=cid).first()
            desc = _category.description
            form.description.data = desc
        else:
            error = "Unable to locate CID " + cid

    if request.method == "POST":
        print(">>>>", str(request.form))
        if 'Save' in str(request.form):
            # Save item
            desc = form.description.data
            if db.session.query(music_category.query.filter(music_category.id == cid).exists()).scalar():
                _category = music_category.query.filter_by(id=cid).first()
                _category.description = desc
                db.session.commit()
                return redirect(url_for('category'))
            else:
                error = "Unable to locate CID " + cid

        if 'Delete' in str(request.form):
            # Delete Item
            if db.session.query(music_category.query.filter(music_category.id == cid).exists()).scalar():
                _category = music_category.query.filter_by(id=cid).first()
                db.session.delete(_category)
                db.session.commit()
                return redirect(url_for('category'))
            else:
                error = "Unable to locate CID " + cid
    return render_template('categoryedit.html', form=form, cat_list=all_categories, message=error)
    
