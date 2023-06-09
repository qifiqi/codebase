"""散点坐标系图（散点雷达图）"""
import random
from pyecharts import options as opts
from pyecharts.charts import Polar

data = [
    (i, random.randint(1, 100)) for i in range(101)
]
data1 = [
    (i, random.randint(1, 100)) for i in range(101)
]
c = (
    Polar()
    .add(
        'bbb',
        data,
        type_='scatter',
        # type_='effectScatter',effect_opts=opts.EffectOpts(scale=10,period=5),#设置涟漪图表
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add(
        'aaa',
        data1,
        type_='scatter',
        # type_='effectScatter',effect_opts=opts.EffectOpts(scale=10,period=5),#设置涟漪图表
        label_opts=opts.LabelOpts(is_show=False),

    )
    # .set_colors(
    #     ['yellow','red']
    # )
    .set_global_opts(
        title_opts=opts.TitleOpts(title='散点坐标图'),
    )
    # .set_series_opts(
    #     label_opts=opts.LabelOpts(formatter='({b},{c})')
    # )
    .render('雷达散点坐标系.html')
)

