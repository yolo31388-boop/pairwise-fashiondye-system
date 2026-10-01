"""时装染色 - 带6个bug"""
from dataclasses import dataclass, field

@dataclass
class Fashion:
    fid: str
    name: str
    is_limited: bool
    main_color: str
    effect_color: str

class FashionDyeSystem:
    def __init__(self):
        self.fashions: dict[str, Fashion] = {}
        self.saved_schemes = {}  # bug3: 未实现

    def dye(self, fid, color):
        f = self.fashions[fid]
        # bug1: 只改主色
        f.main_color = color
        return True

    def get_palette(self):
        # bug2: 固定调色板
        return ["red", "blue", "green", "yellow"]

    def save_scheme(self, player_id, scheme):
        # bug3: 不保存
        return True

    def get_dye_cost(self, channels):
        # bug4: 固定消耗
        return 10

    def can_dye_limited(self, fid):
        # bug5: 限定不能染
        f = self.fashions[fid]
        return not f.is_limited

    def dye_with_preview(self, fid, color):
        # bug6: 无预览直接生效
        return self.dye(fid, color)
