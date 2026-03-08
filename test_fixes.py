#!/usr/bin/env python3
"""
Simple test to verify the attribution window fixes work correctly.
"""

from attribution.window_calculator import is_within_attribution_window

def test_attribution_window():
    """Test that attribution window calculation works correctly."""
    
    # Test case 1: touchpoint 10 days before conversion (should be True)
    result1 = is_within_attribution_window("2024-01-20", "2024-01-30", window_days=30)
    print(f"Test 1 - Touchpoint 10 days before conversion: {result1} (expected: True)")
    
    # Test case 2: touchpoint after conversion (should be False)  
    result2 = is_within_attribution_window("2024-02-05", "2024-01-30", window_days=30)
    print(f"Test 2 - Touchpoint after conversion: {result2} (expected: False)")
    
    # Test case 3: touchpoint exactly at conversion date (should be True)
    result3 = is_within_attribution_window("2024-01-30", "2024-01-30", window_days=30)
    print(f"Test 3 - Touchpoint on conversion date: {result3} (expected: True)")
    
    # Test case 4: touchpoint 35 days before (should be False with 30-day window)
    result4 = is_within_attribution_window("2023-12-26", "2024-01-30", window_days=30)
    print(f"Test 4 - Touchpoint 35 days before (outside window): {result4} (expected: False)")
    
    all_passed = result1 and not result2 and result3 and not result4
    print(f"\nAll tests passed: {all_passed}")
    
    return all_passed

if __name__ == "__main__":
    test_attribution_window()