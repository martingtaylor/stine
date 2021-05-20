from flask import url_for
from flask_testing import TestCase
from application import app, models, db

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///D:\Work\QA\projects2\STINE\database\stine.db",
                SECRET_KEY='ndfjcvas94389oifjjo90',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        # db.create_all()
        models.album.query.delete()
        models.composer.query.delete()
        models.media_label.query.delete()
        models.music_category.query.delete()



        # Create test data
        sample = models.composer(name="Test Composer")
        db.session.add(sample)
        db.session.commit()

        sample = models.media_label(name="Test Label")
        db.session.add(sample)
        db.session.commit()
        
        sample = models.music_category(description="Test Category")
        db.session.add(sample)
        db.session.commit()
        
        sample = models.album(name="Test Album", media_type=1, category=1, composer=1, label=1, number_of_tracks=1, number_of_disks=1)
        db.session.add(sample)
        db.session.commit()
 

    def tearDown(self):
        """
        Will be called after every test
        """

        #db.session.remove()
        #db.drop_all()

# Write a test class for testing that the home page loads but we are not able to run a get request for delete and update routes.
class TestViews(TestBase):

    def test_album_get(self):
        response = self.client.get(url_for('_album'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Album', response.data)

    def test_albumedit_get(self):
        response = self.client.get(url_for('albumedit', aid=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Album', response.data)

    def test_composer_get(self):
        response = self.client.get(url_for('_composer'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Composer', response.data)

    def test_composeredit_get(self):
        response = self.client.get(url_for('composeredit', cid="1"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Composer', response.data)

    def test_label_get(self):
        response = self.client.get(url_for('label'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Label', response.data)

    def test_labeledit_get(self):
        response = self.client.get(url_for('labeledit', lid="1"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Label', response.data)

    def test_category(self):
        response = self.client.get(url_for('category'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Category', response.data)

    def test_categoryedit_get(self):
        response = self.client.get(url_for('categoryedit', cid="1"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Category', response.data)


# Test adding 
class TestAdd(TestBase):
    #def test_album_post(self):
    #    response = self.client.post(url_for('_album', aid="1"), follow_redirects=True)
    #    self.assertIn(b'Test Album',response.data)

    def test_albumedit_post(self):
        response = self.client.post(url_for('albumedit', aid="1"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Album',response.data)
    
    def test_composer_post(self):
        response = self.client.post(url_for('_composer'), data = dict(cid="1"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Composer',response.data)

    def test_composeredit_post(self):
        response = self.client.post(url_for('composeredit', cid="1"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Composer',response.data)

    def test_label_post(self):
        response = self.client.post(url_for('label'), data = dict(lid="1"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Label',response.data)

    def test_label_edit_post(self):
        response = self.client.post(url_for('labeledit', lid="1"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Label',response.data)        

    def test_category_post(self):
        response = self.client.post(url_for('category'), data = dict(cid="1"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Category',response.data)

    def test_category_edit_post(self):
        response = self.client.post(url_for('categoryedit', cid="1"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Category',response.data)   
