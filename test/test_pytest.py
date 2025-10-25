"""
Pytest tests for Financial Calculator
Enhanced testing with parametrization and edge cases
"""

import pytest
import math
from src.financial_calculator import (
    compound_interest, monthly_payment, investment_return,
    portfolio_value, risk_assessment, future_value_annuity,
    add_numbers, subtract_numbers
)

class TestCompoundInterest:
    
    def test_compound_interest_basic(self):
        """Test basic compound interest calculation"""
        result = compound_interest(1000, 0.05, 2, 4)
        expected = 1000 * (1 + 0.05/4) ** (4 * 2)
        assert result == round(expected, 2)
    
    def test_compound_interest_annual(self):
        """Test annual compounding"""
        result = compound_interest(5000, 0.08, 3, 1)
        assert result == 6298.56
    
    def test_compound_interest_zero_rate(self):
        """Test with zero interest rate"""
        result = compound_interest(1000, 0, 5, 12)
        assert result == 1000.0
    
    def test_compound_interest_invalid_inputs(self):
        """Test error handling for invalid inputs"""
        with pytest.raises(ValueError):
            compound_interest(-1000, 0.05, 2)
        with pytest.raises(ValueError):
            compound_interest(1000, -0.05, 2)
        with pytest.raises(ValueError):
            compound_interest("1000", 0.05, 2)

class TestMonthlyPayment:
    
    def test_monthly_payment_standard_loan(self):
        """Test standard 30-year mortgage"""
        result = monthly_payment(200000, 0.04, 30)
        expected = 954.83  # Pre-calculated value
        assert result == expected
    
    def test_monthly_payment_zero_interest(self):
        """Test loan with zero interest"""
        result = monthly_payment(12000, 0, 2)
        assert result == 500.0  # 12000 / 24 months
    
    def test_monthly_payment_invalid_inputs(self):
        """Test error handling"""
        with pytest.raises(ValueError):
            monthly_payment(0, 0.05, 10)
        with pytest.raises(ValueError):
            monthly_payment(10000, -0.01, 5)

class TestInvestmentReturn:
    
    def test_investment_return_positive(self):
        """Test positive investment return"""
        result = investment_return(1000, 1500, 3)
        expected = ((1500/1000)**(1/3) - 1) * 100
        assert result == round(expected, 2)
    
    def test_investment_return_loss(self):
        """Test investment loss"""
        result = investment_return(1000, 800, 2)
        assert result < 0
    
    @pytest.mark.parametrize("initial,final,years,expected", [
        (1000, 2000, 2, 41.42),  # Doubled in 2 years
        (5000, 6000, 1, 20.0),   # 20% return in 1 year
        (10000, 15000, 3, 14.47) # ~14.5% annualized
    ])
    def test_investment_return_parametrized(self, initial, final, years, expected):
        """Test various investment scenarios"""
        result = investment_return(initial, final, years)
        assert abs(result - expected) < 0.1

class TestPortfolioValue:
    
    def test_portfolio_value_single_investment(self):
        """Test portfolio with single investment"""
        investments = [{'amount': 10000, 'return_rate': 8.5}]
        result = portfolio_value(investments)
        assert result == {'total_value': 10000.0, 'weighted_avg_return': 8.5}
    
    def test_portfolio_value_multiple_investments(self):
        """Test diversified portfolio"""
        investments = [
            {'amount': 10000, 'return_rate': 7.0},
            {'amount': 5000, 'return_rate': 12.0},
            {'amount': 15000, 'return_rate': 5.0}
        ]
        result = portfolio_value(investments)
        expected_total = 30000.0
        expected_return = (10000*7.0 + 5000*12.0 + 15000*5.0) / 30000
        assert result['total_value'] == expected_total
        assert result['weighted_avg_return'] == round(expected_return, 2)
    
    def test_portfolio_value_invalid_inputs(self):
        """Test error handling"""
        with pytest.raises(ValueError):
            portfolio_value([])
        with pytest.raises(ValueError):
            portfolio_value([{'amount': 1000}])  # Missing return_rate

class TestRiskAssessment:
    
    def test_risk_assessment_basic(self):
        """Test basic risk metrics"""
        returns = [8.0, 12.0, -3.0, 15.0, 6.0]
        result = risk_assessment(returns)
        
        assert 'mean_return' in result
        assert 'volatility' in result
        assert 'sharpe_ratio' in result
        assert result['mean_return'] == 7.6
    
    def test_risk_assessment_zero_volatility(self):
        """Test with constant returns (zero volatility)"""
        returns = [5.0, 5.0, 5.0, 5.0]
        result = risk_assessment(returns)
        assert result['volatility'] == 0.0
        assert result['sharpe_ratio'] == 0.0
    
    def test_risk_assessment_single_return(self):
        """Test with single return"""
        returns = [10.0]
        result = risk_assessment(returns)
        assert result['mean_return'] == 10.0
        assert result['volatility'] == 0.0

class TestFutureValueAnnuity:
    
    def test_future_value_annuity_basic(self):
        """Test basic annuity calculation"""
        result = future_value_annuity(1000, 0.05, 10)
        expected = 1000 * (((1.05**10) - 1) / 0.05)
        assert result == round(expected, 2)
    
    def test_future_value_annuity_zero_rate(self):
        """Test annuity with zero interest"""
        result = future_value_annuity(500, 0, 12)
        assert result == 6000.0  # 500 * 12

class TestLegacyFunctions:
    
    def test_add_numbers(self):
        """Test legacy add function"""
        assert add_numbers(5, 3) == 8
        assert add_numbers(-2, 7) == 5
    
    def test_subtract_numbers(self):
        """Test legacy subtract function"""
        assert subtract_numbers(10, 3) == 7
        assert subtract_numbers(5, 8) == -3
    
    def test_legacy_functions_error_handling(self):
        """Test error handling for legacy functions"""
        with pytest.raises(ValueError):
            add_numbers("5", 3)
        with pytest.raises(ValueError):
            subtract_numbers(5, "3")