from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

c = (
    Pie(init_opts=opts.InitOpts(page_title='环形饼状图', theme='white', ))
        .add(
        '',
        [list(z) for z in zip(Faker.choose(), Faker.values())],
        radius=['10%', '55%'],  # 设置内半径，外半径
        rosetype='radius',  # 每一块饼的半径大小是不是随着数值的大小改变的
    )
        .set_colors(
        ['blue', 'green', 'yellow', 'red', 'pink', 'orange', 'purple']  # 分别设置颜色
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(title='环形饼状图'),  # 这个是设置标题
        legend_opts=opts.LegendOpts(orient='vertical', pos_top='15%', pos_left='2%'), )
        .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{c}'))
        .render()  # 生成html文件括号中放那个路径和文件名
)
