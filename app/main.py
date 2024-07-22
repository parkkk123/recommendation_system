
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from app.recommend_system.recommendModule import recommend_obj
import logging
from app.base.responseModelItems import responseModelItems
from app.base.responseModelFeatures import responseModelFeatures
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        recommend_obj.load_model()
        logger.info(f'Load model successful')
    except Exception as e:
        logger.debug(f'Error : load model, msg = {e}')
        raise HTTPException(status_code=500, detail="System error")
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def hello_world():
    return {"Hello": "World"}


@app.get("/recommendations")
async def invoke_recommend(user_id : int,returnMetadata : bool = False):
    result = None
    if not returnMetadata :
        result = recommend_obj.invoke_onlyItem(user_id)
    else:
        result = recommend_obj.invoke_Item_wMetadata(user_id)

    return responseModelItems(items=result)

@app.get("/features")
async def invoke_recommend(user_id : int):

    result = recommend_obj.get_features(user_id)
    return responseModelFeatures(features=[{"histories" : [str(t[1]) for t in result]}])