import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from perftest_abhisheks_e2etests_sanity_sql_databricks_automation_realtoworkwith_sql_db_parent_airflowcomposerjob.tasks import (
    Model_0
)
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "perftest_abhisheks_e2etests_Sanity_SQL_Databricks_Automation_RealToWorkWith_SQL_DB_Parent_AirflowComposerJob", 
    schedule_interval = "0 0 1 1 *", 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.today('UTC'), 
    catchup = False, 
    max_active_runs = 1, 
    tags = []
) as dag:
    Model_0_op = Model_0()
