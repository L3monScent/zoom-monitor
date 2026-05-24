FROM python:3
COPY zoom_monitor.py .
RUN pip install requests
CMD python zoom_monitor.py
