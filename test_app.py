from app import app

def test_home():
    response=app.test_client().get("/")           #  get : Récupérer des données (ex : afficher une page)

    assert response.status_code==200        # 200 OK est un code de statut HTTP qui signifie que la requête s'est bien passée
    assert response.data== b"Hello World!"  # b car Flask renvoie une réponse en bytes (binaire)