from application import db
from application.models import album, composer, music_category, media_type, media_label

print("STINE - Set Up.")

print("Dropping and previous database")
db.drop_all()

print("Creating new instance")
db.create_all()

# Media Type
_media_type = media_type(description="C.D.")
db.session.add(_media_type)
db.session.commit()
_media_type = media_type(description="Vinyl")
db.session.add(_media_type)
db.session.commit()
_media_type = media_type(description="Digital")
db.session.add(_media_type)
db.session.commit()

print("Finished Create")