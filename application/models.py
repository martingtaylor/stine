from application import db

# Data Table definitions

# Media_type
class media_type(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    description     = db.Column(db.String(30), unique=True, nullable=False)
    album           = db.relationship('album',         backref='albummediatype')    

# Music Categories
class music_category(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    description     = db.Column(db.String(30))
    album           = db.relationship('album',         backref='albumcategory')

# Composer
class composer(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(30))
    album           = db.relationship('album',         backref='albumcomposer')    

# Publish Labels
class media_label(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(30))
    album           = db.relationship('album',         backref='albumlabel')   

# Main album table
class album(db.Model):
    id                  = db.Column(db.Integer, primary_key=True)
    name                = db.Column(db.String(30))
    media_type          = db.Column(db.Integer, db.ForeignKey('media_type.id'), nullable=False)
    category            = db.Column(db.Integer, db.ForeignKey('music_category.id'), nullable=False)
    composer            = db.Column(db.Integer, db.ForeignKey('composer.id'), nullable=False)
    label               = db.Column(db.Integer, db.ForeignKey('media_label.id'), nullable=False)
    number_of_tracks    = db.Column(db.Integer)
    number_of_disks     = db.Column(db.Integer)



