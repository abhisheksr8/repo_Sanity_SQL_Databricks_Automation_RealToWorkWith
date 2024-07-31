from perftest_abhisheks_e2etests_sanity_sql_databricks_automation_realtoworkwith_sql_db_parent_airflowcomposerjob.utils import *

def Model_0():
    from airflow.operators.python import PythonOperator
    from datetime import timedelta
    import os
    import zipfile
    import tempfile

    return PythonOperator(
        task_id = "Model_0",
        python_callable = invoke_dbt_runner,
        op_kwargs = {
          "is_adhoc_run_from_same_project": False,
          "is_prophecy_managed": False,
          "run_deps": False,
          "run_seeds": True,
          "run_parents": True,
          "run_children": True,
          "run_tests": True,
          "run_mode": "project",
          "entity_kind": "model",
          "entity_name": None,
          "project_id": "28402",
          "git_entity": "branch",
          "git_entity_value": "test_Automation_Branch",
          "git_ssh_url": "https://github.com/abhisheksr8/repo_Sanity_SQL_Databricks_Automation_RealToWorkWith.git",
          "git_sub_path": "",
          "select": "",
          "exclude": "",
          "run_props": " --profile run_profile",
          "envs": {"DBT_DATABRICKS_INVOCATION_ENV" : "prophecy", "DBT_PROFILES_DIR" : "/home/airflow/gcs/data"}
        },
    )
