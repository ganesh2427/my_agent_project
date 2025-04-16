#!/bin/bash
pip install -r requirements.txt
streamlit run frontend/streamlit_app.py --server.port 7860 --server.headless true