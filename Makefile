test:
	python3 -m unittest discover -t . -s src/ -p "*_test.py"

analyze:
	python3 -m src.analysis-service.vagas_analyzer

format_topics:
	python3 -m src.utils.topic_formatter