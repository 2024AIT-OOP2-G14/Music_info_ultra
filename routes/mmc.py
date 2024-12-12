from flask import Blueprint, render_template, request, redirect, url_for
from models import Order, User, Product


# Blueprintの作成
order_bp = Blueprint('order', __name__, url_prefix='/orders')

