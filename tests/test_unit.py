from app.recommend_system.recommendModule import RecommendModule
import pytest

def test_init_recommend_module():

    assert RecommendModule(data_path='./app/weight/dataset.csv')
    assert RecommendModule(movie_path='./app/weight/movies.csv')
    assert RecommendModule(data_path='./app/weight/dataset.csv',movie_path='./app/weight/movies.csv')



@pytest.fixture
def init_recommendObj() -> RecommendModule:
    return RecommendModule(data_path='./app/weight/dataset.csv',movie_path='./app/weight/movies.csv')


def test_load_model(init_recommendObj):
   assert init_recommendObj.load_model() == True
   assert init_recommendObj.load_model(model_path='./app/weight/recommend_algor') == True

def test_get_features(init_recommendObj):
    assert len(init_recommendObj.get_features(1)) != 0

@pytest.fixture
def recommendObj() -> RecommendModule:
    temp = RecommendModule(data_path='./app/weight/dataset.csv',movie_path='./app/weight/movies.csv')
    temp.load_model()
    return temp

def test_inference_recommend(recommendObj):
    assert len(recommendObj._inference_recommend(1)) != 0

def test_invoke_onlyItem(recommendObj):
    assert int(recommendObj.invoke_onlyItem(1)[0]["id"])

def test_invoke_Item_wMetadata(recommendObj):
    assert isinstance(recommendObj.invoke_Item_wMetadata(1)[0]["title"],str) 