import pytest

@pytest.fixture(scope="session")
def test_session():
    # Initialize testing environment
    
    def pytest_addoption(parser):
        parser.addoption("--block-merges", action="store_true", default=False)
    
    yield
    
    if option("block-merges"):
        print("Blocking merge due to failed tests.")