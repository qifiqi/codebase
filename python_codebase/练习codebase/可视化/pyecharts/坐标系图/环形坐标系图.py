from pyecharts import options as opts
from pyecharts.charts import Polar
from pyecharts.faker import Faker
c=(
    Polar()
    .add_schema(
        radiusaxis_opts=opts.RadiusAxisOpts(
            data=Faker.week,
            type_='category'
        ),
        angleaxis_opts=opts.AngleAxisOpts(
            is_clockwise=True,
            max_=10
        ),
    )
    .add(
        '数值',
        [1,2,3,4,3,5,1],
        type_='bar'
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title='环形坐标系图'),
        # toolbox_opts=opts.ToolBoxFeatureRestoreOpts(is_show=True)
    )
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=True)

    )

    .render('环形坐标系图.html')
)