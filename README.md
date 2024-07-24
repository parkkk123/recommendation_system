# How to use this repo
Firstly, install package by using Poetry tool
```
$ cd recommendation_system/
$ poetry install
```

After that, you have to download dataset from https://github.com/lukkiddd-tdg/movielens-small/tree/main and it's will show movielens-small folder.

Next, exporting recommendation model by running "traning_model_and_integration_result.ipynb" notebook which the model will be saved at './app/weight' folder named "recommend_algor"

Then you can run api server by
```
$ uvicorn app.main:app [--log-level debug] [--port 10001]
```

----

# How to send the request by using CURL
1. return only content id
2. return the content metadata
3. return the model features
```
$ curl --location 'localhost:8000/recommendations?user_id=18'
$ curl --location 'localhost:8000/recommendations?user_id=18&returnMetadata=true'
$ curl --location 'localhost:8000/features?user_id=18'
```


----

# How to use unit-test and integration test
All test case will be "tests/" folder that contains two test files:
1. test_unit.py is for unit-tests each method in recommendation function
2. test_main.py is for integration test for API application

and you can run test by
```
$ pytest
```
----

Here is the result
=======
* GET /recommendations
![screenshot](./images/recommend_output.png)

<br>

* GET /recommendations (with metadata)
![screenshot](./images/recommend_output_wMetadata.png)

<br>

* GET /features 
![screenshot](./images/show_features.png)

How to improve in the future
========================

Improving recommendation model
-----------------------

1. Experiment with multiple models to find the highest accuracy.
2. Select appropriate features to enhance the accuracy of the recommendation system.
3. Using data for content recommendation may encounter seasonality issues due to changes in user behavior, necessitating regular model retraining.

Fine tune recommendation model
-----------------------
1. Use k-fold cross validation for creating generalization model.
2. Use Grid search to adjust hyperparameters.
3. Experiment with a variety of similarity measures.



Using A/B testing for chosing model
--------

Using an A/B testing model in cases where there are multiple models with similar accuracy makes it difficult to decide which one to use. This method helps in selecting a more appropriate algorithm.

Speed performance for customer facing
---------

The latency of the recommendation system is crucial because it needs to handle a large amount of historical data and may impact business expectations. If it cannot deliver results in a timely manner, it could affect business outcomes. Therefore, designing a suitable infrastructure for production and selecting efficient algorithmic techniques that provide fast and effective results are essential.