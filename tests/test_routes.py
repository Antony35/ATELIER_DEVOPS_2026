# tests/test_routes.py
from app import app


def test_accueil_repond_200():
    client = app.test_client()
    reponse = client.get("/")
    assert reponse.status_code == 200
    assert "Bonjour tout le monde" in reponse.get_data(as_text=True)

def test_exercices_repond_200():
    client = app.test_client()
    reponse = client.get("/exercices/")
    assert reponse.status_code == 200
    assert "ça fonctionne !" in reponse.get_data(as_text=True).lower()
    assert "Antony Huart" in reponse.get_data(as_text=True)
