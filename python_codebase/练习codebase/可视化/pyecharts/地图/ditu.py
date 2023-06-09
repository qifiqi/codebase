from pyecharts.charts import Map
from pyecharts import options as opts
import pandas as pd
from pyecharts.globals import ThemeType

data = pd.read_json('./疫情数据全国.json')
print(data)
c = (
    Map(init_opts=opts.InitOpts(theme=ThemeType.WHITE))

        .add(
        series_name='地区/数据',  # 这个是设置那个标签legend 的图例筛选。
        data_pair=data.values,  # 数据项，最好是直接传json
        is_selected=True,  # 是否选中图例
        selected_mode=True,  # 选中模式，表示是否支持多个选中 、 字符串取值可选'single'表示单选，或者'multiple'表示多选。

    )
        # 这个里面是放全局配置的地方
        .set_global_opts(
        title_opts=opts.TitleOpts(title="疫情地图"),  # 这个是设置了标题是标题配置项
        visualmap_opts=opts.VisualMapOpts(  #
            is_show=True,
            min_=50,
            max_=3000,
            range_color=['green', 'yellow', '#7f7522', '#224b8f', 'red'],
            range_text=['疫情严重地', '疫情低概率'],
        ))
        # 这个是设置颜色地方
        # .set_colors()
        # 这个是设置局部，或者系列配置项的地方
        .set_series_opts()
        # 这个方法是生成html文件
        .render('地图.html')

)
