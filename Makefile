install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
			pip install "apache-airflow[celery]==2.1.4" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.1.4/constraints-3.8.txt"