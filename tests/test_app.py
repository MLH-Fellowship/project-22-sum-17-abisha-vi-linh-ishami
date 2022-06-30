from app import app
import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html

        assert "<h1>Ishami Rulinda</h1>" in html
        assert "<h1>Projects</h1>" in html
        assert "<meta charset=\"utf-8\" />" in html
    
    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
    
    def test_timeline_page_form(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Timeline</title>" in html
        assert 'name="name"' in html
        assert 'name="email"' in html
        assert 'name="content"' in html


    def test_timeline_post(self):
        info = {"name": "testname", "email": "test2@gmail.com",
                "content": "hello world!"}
        response = self.client.post("/api/timeline_post", data=info)
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert json["name"] == "testname"
        assert json["email"] == "test2@gmail.com"
        assert json["content"] == "hello world!"

        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1

        info = {"name": "testname2", "email": "testname2@gmail.com",
                "content": "bye world!"}
        response = self.client.post("/api/timeline_post", data=info)
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert json["name"] == "testname2"
        assert json["email"] == "testname2@gmail.com"
        assert json["content"] == "bye world!"

        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 2

    def test_malformed_timeline_post(self):
        response = self.client.post("/api/timeline_post", data={
            "email": "john@example.com", "content": "Hello world, I'm John!",
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        response = self.client.post("/api/timeline_post", data={"name": "John Doe",
            "email": "john@example.com", "content": "",
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        response = self.client.post("/api/timeline_post", data={"name": "John Doe",
            "email": "not-an-email", "content": "Hello world, I'm John!",
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html

