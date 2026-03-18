"""Tests for AiShoppingAgent."""
from src.core import AiShoppingAgent
def test_init(): assert AiShoppingAgent().get_stats()["ops"] == 0
def test_op(): c = AiShoppingAgent(); c.search(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = AiShoppingAgent(); [c.search() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = AiShoppingAgent(); c.search(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = AiShoppingAgent(); r = c.search(); assert r["service"] == "ai-shopping-agent"
