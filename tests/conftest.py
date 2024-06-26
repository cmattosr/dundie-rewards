import pytest

MARKER = """\
unit: Mark unit tests
high: High priority
medium: Medium priority
low: Low priority
"""


def pytest_configure(config):
    for line in MARKER.split("\n"):
        config.addinivalue_line("markers", line)


@pytest.fixture(autouse=True)
def go_to_tempdir(request):  # injecão de dependências
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield
