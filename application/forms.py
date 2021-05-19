from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms import validators
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired, ValidationError, Length
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application.models import media_type, composer, media_label, music_category

from application import db

class AlbumForm(FlaskForm):
    name                = StringField('Album Name', validators=[DataRequired()])
    mediatype           = SelectField('Media Type', validators=[DataRequired()])
    composer            = SelectField('Composer',   validators=[DataRequired()])
    media_label         = SelectField('Label',      validators=[DataRequired()])
    music_category      = SelectField('category',   validators=[DataRequired()])
    number_of_tracks    = IntegerField('Number of Tracks', validators=[DataRequired()])
    number_of_disks     = IntegerField('Number of Disks', validators=[DataRequired()])
    #--
    submit              = SubmitField('Save')
    delete              = SubmitField('Delete')

    def __init__(self):
        super(AlbumForm, self).__init__()
        self.mediatype.choices      = [(c.id, c.description)    for c in media_type.query.all()]
        self.composer.choices       = [(c.id, c.name)           for c in composer.query.all()]
        self.media_label.choices    = [(c.id, c.name)           for c in media_label.query.all()]
        self.music_category.choices = [(c.id, c.description)    for c in music_category.query.all()]

class CategoryForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired(), Length(min=2,max=15)])
    submit = SubmitField('Save')
    delete = SubmitField('Delete')

class LabelForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2,max=15)])
    submit = SubmitField('Save')
    delete = SubmitField('Delete')

class ComposerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2,max=15)])
    submit = SubmitField('Save')
    delete = SubmitField('Delete')