from flask.cli import FlaskGroup

from project import app
# from project import db
import logging


cli = FlaskGroup(app)


# @app.before_first_request
# def setup_logging():
#     if not app.debug:
#         # In production mode, add log handler to sys.stderr.
#         app.logger.addHandler(logging.StreamHandler())
#         app.logger.setLevel(logging.INFO)
#     app.logger.info('this is an INFO message.1')


@cli.command("create_db")
def create_db():
    app.logger.info('this is an INFO message')
    # db.drop_all()
    # db.create_all()
    # db.session.commit()


if __name__ == "__main__":
    print("djdjdjdj0")
    cli()
    print("djdjdjdj")
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.logger.info('this will show in the log')
    print("djdjdjdj1")
