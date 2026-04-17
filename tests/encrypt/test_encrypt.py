from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(6, 'A')
    assert encrypt_message("teste", 6) == "etset"
    assert encrypt_message("palavra", 3) == "lap_arva"
    assert encrypt_message("palavra", 4) == "arv_alap"
