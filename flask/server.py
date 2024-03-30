from flask import Flask
from typing import List
import logging
import traceback


def register_blueprints(app: Flask, list_bp: List):
    for bp in list_bp:
        app.register_blueprint(bp)

def create_app():
    app = Flask(__name__)

    import secrets 
    
    app.secret_key = secrets.token_hex(128)
    
    logger = configure_logging(app, "DEBUG")

    try:
        logger.info("Starting Blueprints registration...")
        
        from index import index_bp

        list_bp = [index_bp]

        register_blueprints(app, list_bp)
        logger.info("Successfully registered Blueprints.")
    except:
        logger.critical("Unable to register Blueprints.", exc_info=traceback.format_exc())
    
    try:
        logger.info("Starting error handler registration...")
        app.register_error_handler(404, page_not_found)
        logger.info("Successfully registered error handler.")
    except:
        logger.critical("Unable to register error handler.", exc_info=traceback.format_exc())
    
    return app

def page_not_found(error):
    return "<h3>Oops! Page not found.</h3>"

def configure_logging(app: Flask, log_level: str):
    logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    logger.info(f"Logger configured, level is {logger.getEffectiveLevel()}")
    return logger

segmentation_app = create_app()

if __name__ == "__main__":
    segmentation_app.run(port=8080, host="0.0.0.0", debug=True)