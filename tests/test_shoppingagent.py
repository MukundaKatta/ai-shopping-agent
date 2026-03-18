"""Tests for ShoppingAgent."""
import pytest
from src.shoppingagent import ShoppingAgent

def test_init():
    obj = ShoppingAgent()
    stats = obj.get_stats()
    assert stats["total_ops"] == 0

def test_operation():
    obj = ShoppingAgent()
    result = obj.search_products(input="test")
    assert result["processed"] is True
    assert result["operation"] == "search_products"

def test_multiple_ops():
    obj = ShoppingAgent()
    for m in ['search_products', 'compare_prices', 'analyze_reviews']:
        getattr(obj, m)(data="test")
    assert obj.get_stats()["total_ops"] == 3

def test_caching():
    obj = ShoppingAgent()
    r1 = obj.search_products(key="same")
    r2 = obj.search_products(key="same")
    assert r2.get("cached") is True

def test_reset():
    obj = ShoppingAgent()
    obj.search_products()
    obj.reset()
    assert obj.get_stats()["total_ops"] == 0

def test_stats():
    obj = ShoppingAgent()
    obj.search_products(x=1)
    obj.compare_prices(y=2)
    stats = obj.get_stats()
    assert stats["total_ops"] == 2
    assert "ops_by_type" in stats
