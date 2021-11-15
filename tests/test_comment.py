import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):

  def setUp(self):
      self.user_Vickie = User(first_name="Vickie",
                            last_name="Shiraa",
                            username="Shaggy_Neils",
                            password="787898",
                            email="victor.wairiguini@student.moringaschool.com")
      self.new_post = Post(post_title="Title Here",
                            post_content="Time To Float.",
                            user_id=self.user_Vickie.id)
      self.new_comment = Comment(comment="Tortuga",
                                post_id=self.new_post.id,
                                user_id=self.user_Vickie.id)

  def test_instance(self):
      self.assertTrue(isinstance(self.user_Vickie, User))
      self.assertTrue(isinstance(self.new_post, Post))
      self.assertTrue(isinstance(self.new_comment, Comment))