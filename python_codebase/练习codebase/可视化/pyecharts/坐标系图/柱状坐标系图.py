from pyecharts import options as opts
from pyecharts.charts import Polar
from pyecharts.faker import Faker

c = (
    Polar()
        .add_schema(
        angleaxis_opts=opts.AngleAxisOpts(
            data=Faker.week,  # 这个是pyecharts自带的数据，到时候改了就可以
            type_='category')
    )
        .add('A', [1, 2, 3, 4, 3, 5, 1], type_='bar', stack='stack0')
        .add('B', [2, 3, 6, 1, 2, 3, 1], type_='bar', stack='stack0')
        .add('C', [1, 2, 3, 4, 3, 2, 5], type_='bar', stack='stack0')
        .set_global_opts(
        title_opts=opts.TitleOpts(title='柱状坐标系图')
    )
        .render('柱状坐标系图.html')
)
