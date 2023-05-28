from flask import Blueprint, json, jsonify, abort, request
from ..models import User, Expense, db

bp_expenses = Blueprint('expenses', __name__, url_prefix='/expenses')

@bp_expenses.route('', methods=['GET'])
def index():
    expenses = Expense.query.all()
    result = []
    for expense in expenses:
        result.append(expense.serialize())
    return jsonify(result)

@bp_expenses.route('/create', methods=['POST'])
def create_expense():
    expense_name = request.json['expense_name']
    expense_amount = request.json['expense_amount']
    user_id = request.json['user_id']
    category = request.json['category']
    
    new_expenses = Expense(expense_name, expense_amount, user_id, category)
    
    new_expenses.insert()
    
    return jsonify(new_expenses.serialize())
