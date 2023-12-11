from src.github_pylint import helloworld

def test_hellworld():
    assert helloworld.hello_world('suranga') == 'Hello suranga'