from flaskr import create_app

app = create_app()


@app.cli.command("init-db")
def init_db_command():
    with app.app_context():
        from flaskr.extensions import db

        db.create_all()

    print("Successfully created tables")


if __name__ == "__main__":
    app.run(debug=True)
