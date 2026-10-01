"""染色测试"""
import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.engine import FashionDyeSystem, Fashion

class TestDye:
    def test_effect_color_changed(self):
        fds = FashionDyeSystem()
        fds.fashions = {"f1": Fashion("f1","a",False,"white","blue")}
        fds.dye("f1", "red")
        assert fds.fashions["f1"].effect_color == "red", "光效色未改"

class TestSave:
    def test_scheme_saved(self):
        fds = FashionDyeSystem()
        fds.save_scheme("p1", {"main": "red"})
        assert "p1" in fds.saved_schemes, "方案未保存"
