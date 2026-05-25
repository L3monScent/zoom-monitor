FROM python:3
COPY zoom_monitor.py .
RUN pip install -r  requirements.txt
CMD python zoom_monitor.py
