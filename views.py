from flask import *


views = Blueprint("views", __name__)

shopping_list = []


@views.route("/")
def home():
	return render_template("index.html", shopping_list=shopping_list)

@views.route("/add", methods=["POST"])
def add_item():
	item = request.form.get("item")
	if item:
		shopping_list.append(item)
	return redirect(url_for("views.home"))

@views.route("/delete/<int:item_index>")
def delete_item(item_index):
	if 0 <= item_index < len(shopping_list):
		del shopping_list[item_index]
	return redirect(url_for("views.home"))