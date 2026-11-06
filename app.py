from flask import Flask, request, render_template, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "dev-secret-not-for-production"

def get_db():
    conn = sqlite3.connect("harmattan.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/security", methods=["GET", "POST"])
def security():
    if request.method == "POST":
        session["security"] = request.form["level"]
        return redirect("/security")
    level = session.get("security", "low")
    return render_template("security.html", level=level)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = get_db()
        conn.execute("INSERT INTO users (username, password, balance) VALUES (?, ?, ?)",
                     (username, password, 1000))
        conn.commit()
        conn.close()
        return redirect("/login")
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = get_db()
        level = session.get("security", "low")
        if level == "high":
            # SECURE: placeholders keep input locked in the data lane
            user = conn.execute(
                "SELECT * FROM users WHERE username = ? AND password = ?",
                (username, password)
            ).fetchone()
        else:
            # VULNERABLE: input glued straight into the SQL command
            query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
            user = conn.execute(query).fetchone()
        conn.close()
        if user:
            session["username"] = user["username"]
            return redirect("/dashboard")
        return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect("/login")
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE username = ?", (session["username"],)).fetchone()
    conn.close()
    return render_template("dashboard.html", user=user)

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
