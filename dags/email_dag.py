from datetime import datetime, timedelta
import pytz
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable

import common

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 22, tzinfo=pytz.timezone('US/Eastern')),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# variables
engineers_emails = Variable.get('engineers_email')
engineers_cc = Variable.get('engineers_email_cc')
engineers_bcc = Variable.get('engineers_email_bcc')
smtp_host = Variable.get('smtp_gmail_host')
smtp_username = Variable.get('smtp_gmail_username')
smtp_pw = Variable.get('smtp_gmail_pw')


def send_email_dag(host, user, pw, recipients, cc, bcc):
    content = '<h3>This is a test email sent from dockerised Airflow!</h3>'
    sent = common.send_email_smtp(
        host, user, pw, recipients, 'Test', content, cc=cc,
        bcc=bcc
    )
    if not sent:
        raise Exception('email not sent')


# Create the DAG
with DAG(
    'send_email_dag',
    default_args=default_args,
    description='A simple DAG to send an email to a variable from Airflow',
    schedule_interval='0 21 */3 * *',  # Every three days at 9 PM EST
    catchup=False,
) as dag:

    # empty operator that does nothing
    # t_dummy = EmptyOperator(
    #     'dummy'
    # )

    # Task to send an email
    t_send_email = PythonOperator(
        task_id='send_email',
        python_callable=send_email_dag,
        op_kwargs=dict(
            host=smtp_host,
            user=smtp_username,
            pw=smtp_pw,
            recipients=engineers_emails,
            cc=engineers_cc,
            bcc=engineers_bcc,
        ),
        dag=dag,
    )

    # Set the task in the DAG
    # t_dummy >> t_send_email
    # t_send_email
