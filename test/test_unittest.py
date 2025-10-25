"""
Unittest tests for Financial Calculator
Comprehensive unit testing with setUp and tearDown methods
"""

import sys
import os
import unittest
import math

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src.financial_calculator import (
    compound_interest, monthly_payment, investment_return,
    portfolio_value, risk_assessment, future_value_annuity,
    add_numbers, subtract_numbers
)

class TestFinancialCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.sample_investments = [
            {'amount': 10000, 'return_rate': 8.0},
            {'amount': 5000, 'return_rate': 12.0},
            {'amount': 20000, 'return_rate': 6.0}
        ]
        self.sample_returns = [8.5, 12.3, -2.1, 15.7, 6.8, 9.2]
    
    def tearDown(self):
        """Clean up after each test method."""
        pass
    
    def test_compound_interest_calculations(self):
        """Test compound interest with various scenarios"""
        # Test basic calculation
        result = compound_interest(1000, 0.05, 2, 4)
        expected = 1000 * (1 + 0.05/4) ** (4 * 2)
        self.assertEqual(result, round(expected, 2))
        
        # Test with different compounding frequency
        result_annual = compound_interest(5000, 0.08, 3, 1)
        self.assertAlmostEqual(result_annual, 6298.56, places=2)
        
        # Test zero interest rate
        result_zero = compound_interest(1000, 0, 5)
        self.assertEqual(result_zero, 1000.0)
    
    def test_compound_interest_error_handling(self):
        """Test error handling for compound interest"""
        with self.assertRaises(ValueError):
            compound_interest(-1000, 0.05, 2)
        with self.assertRaises(ValueError):
            compound_interest(1000, -0.05, 2)
        with self.assertRaises(ValueError):
            compound_interest(1000, 0.05, -2)
    
    def test_monthly_payment_calculations(self):
        """Test monthly payment calculations"""
        # Standard 30-year mortgage
        result = monthly_payment(200000, 0.04, 30)
        self.assertAlmostEqual(result, 954.83, places=2)
        
        # Zero interest loan
        result_zero = monthly_payment(12000, 0, 2)
        self.assertEqual(result_zero, 500.0)
        
        # Short term high interest
        result_short = monthly_payment(10000, 0.12, 1)
        expected = 10000 * (0.01 * (1.01**12)) / ((1.01**12) - 1)
        self.assertAlmostEqual(result_short, round(expected, 2), places=2)
    
    def test_monthly_payment_error_handling(self):
        """Test error handling for monthly payment"""
        with self.assertRaises(ValueError):
            monthly_payment(0, 0.05, 10)
        with self.assertRaises(ValueError):
            monthly_payment(-10000, 0.05, 5)
        with self.assertRaises(ValueError):
            monthly_payment(10000, -0.01, 5)
    
    def test_investment_return_calculations(self):
        """Test investment return calculations"""
        # Positive return
        result = investment_return(1000, 1500, 3)
        expected = ((1500/1000)**(1/3) - 1) * 100
        self.assertEqual(result, round(expected, 2))
        
        # Loss scenario
        result_loss = investment_return(1000, 800, 2)
        self.assertLess(result_loss, 0)
        
        # Doubled investment
        result_double = investment_return(5000, 10000, 2)
        self.assertAlmostEqual(result_double, 41.42, places=1)
    
    def test_investment_return_error_handling(self):
        """Test error handling for investment return"""
        with self.assertRaises(ValueError):
            investment_return(0, 1000, 2)
        with self.assertRaises(ValueError):
            investment_return(1000, 0, 2)
        with self.assertRaises(ValueError):
            investment_return(1000, 1500, 0)
    
    def test_portfolio_value_calculations(self):
        """Test portfolio value calculations"""
        result = portfolio_value(self.sample_investments)
        
        expected_total = 35000.0
        expected_return = (10000*8.0 + 5000*12.0 + 20000*6.0) / 35000
        
        self.assertEqual(result['total_value'], expected_total)
        self.assertEqual(result['weighted_avg_return'], round(expected_return, 2))
    
    def test_portfolio_value_single_investment(self):
        """Test portfolio with single investment"""
        single_investment = [{'amount': 15000, 'return_rate': 9.5}]
        result = portfolio_value(single_investment)
        
        self.assertEqual(result['total_value'], 15000.0)
        self.assertEqual(result['weighted_avg_return'], 9.5)
    
    def test_portfolio_value_error_handling(self):
        """Test error handling for portfolio value"""
        with self.assertRaises(ValueError):
            portfolio_value([])
        with self.assertRaises(ValueError):
            portfolio_value([{'amount': 1000}])  # Missing return_rate
        with self.assertRaises(ValueError):
            portfolio_value([{'amount': -1000, 'return_rate': 5.0}])  # Negative amount
    
    def test_risk_assessment_calculations(self):
        """Test risk assessment calculations"""
        result = risk_assessment(self.sample_returns)
        
        # Calculate expected values manually
        mean_expected = sum(self.sample_returns) / len(self.sample_returns)
        variance = sum((r - mean_expected)**2 for r in self.sample_returns) / (len(self.sample_returns) - 1)
        volatility_expected = math.sqrt(variance)
        
        self.assertAlmostEqual(result['mean_return'], round(mean_expected, 2), places=2)
        self.assertAlmostEqual(result['volatility'], round(volatility_expected, 2), places=2)
        self.assertIsInstance(result['sharpe_ratio'], float)
    
    def test_risk_assessment_constant_returns(self):
        """Test risk assessment with constant returns"""
        constant_returns = [5.0, 5.0, 5.0, 5.0, 5.0]
        result = risk_assessment(constant_returns)
        
        self.assertEqual(result['mean_return'], 5.0)
        self.assertEqual(result['volatility'], 0.0)
        self.assertEqual(result['sharpe_ratio'], 0.0)
    
    def test_risk_assessment_error_handling(self):
        """Test error handling for risk assessment"""
        with self.assertRaises(ValueError):
            risk_assessment([])
        with self.assertRaises(ValueError):
            risk_assessment(['not', 'numbers'])
    
    def test_future_value_annuity_calculations(self):
        """Test future value annuity calculations"""
        # Basic calculation
        result = future_value_annuity(1000, 0.05, 10)
        expected = 1000 * (((1.05**10) - 1) / 0.05)
        self.assertEqual(result, round(expected, 2))
        
        # Zero interest rate
        result_zero = future_value_annuity(500, 0, 12)
        self.assertEqual(result_zero, 6000.0)
    
    def test_future_value_annuity_error_handling(self):
        """Test error handling for future value annuity"""
        with self.assertRaises(ValueError):
            future_value_annuity(-500, 0.05, 10)
        with self.assertRaises(ValueError):
            future_value_annuity(500, -0.05, 10)
    
    def test_legacy_functions(self):
        """Test legacy calculator functions"""
        # Test addition
        self.assertEqual(add_numbers(5, 3), 8)
        self.assertEqual(add_numbers(-2, 7), 5)
        self.assertEqual(add_numbers(0, 0), 0)
        
        # Test subtraction
        self.assertEqual(subtract_numbers(10, 3), 7)
        self.assertEqual(subtract_numbers(5, 8), -3)
        self.assertEqual(subtract_numbers(0, 0), 0)
    
    def test_legacy_functions_error_handling(self):
        """Test error handling for legacy functions"""
        with self.assertRaises(ValueError):
            add_numbers("5", 3)
        with self.assertRaises(ValueError):
            subtract_numbers(5, "3")
        with self.assertRaises(ValueError):
            add_numbers(None, 5)

if __name__ == '__main__':
    unittest.main(verbosity=2)