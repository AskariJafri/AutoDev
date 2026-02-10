import unittest
from autodev.models import SearchQuery, Post
from autodev.utils import validate_search_query

class TestSearchFunctionality(unittest.TestCase):
    def test_valid_search_query(self):
        # Arrange
        query = SearchQuery(text="test query")
        result = Post.objects.filter(query=query)

        # Act
        validated_result = validate_search_query(result)
        assert isinstance(validated_result, list)

    def test_empty_search_query(self):
        # Arrange
        query = SearchQuery(text="")
        result = Post.objects.filter(query=query)

        # Act
        validated_result = validate_search_query(result)
        self.assertEqual(len(validated_result), 0)

    def test_invalid_characters(self):
        # Arrange
        query = SearchQuery(text="test!query")
        result = Post.objects.filter(query=query)

        # Act
        validated_result = validate_search_query(result)
        assert len(validated_result) == 0

if __name__ == '__main__':
    unittest.main()