import pandas as pd
from surprise import dump
import operator
from fastapi import HTTPException

class RecommendModule:
    def __init__(self,data_path='./app/weight/dataset.csv',movie_path='./app/weight/movies.csv',set_max_rec_items=5):
        try:
            movie = pd.read_csv(movie_path,dtype={'userId': int, 'movieId': int})
        except Exception as e:
            raise HTTPException(status_code=500, detail="Movie data has not found!")
        
        self._all_items = { row["movieId"] :{ "title" : row["title"],"genres" : row["genres"] } for _,row in movie.iterrows() }
        self._set_max_rec_items = set_max_rec_items
        
        try:
            ground_truth = pd.read_csv(data_path,index_col="Unnamed: 0",dtype={'userId': int, 'movieId': int})
        except Exception as e:
            raise HTTPException(status_code=500, detail="File history has not found!")
    
        
        self.ground_truth = ground_truth.drop(["timestamp"],axis=1)
        self.model = None

    def load_model(self,model_path='./app/weight/recommend_algor') -> bool:
        try:
            _,self.model = dump.load(model_path)
            return True
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error Model Loaded")
    
    def get_features(self,uid:int):
        return [ (val["userId"],int(val["movieId"]),val["rating"] )for _,val in self.ground_truth[self.ground_truth.userId == uid].iterrows()]

    def _inference_recommend(self,uid:int):
        if self.model is None:
            self.load_model()

        user_items = self.get_features(uid)
        recommendations = self.model.test(user_items)

        recommendations.sort(key=operator.itemgetter(3), reverse=True)
        return recommendations
        
    def invoke_onlyItem(self,uid:int):
        temp = self._inference_recommend(uid)

        return [{"id": i[1]} for i in temp[0:self._set_max_rec_items]]
    
    def invoke_Item_wMetadata(self,uid:int):
        temp = self._inference_recommend(uid)

        return [{"id": i[1], "title":self._all_items[i[1]]["title"] , "genres" : self._all_items[i[1]]["genres"] } for i in temp[0:self._set_max_rec_items]]


recommend_obj = RecommendModule()