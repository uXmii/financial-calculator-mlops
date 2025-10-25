"""
Financial Calculator Module
Enhanced MLOps Lab with Financial Analysis Functions
Author: uXmii
"""

import math
from typing import Union, List, Dict

def compound_interest(principal: float, rate: float, time: float, n: int = 1) -> float:
    """
    Calculate compound interest.
    
    Args:
        principal (float): Initial amount of money
        rate (float): Annual interest rate (as decimal, e.g., 0.05 for 5%)
        time (float): Time in years
        n (int): Number of times interest is compounded per year
    
    Returns:
        float: Final amount after compound interest
        
    Raises:
        ValueError: If any parameter is invalid
    """
    if not all(isinstance(x, (int, float)) for x in [principal, rate, time]):
        raise ValueError("Principal, rate, and time must be numbers")
    if principal < 0 or rate < 0 or time < 0 or n <= 0:
        raise ValueError("Values must be non-negative, n must be positive")
    
    amount = principal * (1 + rate/n) ** (n * time)
    return round(amount, 2)

def monthly_payment(principal: float, rate: float, years: int) -> float:
    """
    Calculate monthly loan payment using formula: M = P * [r(1+r)^n] / [(1+r)^n - 1]
    
    Args:
        principal (float): Loan amount
        rate (float): Annual interest rate (as decimal)
        years (int): Loan term in years
    
    Returns:
        float: Monthly payment amount
    """
    if not all(isinstance(x, (int, float)) for x in [principal, rate, years]):
        raise ValueError("All inputs must be numbers")
    if principal <= 0 or rate < 0 or years <= 0:
        raise ValueError("Principal and years must be positive, rate non-negative")
    
    if rate == 0:  # No interest case
        return round(principal / (years * 12), 2)
    
    monthly_rate = rate / 12
    num_payments = years * 12
    
    payment = principal * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
    return round(payment, 2)

def investment_return(initial: float, final: float, years: float) -> float:
    """
    Calculate annualized return on investment.
    
    Args:
        initial (float): Initial investment amount
        final (float): Final investment value
        years (float): Investment period in years
    
    Returns:
        float: Annualized return rate as percentage
    """
    if not all(isinstance(x, (int, float)) for x in [initial, final, years]):
        raise ValueError("All inputs must be numbers")
    if initial <= 0 or final <= 0 or years <= 0:
        raise ValueError("All values must be positive")
    
    annual_return = ((final / initial) ** (1/years) - 1) * 100
    return round(annual_return, 2)

def portfolio_value(investments: List[Dict[str, float]]) -> Dict[str, float]:
    """
    Calculate total portfolio value and weighted average return.
    
    Args:
        investments (List[Dict]): List of investments with 'amount' and 'return_rate' keys
    
    Returns:
        Dict: Portfolio total value and weighted average return
    """
    if not isinstance(investments, list) or not investments:
        raise ValueError("Investments must be a non-empty list")
    
    total_value = 0
    weighted_return = 0
    
    for investment in investments:
        if not isinstance(investment, dict):
            raise ValueError("Each investment must be a dictionary")
        if 'amount' not in investment or 'return_rate' not in investment:
            raise ValueError("Each investment must have 'amount' and 'return_rate' keys")
        
        amount = investment['amount']
        return_rate = investment['return_rate']
        
        if not isinstance(amount, (int, float)) or not isinstance(return_rate, (int, float)):
            raise ValueError("Amount and return_rate must be numbers")
        if amount < 0:
            raise ValueError("Investment amount cannot be negative")
        
        total_value += amount
        weighted_return += amount * return_rate
    
    if total_value == 0:
        return {'total_value': 0.0, 'weighted_avg_return': 0.0}
    
    avg_return = weighted_return / total_value
    return {
        'total_value': round(total_value, 2),
        'weighted_avg_return': round(avg_return, 2)
    }

def risk_assessment(returns: List[float]) -> Dict[str, float]:
    """
    Calculate basic risk metrics for a series of returns.
    
    Args:
        returns (List[float]): List of periodic returns (as percentages)
    
    Returns:
        Dict: Risk metrics including volatility and Sharpe ratio approximation
    """
    if not isinstance(returns, list) or not returns:
        raise ValueError("Returns must be a non-empty list")
    
    if not all(isinstance(r, (int, float)) for r in returns):
        raise ValueError("All returns must be numbers")
    
    n = len(returns)
    mean_return = sum(returns) / n
    
    # Calculate standard deviation (volatility)
    variance = sum((r - mean_return) ** 2 for r in returns) / (n - 1) if n > 1 else 0
    volatility = math.sqrt(variance)
    
    # Simple Sharpe ratio approximation (assuming risk-free rate = 0)
    sharpe_ratio = mean_return / volatility if volatility != 0 else 0
    
    return {
        'mean_return': round(mean_return, 2),
        'volatility': round(volatility, 2),
        'sharpe_ratio': round(sharpe_ratio, 2)
    }

def future_value_annuity(payment: float, rate: float, periods: int) -> float:
    """
    Calculate future value of ordinary annuity.
    
    Args:
        payment (float): Regular payment amount
        rate (float): Interest rate per period
        periods (int): Number of periods
    
    Returns:
        float: Future value of annuity
    """
    if not all(isinstance(x, (int, float)) for x in [payment, rate, periods]):
        raise ValueError("All inputs must be numbers")
    if payment < 0 or rate < 0 or periods < 0:
        raise ValueError("All values must be non-negative")
    
    if rate == 0:
        return round(payment * periods, 2)
    
    fv = payment * (((1 + rate) ** periods - 1) / rate)
    return round(fv, 2)

# Legacy functions for backward compatibility (from original calculator)
def add_numbers(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """Add two numbers (legacy function)."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x + y

def subtract_numbers(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """Subtract two numbers (legacy function)."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y