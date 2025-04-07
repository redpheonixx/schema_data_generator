## Schema Data Generator
Define the schema in schema.yaml and deploy the flask application to create a endpoint which you can hit to generate dummy data in realtime to test your data pipeline.

## Clickstream Data Generator
Schema.yaml is by default having schema for clickstream data which one can reference to edit the schema file

## Milestones
- [X] Clickstream Data Generation
- [ ] Deployment Guidelines 
- [ ] Authenticator setup
- [ ] Json upload to extract schema



## How to run
1. Activate your environment
    ```
    python -m venv myenv 
    source myenv/bin/activate  # For macOS/Linux
    myenv\Scripts\activate     # For Windows 
    ```
2. Install python modules

    ```pip install -r requirements.txt```

3. Run the flask application

    ```python app.py```

## Deployment Guides
1. Pythonanywhere by ANACONDA deployment guide (free for 3 months) - *schema_data_generator/Deployment_Guide/python_anywhere.md*
