import uuid
import pytest
from dundie.core import load
from constants import PEOPLE_FILE


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_has_2_people(request):
    """Test load function"""
    
    request.addfinalizer(lambda: print("\nTerminou"))
    
    with open(f"arquivo_indesejado-{uuid.uuid4()}.txt", "w") as file_:
        file_.write("dados uteis somente para o teste")
    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'J'
    
@pytest.mark.unit
@pytest.mark.high
def test_load_positive_first_name_starts_with_j(request):
    """Test load function"""
    
    request.addfinalizer(lambda: print("\nTerminou"))
    
    with open(f"arquivo_indesejado-{uuid.uuid4()}.txt", "w") as file_:
        file_.write("dados uteis somente para o teste")
    assert load(PEOPLE_FILE)[0][0] == 'J'
    